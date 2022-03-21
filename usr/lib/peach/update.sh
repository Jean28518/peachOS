#!/bin/bash
sleep 120
echo 'running peach update...'
apt update
apt dist-upgrade -y
flatpak update -y
flatpak uninstall --unused -y
