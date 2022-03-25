#!/bin/bash

echo 'Installing peachOS ...'
apt update 
apt install vanilla-gnome-desktop -y
apt purge gnome-mahjongg gnome-mines gnome-sudoku cheese gnome-todo gnome-documents gnome-photos deja-dup rhythmbox gnome-music gnome-weather transmission-gtk aisleriot dconf-editor usb-creator-gtk update-manager libreoffice* totem firefox ubuntu-session -y
apt install flatpak timeshift celluloid vim htop -y
snap remove firefox
snap remove snap-store
apt autoremove --purge -y
apt dist-upgrade -y
apt purge mpv -y
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install org.mozilla.firefox -y
flatpak install org.libreoffice.LibreOffice -y
flatpak install org.gnome.World.PikaBackup -y
flatpak install com.github.tchx84.Flatseal -y
systemctl enable peach-update.service

reboot