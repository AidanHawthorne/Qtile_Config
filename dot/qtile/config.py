import os
import re
import socket
import subprocess
import psutil
from libqtile import hook
from libqtile import qtile
from typing import List  
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import Spacer, Backlight
from libqtile.widget.image import Image
from libqtile.dgroups import simple_key_binder

import colors

#Variables
mod = "mod4"
mod1 = "mod1"
browser = 'firefox'
terminal = 'kitty'
text_editor = terminal + ' micro'
file_manager1 = 'pcmanfm'
file_manager2 = terminal + ' ranger'
file_launcher1 = 'rofi -show run'
file_launcher2 = 'dmenu_run'
email_cliant = 'thunderbird'
process_viewer = terminal + ' htop'
config_menu = '.local/bin/config_menu'
websites_menu = '.local/bin/websites_menu'
colorscheme_menu = '.local/bin/colorscheme_menu'
power_menu = '.local/bin/power_menu'
music = 'spotify'
pycode = 'pycharm-community'
code = 'code'

mbfs = colors.mbfs()
doomOne = colors.doomOne()
dracula = colors.dracula()
everforest = colors.everforest()
nord = colors.nord()
gruvbox = colors.gruvbox()
custom = colors.custom()
# if you want to create your own colorscheme add it to colors.py and here

#Choose colorscheme
colorscheme = custom

#Colorschme funcstion
colors, backgroundColor, foregroundColor, workspaceColor, foregroundColorTwo = colorscheme 


#KEYBINDINGS

#Window keybindings
#change to whatever works for you. You will also need to change conky file to mirror this
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc = "Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc = "Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc = "Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc = "Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc = "Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc = "Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc = "Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc = "Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc = "Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc = "Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc = "Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc = "Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc = "Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "space", lazy.layout.toggle_split(),
        desc = "Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc = "Toggle between layouts"),
    
    # Close windows
    Key([mod, "shift"], "c", lazy.window.kill(), desc = "Kill focused window"),
   
# Close, logout and reset Qtile
    Key([mod, "control"], "r", lazy.restart(), desc = "Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc = "Shutdown Qtile"),

#Applications

    # Open Terminal    
    Key([mod], "Return", lazy.spawn(terminal), desc = "Launch terminal"),
    
    #Browser
    Key([mod, "shift"], "b", lazy.spawn(browser), desc = "Launch browser"),

    #Text editor
    Key([mod, "shift"], "n", lazy.spawn(text_editor), desc = "Launch Micro"),

    #Email cliant
    Key([mod], "e", lazy.spawn(email_cliant), desc = "Launch thunderbird"),

    #File manager
    Key([mod, "shift"], "f", lazy.spawn(file_manager2), desc = "Lauch primary file manager"),

    #Rofi
    Key([mod, "shift"], "Return", lazy.spawn(file_launcher1), desc = "Launch primary launcher"),

    #Spotify
    Key([mod, "shift"], "s", lazy.spawn(music), desc = "Launch primary spotify"),

    #Pycharm
    Key([mod, "shift"], "p", lazy.spawn(pycode), desc = "Launch primary pycharm"),

    #VsCode
    Key([mod, "shift"], "o", lazy.spawn(code), desc = "Launch primary VsCode"),

    #Rofi Bash scripts
    Key([mod], "d", lazy.spawn(file_launcher2), desc = "Launch secondary launcher"),
    Key([mod, "control"], "c", lazy.spawn(config_menu), desc = "Launch rofi configuration menu"),
    Key([mod, "control"], "b", lazy.spawn(websites_menu), desc = "Launch rofi website menu"),
    Key([mod, "control"], "t", lazy.spawn(colorscheme_menu), desc = "Launch rofi colorscheme menu"),
    Key([mod, "control"], "p", lazy.spawn(power_menu), desc = "Launch rofi power menu"),

    #Backup run launcher
    Key([mod], "r", lazy.spawncmd(), desc = "Spawn a command using a prompt widget"),

# Hardware/system control
    #Sound
    Key([mod], "u", lazy.spawn("playerctl --player='spotify' volume 0.05+")),
    Key([mod], "y", lazy.spawn("playerctl --player='spotify' volume 0.05-")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),
    Key([mod], "o", lazy.spawn("playerctl --player='spotify' play-pause")),
    Key([mod], "i", lazy.spawn("playerctl --player='spotify' next")),
    Key([mod], "p", lazy.spawn("playerctl --player='spotify' previous")),

    #Brightness
    #Key([], "XF86MonBrightnessUp", lazy.spawn("lux -a 10%")),
    #Key([], "XF86MonBrightnessDown", lazy.spawn("lux -s 10%")),

    Key([mod, "shift"], "Print", lazy.spawn('gnome-screenshot -i')),
]

groups = [Group("", layout='bsp'),
          Group("󰇮", layout='bsp'),
          Group("", layout='bsp'),
          Group("", layout='bsp'),
          Group("󰈙", layout='bsp'),
          Group("", layout='bsp'),
          Group("", layout='bsp'),
          Group("", layout='bsp'),
          Group("", layout='bsp'),
          Group("", layout='bsp')]

dgroups_key_binder = simple_key_binder(mod)


# Append scratchpad with dropdowns to groups
groups.append(ScratchPad('scratchpad', [
    DropDown('terminal2', terminal, width=0.4, height=0.5, x=0.3, y=0.3, opacity=1.0),
    DropDown('terminal', terminal, width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('text_editor', text_editor, width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('file_manager2', file_manager2, width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('process_viewer', process_viewer, width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
]))
# extend keys list with keybinding for scratchpad
keys.extend([
    Key(["control"], "0", lazy.group['scratchpad'].dropdown_toggle('terminal2')),
    Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('terminal')),
    Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('text_editor')),
    Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('file_manager2')),
    Key(["control"], "4", lazy.group['scratchpad'].dropdown_toggle('process_viewer')),
])  
# different layouts that are available if you want to see what each one is read qtile docs
layouts = [
    layout.MonadTall(border_focus = colors[8], border_normal = colors[8], border_width = 2, margin = 8),
    layout.MonadWide(margin=8, border_width=2, border_focus=colors[8], border_normal=colors[8]),
    layout.Bsp      (margin=5, border_width=2, border_focus=colors[8], border_normal=colors[8], fair=False),
    layout.Max(),
    #layout.Bsp(border_focus = colors[4], margin = 5),
    #layout.RatioTile(border_focus = colors[4], margin = 2),
    #layout.TreeTab(border_focus = colors[4], margin = 2),
    #layout.Tile(border_focus = colors[4], margin = 2),
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    #layout.Matrix(),
    #layout.MonadWide(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

#### MOUSE CALLBACKS ####

#### WIDGETS ####
widget_defaults = dict(
    font = 'Hack Nerd Font Bold',
    fontsize = 14,
    padding = 2,
    background = colors[0]
)
extension_defaults = widget_defaults.copy()

# If you want to change the top bar this is where you do it

screens = [
    Screen(
        top = bar.Bar(
            [
                widget.Image(
                    filename = '~/.config/qtile/icons/menu-pink.png',
                    scale = 'False',
                    margin_x = 8,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(file_launcher2)},
                    # mouse_callbacks just call a function on a click event 
                    # this one just launches the file_launcher
                    ),
                widget.GroupBox(
        		    padding = 4,
		            active = colors[8],
                    inactive = colors[1],
		            this_screen_border = colors[8],
		            this_current_screen_border = colors[8],
                    highlight_color = ['f8f8f2', 'f8f8f2'],
                    highlight_method = 'line',
                    ),
               widget.Prompt(
                   ),
            	    widget.WindowName(
		            foreground = colors[8],
		            padding = 8
                    ),
                widget.Chord(
                    chords_colors = {
                        'launch': (foregroundColor, foregroundColor),
                    },
                    name_transform=lambda name: name.upper(),
                    ),
                widget.TextBox(
                    text='',
                    padding = 0,
                    fontsize = 30,
                    foreground = colors[2]
                    ),
		        widget.Image(
		            filename = '~/.config/qtile/icons/ram-pink.png',
                    scale = 'False',
                    margin_x = 0,
		            background = colors[2],
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('kitty htop')}
		    ),
                widget.Memory(
		            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('kitty htop')},
		            background = colors[2],
        		    foreground = colors[8],
		            padding = 8
                    ),
                widget.TextBox(
                    text='',
                    padding = 0,
                    fontsize = 50,
                    foreground = colors[8],
                    background = colors[2]
                    ),
                widget.TextBox(
                    text='',
                    padding = 0,
                    fontsize = 30,
                    background = colors[2],
                    foreground = colors[8]
                    ),
		        widget.CPU(
		            fmt = '󰻠 {}',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('kitty glances')},
                    foreground = colors[2],
                    background = colors[8],
                    padding = 8
		            ), 
		        widget.TextBox(
                    text='',
                    padding = 0,
                    fontsize = 50,
                    foreground = colors[2],
                    background = colors[8]
                    ),
                widget.TextBox(
                    text='',
                    padding = 0,
                    fontsize = 30,
                    background = colors[8],
                    foreground = colors[2]
                    ),
		        widget.Image(
		            filename = '~/.config/qtile/icons/python-pink.png',
                    scale = 'False',
                    margin_x = 8,
		            background = colors[2],
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('python-community')}
		            ),
                widget.Image(
                    filename = '~/.config/qtile/icons/vs-pink.png',
                    scale = 'False',
                    margin_x = 8,
                    background = colors[2],
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('code')}
                    ),
                widget.Image(
                    filename = '~/.config/qtile/icons/spotify-pink.png',
                    scale = 'False',
                    margin_x = 8,
                    background = colors[2],
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('spotify')}
                    ),
                widget.TextBox(
                    text='',
                    padding = 0,
                    fontsize = 50,
                    foreground = colors[8],
		            background = colors[2]
                    ),

                widget.TextBox(
                    text='',
                    padding = 0,
                    fontsize = 30,
                    background = colors[2],
                    foreground = colors[8]
                    ),
                widget.PulseVolume(
                    foreground = colors[2],
                    background = colors[8],
                    fmt = '  {}',
                    padding = 13
                    ),
                widget.TextBox(
                    text='',
                    padding = 0,
                    fontsize = 50,
                    foreground = colors[2],
                    background = colors[8]
                    ),
                widget.TextBox(
                    text='',
                    padding = 0,
                    fontsize = 30,
                    background = colors[8],
                    foreground = colors[2]
                    ),
                widget.Clock(format='%d/%m/%Y',
		            foreground = colors[8],
                    background = colors[2],
		            padding = 8
		            ),
                widget.Clock(format='%I:%M %p',
		            foreground = colors[8],
                    background = colors[2],
		            padding = 8
		            ),
		        widget.QuickExit(
		            fmt = ' ',
		            foreground = colors[7],
		            padding = 8,
		            background = colors[2]
		            ),              
            ],
            30, # the size of the bar 
            margin = [5, 5, 0, 5], # [up, right, down, left]
            opacity = 0.8, # opacity of whole bar
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start = lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start = lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
    Click([mod, "shift"], "Button1", lazy.window.toggle_floating())
]

#dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(border_focus = colors[4], float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class = 'ssh-askpass'),  # ssh-askpass
    Match(title = 'branchdialog'),  # gitk
    Match(title = 'pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

#Programms to start on log in
@hook.subscribe.startup_once
def autostart ():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
