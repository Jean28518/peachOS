#!/usr/bin/python3

# app folder code inspired by https://github.com/muflone/gnome-appfolders-manager

from threading import local
from time import sleep
from gi.repository import Gio
import jtools.jessentials as je
import jtools.jfiles as jfiles
import os

SCHEMA_FOLDERS = 'org.gnome.desktop.app-folders'
SCHEMA_FOLDER = f'{SCHEMA_FOLDERS}.folder'

PATH_FOLDER = '/org/gnome/desktop/app-folders/folders/{folder}/'

OPTION_FOLDER_NAME = 'name'
OPTION_FOLDER_TRANSLATE = 'translate'
OPTION_FOLDER_APPS = 'apps'
OPTION_FOLDER_CATEGORIES = 'categories'

APPS_SETTINGS_FOLDER = ['gnome-control-center.desktop', 'software-properties-gtk.desktop', 'org.gnome.Extensions.desktop', 'gnome-language-selector.desktop', 'gnome-session-properties.desktop', 'timeshift-gtk.desktop', 'software-properties-drivers.desktop', 'org.gnome.World.PikaBackup.desktop', 'com.github.tchx84.Flatseal.desktop']
APPS_UTILITIES_FOLDER = ['io.github.celluloid_player.Celluloid.desktop', 'org.gnome.Terminal.desktop', 'simple-scan.desktop', 'org.gnome.PowerStats.desktop']
APPS_HIDE = ['htop.desktop', 'info.desktop', 'software-properties-livepatch.desktop', 'vim.desktop']

class FolderInfo(object):
    def __init__(self, folder):
        self.folder = folder
        # Get info from the settings schema
        folder_path = PATH_FOLDER.format(folder=folder)
        self.settings = Gio.Settings.new_with_path(schema_id=SCHEMA_FOLDER,
                                                   path=folder_path)
        self.name = self.settings.get_string(OPTION_FOLDER_NAME)
        self.translate = self.settings.get_boolean(OPTION_FOLDER_TRANSLATE)
        self.apps = self.settings.get_strv(OPTION_FOLDER_APPS)
        self.categories = self.settings.get_strv(OPTION_FOLDER_CATEGORIES)
        self.desktop_entry = None


    def set_title(self, title):
        self.settings.set_string(OPTION_FOLDER_NAME, title) 


def add_app_folder(folder_name, folder_title):
    # Create a new FolderInfo object and set its title
    folder_info = FolderInfo(folder_name)
    folder_info.set_title(folder_title)
    # Add the folder to the folders list
    settings_folders = Gio.Settings.new(SCHEMA_FOLDERS)
    list_folders = settings_folders.get_strv('folder-children')
    list_folders.append(folder_name)
    settings_folders.set_strv('folder-children', list_folders)
    
    elements = je.run_command("gsettings get org.gnome.desktop.app-folders folder-children", print_output=False, return_output=True)
    os.system("gsettings set org.gnome.desktop.app-folders folder-children \"" + elements[0].replace("]", ", '%s']" % folder_name)+ "\"")
    

def add_entry_to_app_folder(folder_name, entry_name):
    elements = je.run_command("gsettings get org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/%s/ apps" % folder_name, print_output=False, return_output=True)
    element_string = "" 
    if elements[0] == "@as []":
        element_string = "['%s']" % entry_name
    elif "'%s'" % entry_name in elements[0]:
        return
    else:
        element_string = elements[0].replace("]", ", '%s']" % entry_name)
    os.system("gsettings set org.gnome.desktop.app-folders.folder:/org/gnome/desktop/app-folders/folders/%s/ apps \"%s\"" % (folder_name, element_string))


def set_background_image(absolte_file_path):
    os.system("gsettings set org.gnome.desktop.background picture-uri \"file://%s\"" % absolte_file_path)


def hide_app_from_menu(desktop_file_name):
    home_folder = os.environ['HOME']
    local_file_path = "%s/.local/share/applications/%s" % (home_folder, desktop_file_name)
    if jfiles.does_file_exist("/usr/share/applications/%s" % desktop_file_name):
        if not jfiles.does_file_exist(local_file_path):
            os.system("cp /usr/share/applications/%s %s" % (desktop_file_name, local_file_path))
    else:
        return

    if jfiles.get_value_from_file(local_file_path, "Hidden", "false") == "false":
        jfiles.set_value_in_file(local_file_path, "Hidden", "true")

def main():
    # App Menu
    if (not "Settings" in je.run_command("gsettings get org.gnome.desktop.app-folders folder-children", print_output=False, return_output=True)[0]):
        add_app_folder("Settings", "Settings")

    for app in APPS_SETTINGS_FOLDER:
        add_entry_to_app_folder("Settings", app)

    for app in APPS_UTILITIES_FOLDER:
        add_entry_to_app_folder("Utilities", app)

    # Set Background
    set_background_image("/usr/share/backgrounds/peach/peach-1.jpg")

    for app in APPS_HIDE:
        hide_app_from_menu(app)


if __name__ == "__main__":
    main()
