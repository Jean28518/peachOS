# peachOS
Just a small project for yet another linux desktop distro. Very easy installation and setup. Based on Ubuntu, Flatpak and Gnome.

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
- Install the files of this repo (.deb file available).
- `sudo /usr/lib/peach/install.sh`


## How to build and install peachOS.deb:
- Download (and unzip) this repository
- `chmod +x peachOS-main/DEBIAN/postinst`
- `chmod 755 peachOS-main/DEBIAN`
- `dpkg-deb --build peachOS-main`
- `sudo dpkg --install peachOS-main.deb`

## Setup of user workspace:
- Install these gnome addons
	- https://extensions.gnome.org/extension/352/middle-click-to-close-in-overview/ (!)
	- https://extensions.gnome.org/extension/307/dash-to-dock/ (!)
- Set DashToDock to bottom
- Everything else will set up automatically