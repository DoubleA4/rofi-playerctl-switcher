# rofi-playerctl-switcher
simple rofi script to choose player for playerctl to execute its command

## Usage
copy `playerSwitch.py` and `playerctl.sh` to `~/.config/i3/scripts/` or you can change the directory that you want inside the scripts 

to run player switcher, do
```bash
python ~/.config/i3/scripts/playerSwitch.py
```
and to control player, do
```bash
~/.config/i3/scripts/playerctl.sh [playerctl command (playerctl -h)]
```
or you can also add it to your i3 config file
```
bindsym $mod+u exec python ~/.config/i3/scripts/playerSwitch.py

bindsym XF86AudioPlay exec ~/.config/i3/scripts/playerctl.sh play-pause
bindsym XF86AudioPause exec ~/.config/i3/scripts/playerctl.sh pause
bindsym XF86AudioNext exec ~/.config/i3/scripts/playerctl.sh next
bindsym XF86AudioPrev exec ~/.config/i3/scripts/playerctl.sh previous
```
