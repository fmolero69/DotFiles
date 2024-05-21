# `7MMF'   `7MF'  db                                  .6*"             
#   `MA     ,V                                      ,M'                
#    VM:   ,V   `7MM  `7Mb,od8 `7MM  `7MM  ,pP"Ybd ,Mbmmm.    .d*"*bg. 
#     MM.  M'     MM    MM' "'   MM    MM  8I   `" 6M'  `Mb. 6MP    Mb 
#     `MM A'      MM    MM       MM    MM  `YMMMa. MI     M8 YMb    MM 
#      :MM;       MM    MM       MM    MM  L.   I8 WM.   ,M9  `MbmmdM9 
#       VF      .JMML..JMML.     `Mbod"YML.M9mmmP'  WMbmmd9        .M' 
#                                                               .d9   
#                                                             m"'   

# Q T I L E   C O N F I G

import os
import subprocess

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from time import sleep

mod = "mod4"
terminal = "alacritty"

audR = "audacious"
bakG = "nitrogen"
filM = "thunar"
ligD = "gtksu lightdm-gtk-greeter-settings"
logO = "archlinux-logout"
locK = "betterlockscreen -l"
menR = "rofi -show drun"
runP = "gmrun"
scrS = "xfce4-screenshooter"
texE = "code"
theM = "lxappearance"
webB = "firefox"


# K E Y B I N D S

keys = [
    # Movimiento del foco de la ventana
    Key([mod], "Up", lazy.layout.up(), desc="Mover el foco hacia arriba"),
    Key([mod], "Down", lazy.layout.down(), desc="Mover el foco hacia abajo"),
    Key([mod], "Left", lazy.layout.left(), desc="Mover el foco hacia la izquierda"),
    Key([mod], "Right", lazy.layout.right(), desc="Mover el foco hacia la derecha"),
    Key([mod], "space", lazy.layout.next(), desc="Mover el foco de la ventana a la siguiente ventana"),

    # Mover ventanas
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Mover la ventana hacia arriba"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Mover la ventana hacia abajo"),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Mover la ventana hacia la izquierda"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Mover la ventana hacia la derecha"),

    # Cambiar tamaño de ventanas
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Aumentar el tamaño de la ventana hacia arriba"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Aumentar el tamaño de la ventana hacia abajo"),
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Aumentar el tamaño de la ventana hacia la izquierda"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Aumentar el tamaño de la ventana hacia la derecha"),

    # Otras acciones de ventanas
    Key([mod], "n", lazy.layout.normalize(), desc="Restablecer los tamaños de todas las ventanas"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Alternar entre dividir y no dividir los lados de la pila"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Cerrar la ventana enfocada"),
    Key([mod, "control"], "e", lazy.shutdown(), desc="Apagar Qtile"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Recargar la configuración de Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Apagar Qtile"),

    # Control de volumen
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    # Controles de música
    Key([mod, "control"], "p", lazy.spawn("mpc toggle")),
    Key([mod, "control"], "n", lazy.spawn("mpc next")),
    Key([mod, "control"], "b", lazy.spawn("mpc prev")),
    Key([mod, "control"], "s", lazy.spawn("mpc stop")),

    # Brillo
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Lanzar aplicaciones
    Key([mod], "F1", lazy.spawn(webB), desc="Lanzar navegador web"),
    Key([mod], "F2", lazy.spawn(filM), desc="Lanzar administrador de archivos"),
    Key([mod], "F3", lazy.spawn(texE), desc="Lanzar editor de texto"),
    Key([mod], "F4", lazy.spawn(theM), desc="Lanzar configuración de temas GTK"),
    Key([mod], "F5", lazy.spawn(bakG), desc="Lanzar selección de fondo de pantalla"),
    Key([mod], "F6", lazy.spawn(audR), desc="Lanzar reproductor de audio"),
    Key([mod], "F7", lazy.spawn(ligD), desc="Lanzar configuración de lightdm"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Lanzar terminal"),

    # Otras acciones
    Key([mod], "Tab", lazy.next_layout(), desc="Alternar entre diseños"),
    Key([mod], "d", lazy.spawn(runP), desc="Lanzar ventana para ejecutar programas"),
    Key([mod], "l", lazy.spawn(locK), desc="Bloquear pantalla"),
    Key([mod], "m", lazy.spawn(menR), desc="Lanzar menú Rofi"),
    Key([mod], "r", lazy.spawncmd(), desc="Ejecutar un comando usando un widget de entrada"),
    Key([mod], "x", lazy.spawn(logO), desc="Cerrar sesión"),
    Key([mod], "h", lazy.spawn("roficlip"), desc='Portapapeles'),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc='Capturar pantalla'),
    Key([mod], "t", lazy.spawn("sh -c ~/.config/rofi/scripts/themes"), desc='Cambiador de temas'),
    Key([mod], "p", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc='Menú de energía'),
    Key([], "Print", lazy.spawn(scrS), desc="Capturar pantalla")
]


# G R O U P S 

groups = [Group(f"{i+1}", label="󰏃") for i in range(6)]

for i in groups:
    keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                    ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                    ),
                ]
            )




# L A Y O U T S

layouts = [
   layout.Columns( 
        margin= [10,10,10,10],
        border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
        border_width=0,
    ),
 
     layout.Matrix(
        border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
	    margin=10,
	    border_width=0,
	),

    layout.Max(	
        border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
	    margin=10,
	    border_width=0,
    ),

    layout.Floating(
        border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
	    margin=10,
	    border_width=0,
	),

    layout.MonadTall(	
        border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
        margin=10,
	    border_width=0,
    ),

    #  layout.RatioTile(),
     layout.Tile(
        border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
    ),
]


# W I D G E T 
widget_defaults = dict(
    font="Terminess Nerd Font Mono",
    fontsize=12,
    padding=3,
)
extension_defaults = [widget_defaults.copy()]

def search():
    qtile.cmd_spawn("rofi -show drun")

def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")



# P A N E L   B A R 
screens = [
    Screen(
        top=bar.Bar(
            [
            # Left side
				widget.Spacer(length=15,
                    background='#101c29',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/launch_Icon.png',
                    margin=2,
                    background='#101c29',
                    mouse_callbacks={"Button1":search},
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                ),

                widget.GroupBox(
                    fontsize=24,
                    borderwidth=3,
                    highlight_method='block',
                    active='#add2c1',
                    block_highlight_text_color="#73a9de",
                    highlight_color='#4B427E',
                    inactive='#101c29',
                    foreground='#4B427E',
                    background='#536e86',
                    this_current_screen_border='#536e86',
                    this_screen_border='#536e86',
                    other_current_screen_border='#536e86',
                    other_screen_border='#536e86',
                    urgent_border='#536e86',
                    rounded=True,
                    disable_drag=True,
                 ),

                widget.Spacer(
                length=8,
                background='#536e86',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/1.png',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/layout.png',
                    background="#536e86"
                ),

                widget.CurrentLayout(
                    background='#536e86',
                    foreground='#101c29',
                    fmt='{}',
                    font="Terminess Nerd Font Mono",
                    fontsize=13,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/search.png',
                    margin=2,
                    background='#101c29',
                ),

                widget.Prompt(
                    background='#101c29',
                    font="Terminess Nerd Font Mono",
                    fontsize=13,
                    foreground='#86918A',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/4.png',
                ),

                widget.WindowName(
                    background = '#536e86',
                    format = "{name}",
                    font="Terminess Nerd Font Mono",
                    fontsize=13,
                    foreground='#101c29',
                    empty_group_string = 'Desktop',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/3.png',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/ram.png',
                    background='#101c29',
                ),

                widget.Spacer(
                    length=-7,
                    background='#101c29',
                ),

            # Right side
                widget.Memory(
                    background='#101c29',
                    format='{MemUsed: .0f}{mm}',
                    foreground='#86918A',
                    font="Terminess Nerd Font Mono",
                    fontsize=13,
                    update_interval=5,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/11.png',
                    background='#add2c1',
                ),

                #widget.Net(
                #    format=' {up}  {down} ',
                #    background='#283648',
                #    foreground='#86918A',
                #    font="Terminess Nerd Font Mono",
                #    prefix='k',
                #),

                #widget.Image(
                #    filename='~/.config/qtile/Assets/2.png',
                #),

                widget.TextBox(
                    font="Font Awesome 6 Free",
                    fontsize=13,
                    text="",
                    foreground="101c29",
                    background="add2c1",                   
                ),
                widget.CPU(
                    foreground="101c29",
                    background="add2c1",
                    format= 'CPU {freq_current}GHz',
                    #**powerline,
                ),             

                widget.Image(
                    filename='~/.config/qtile/Assets/10.png',
                ),
                widget.TextBox(
                    font="Font Awesome 6 Free",
                    fontsize=10,
                    text="",
                    foreground='101c29',
                    background='c5ffff', 
                ),

                widget.CheckUpdates(
                    foreground='101c29',
                    background='c5ffff', 
                    distro = "Arch_checkupdates",
                    colour_have_updates = "de935f",
                    no_update_string='No updates',
                    colour_no_updates='101c29',
                    update_interval = 30,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/9.png',
                ),

                widget.Spacer(
                    length=8,
                    background='#536e86',
                ),

                widget.Volume(
                    font="Terminess Nerd Font Mono",
                    fontsize=13,
                    theme_path='~/.config/qtile/Assets/Volume/',
                    emoji=True,
                    background='#536e86',
                ),

                widget.Spacer(
                    length=-5,
                    background='#536e86',
                ),

                widget.Volume(
                    font="Terminess Nerd Font Mono",
                    fontsize=13,
                    background='#536e86',
                    foreground='#101c29',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/8.png',
                ),

                widget.Spacer(
                    length=8,
                    background='#73a9de',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/clock.png',
                    background='#73a9deff',
                    margin_y=6,
                    margin_x=5,
                ),

                widget.Clock(
                    format='%I:%M %p',
                    background='#73a9de',
                    foreground='#101c29',
                    font="Terminess Nerd Font Mono",
                    fontsize=13,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/7.png',
                    background='#283648',
                ),

                widget.Systray(
                    background='#101c29',
                    fontsize=2,
                ),

                widget.Spacer(
                    length=12,
                    background='#101c29',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/on-off.png',
                    margin=2,
                    background='#101c29',
                    mouse_callbacks={"Button1":power},
                ),

                widget.Spacer(
                    length=12,
                    background='#101c29',
                ),
            ],
            28,
            border_color = '#101c29',
            border_width = [0,0,0,0],
            margin = [10,10,4,10],
            #margin = [15,60,6,60],

        ),
    ),

    Screen (),
]


# M O U S E 

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
	border_focus='#1F1D2E',
	border_normal='#1F1D2E',
	border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="Nitrogen"),
        Match(wm_class="Lxappearancer"),
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

# stuff
@hook.subscribe.startup_once
def autostart():
    subprocess.call([os.path.expanduser('~/.config/qtile/autostart_once.sh')])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "qtile"

# E O F
