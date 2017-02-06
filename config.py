from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget

mod = "mod4"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Navigate between groups
    Key([mod], "Left",lazy.screen.prev_group()),
    Key([mod], "Right",lazy.screen.next_group()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    Key([mod], "Return", lazy.spawn('terminator')),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    # Restart Qtile
    Key([mod, "control"], "r", lazy.restart()),
    # Quit Qtile
    Key([mod, "control"], "q", lazy.shutdown()),
    # Launch command
    Key([mod], "r", lazy.spawncmd()),
]

groups = [Group(str(i)) for i in range(0, 7)]

for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], i.name, lazy.group[i.name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
    )

layouts = [
    layout.Max(),
    layout.Stack(),
    layout.Tile()
]

widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=14,
    padding=3,
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.TextBox('|'),
                widget.LaunchBar([
                    ('Firefox', 'Application/firefox/firefox', 'Web browser'),
                    ('PyCharm', 'Application/pycharm-2016.3/bin/pycharm.sh', 'Editor'),
                ]),
                widget.Prompt(),
                widget.Spacer(),
                widget.Volume(),
                widget.TextBox('|'),
                widget.Clock(format='%d-%m-%Y %a %H:%M %p'),
            ],
            25,
            background=["#042a2b"],
        ),
        bottom=bar.Bar(
            [
                widget.GroupBox(),
                widget.WindowName(foreground="#eeeeee"),
                widget.Systray(),
                widget.CPUGraph(),
                widget.MemoryGraph(),
                widget.NetGraph(),
                widget.CurrentScreen(),
            ],
            size=25,
            background="#042a2b",
            foreground="#00ff00",
        ),
    ), Screen(bottom=bar.Bar(
        [
            widget.AGroupBox(),
        ]
    ,25,
    background="#042a2b",
    foreground="#eeeeee",
    )),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
auto_fullscreen = True
focus_on_window_activation = "smart"
extentions = []

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
