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
- VSCode
- PyCharm
- Spotify
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
### Nitrogen
Install nitrogn to set and change your background picture.
```
sudo apt install nitrogen
```
Find a background you like and then set it using nitrogen. https://gitlab.com/dwt1/wallpapers has a large collection of nice wallpapers. The one in the pictures is 0277.jpg from that collection.
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
To set fish as your default shell simply enter ```which fish``` into your terminal and copy the path it returns. Then enter ```chsh``` and paste the path you copied.
If you want further customization you can install oh my fish at https://github.com/oh-my-fish/oh-my-fish. It gives you the ability to download themes and other great things.
### Kitty
```
sudo apt install kitty
```
### The fun part
You now finally have all the dependencies installed and now you just need to download their corresponding config files. For the qtile specific dot files make sure you maintain the folder structure while downloading so that it works seemlessly with the config. Once you have all the config files downloaded and moved to their respective folders in the .config/ directory you will have a working Qtile rice (rice is just a word people like to use for making a desktop environment visual appealing).  
Now that everything is installed run the command ```wal -i -n```. This will generate a colorscheme based off your background colors and will apply it to most programs installed above. The main exception being QTile with which you will manually have to figure out your colorscheme based off the colors found in ```.config/wal/```.   
You may notice your micro is not copying your terminal colors. This can be easily fixed by entering micro and hitting ctrl-E followed by ```set colorscheme simple```.  
*** Note that the qtile config.py references Spotify, VSCode, and PyCharm. Either install them or remove all references to them in config.py.  
Also, if you want to keep a clean file system than look into adding folders to your path for your designated shell (if you followed this it should be fish). This will allow you to put files you want to run in autostart.sh in a folder and still have it run.
## Bonus programs for those juicy screenshots
### Cava
Cava is an audio visualizer you can customize to match your color scheme and can be a nice addition to any screenshots. To get it go to https://github.com/karlstav/cava and follow their instructions
### Color Scripts
Probably my favourite of these few bonus programs. It's a simple script that give you custom ascii art each time you open a terminal. To install it go to https://gitlab.com/dwt1/shell-color-scripts and follow the instructions.
### Pipes
Probably one of the most common program you will see in screenshots of peoples desktop. The instructions to install can be found here https://github.com/pipeseroni/pipes.sh.
### Desktop with the eye candy
![Screenshot](Images/desktop3.png)
## Your journey
In this section I will give you a brief overview of where to go to change specific things. The rest will be up to googling and reading documentation. There is a little bit of a learning curve when you start customizing it but it is worth it when you have your own fully custom desktop environment suited to your needs.
### The bar and shortcuts
Most of your editig you want to do will be happening in your qtile config file. Open your command window and enter ```micro ~/.config/qtile/config.py```. Once you are in the folder you can begin navigating the folder. I have added comments to the file outlining what certain parts do. You can ```ctrl+f``` to find what you are looking for (bar, color, shortcuts, and layouts should cover everything you need). Once you find what you want to change simply begin editing. If you want to check how a change will look hit ```ctrl+s``` in micro and then ```mod+ctrl+r``` to refresh qtile and if the change is valid it will show. If however you notic qtile does not update there is an error somehwere in the change you made.
### Transparency and window margins
If you want to adjust the transparency settings, get rid of the rounded corners or maybe you dont like the margins, you will need to head to the picom config. To edit the file type ```micro picom.conf``` while in the home directory (I keep my conky and picom config in my home directory because I was having problems and only that seemed to solve it). You will find everything you need here to edit the appearances of your windows.
### The rest
With all the of the programs it is much of the same. I would start with editing your qtile config and then moving down the chain of config files if it is necessary (usually only conky will need changes if you add shortcuts, more editing will be needed if you decide to change color schemes).
