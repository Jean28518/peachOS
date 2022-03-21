# peachOS
Just a small project for yet another linux desktop distro. Very easy Installation and Setup. Based on Ubuntu, Flatpak and Gnome.

**Under construction!**

## Concept
PeachOS want's to make linux accessible for new users. 
For that many applications will be developed. These aim to be as easy as possible.
By using ubuntu as a base peachOS will work the widest range of applications and is compatible to one of the most used distro.

![grafik](https://user-images.githubusercontent.com/39700889/159352692-ac687bad-9d44-4852-a156-04d983d5da79.png)

## Unique Features (coming soon)
- One Click Installer (You will really need only one click for full automatic installation)
- Very easy Welcome Screen for new users
- Automatic installation of drivers automatic maintanance. One click -> Everything is ready to go.
- Very easy software management 
- Easy Settings Manager with full support of gnome settings
- (Easy integration of windows VMs)

## How to setup peachOS for now (in development)
- Install newest Ubuntu Desktop LTS version (tested for 20.04 of 22.04) (Choose minimal installation)
- Install the files of this repo.
- Run /usr/lib/peach/update.sh

### SetUp of user workspace:
- Install these gnome addons
	- https://extensions.gnome.org/extension/1319/gsconnect/
	- https://extensions.gnome.org/extension/615/appindicator-support/
	- https://extensions.gnome.org/extension/352/middle-click-to-close-in-overview/ (!)
	- https://extensions.gnome.org/extension/307/dash-to-dock/ (!)
- Set DashToDock to bottom
- Remove these entries of menu with alacarte:
  - Livepatch
  - vim
  - htop
  - TexInfo
- Create a new Folder in Gnome Menu called "settings" with these entries:
  - Applications & Updates
  - Settings
  - AddOns
  - Language
  - StartUp Programms
  - Additional Drivers
  - Timeshift
  - Pika BackUp
  - Flatseal
- Move these entries to Folder "Utilities":
  - Terminal
  - Celluloid
  - Document Scanner
  - Energy Statistics
- Set gnome backgroud to the background in `/usr/share/backgrouds/peach/peach-1.png`

## How to build peachOS.deb:
- Download (and unzip) this repository
- `chmod +x peachOS-main/DEBIAN/postinst`
- `chmod 755 peachOS-main/DEBIAN`
- `dpkg-deb --build peachOS-main`
- Install this .deb package with `sudo dpkg --install peachOS-main.deb`
