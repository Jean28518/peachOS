#!/bin/bash

echo 'Installing peachOS ...'
apt update 
apt install vanilla-gnome-desktop -y
apt purge purge gnome-mahjongg gnome-mines gnome-sudoku cheese gnome-todo gnome-documents gnome-photos deja-dup rhythmbox gnome-music gnome-weather transmission-gtk aislerot dconf-editor usb-creator-gtk update-manager libreoffice* totem firefox ubuntu-session
apt install flatpak alacarte timeshift celluloid vim htop -y
snap remove firefox
apt autoremove --purge -y
apt upgrade -y
apt purge mpv
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install org.mozilla.firefox
flatpak install org.libreoffice.LibreOffice -y
flatpak install org.gnome.World.PikaBackup -y
flatpak install com.github.tchx84.Flatseal -y
systemctl enable peach-update.service