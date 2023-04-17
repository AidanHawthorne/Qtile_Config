# Qtile Config
## Purpose
A fun project to learn about the tiling manager and create an asthetically pleasing environment.
Following this guide wil give you more control over your desktop environment and it will teach you how to customize the config when to put your own personal twist on it
## The End Result
![Screenshot](Images/Desktop_pic.png)
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
- Rofi as a launcher
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
