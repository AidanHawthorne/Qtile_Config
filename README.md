# Qtile Config
## Purpose
A fun project to learn about the tiling manager and create an asthetically pleasing environment.
Following this guide wil give you more control over your desktop environment and it will teach you how to customize the config when to put your own personal twist on it
## The End Result
![Screenshot](Images/desktop2.png)
This is the setup I found worked for my needs the most. It can be much more stripped down or even more complex depending on your needs. Once you are done this you will be able to customize the config to suit your needs.
## Overview
### Time Investment
It shouldn't take you anymore than an hour to complete this setup. If you decide to customize after that be prepared to google
### Programs Running
Now to get to the meat and potatoes of the config... What is being utilized?
- Qtile
- Picom for transparency effects and rounded corners
- Fish shell (my preferred shell)
- Kitty (my preferred terminal)
- Htop as my system monitor
- Nitrogen for wallpapers (now mostly just pywal)
- Spicetify for nice spotify
- Conky for shortcuts quick reference 
- Micro as a text editor
- Rofi as a launcher (dmenu as a secondary if you want)
- Pywal which will set background and automatically adjust colours (bundled with pywalfox for firefox colours)
- Ranger for file management
- Arandr for simple monitor organization
## Process
Once you launch Qtile for the first time you might be shocked to see the baren black screen with just a couple of icons. If you have multiple monitors you may also notice that the order of your monitors is messed up.
### First steps
If your monitors are messed up and you are on Linux enter the following command to download arandr.
```
sudo apt install arandr
```
Organize your monitors however you would like (you can press apply in the top left to check if it is correct), then press the blue download arrow at the top. Once you have the shell script downloaded move it to be in your home folder for easy execution.
Next you will need python and pip installed on your system for depencies
```
sudo apt install python3-pip
```
Next were going to fire through downloading a bunch of dependencies.
### Picom
```
sudo apt install picom
```
### Htop
```
sudo apt install htop
```
### Pywal
Go to https://github.com/dylanaraps/pywal/wiki/Installation and follow their instructions to install.
### Rofi
```
sudo apt install rofi
```
### Micro
```
sudo apt install micro
```
### Ranger
```
sudo apt install ranger
```
### Conky 
```
sudo apt install conky-all
```
### Fish
```
sudo apt install fish
```
If you want further customization you can install oh my fish at https://github.com/oh-my-fish/oh-my-fish. It gives you the ability to download themes and other great things.
### Kitty
```
sudo apt install kitty
```
### The fun part
You now finally have all the dependencies installed and now you just need to download their corresponding config files. Once you have all the config files downloaded and moved to their respective folders in the .config directory you will have a working Qtile rice (rice is just a word people like to use for making a desktop environment visual appealing). From here on out I will be directing you on how to make changes to specific aspects so that you can truly make this your own.
