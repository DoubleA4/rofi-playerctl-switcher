import os
import subprocess

# get list of players
players = subprocess.run(['playerctl', '-l'], capture_output=True, text=True).stdout.split("\n")
players.pop(len(players)-1)

# create class
class playersData: 
    def __init__(self, display, command): 
        self.display = display
        self.command = command

# create list and input players info into class of it's own
list = []
for player in players:
    info = subprocess.run(['playerctl', '-p', player, 'metadata', '--format', "({{ artist }} - {{ title }})"], capture_output=True, text=True).stdout[:-1]
    statusGet = subprocess.run(['playerctl', '-p', player, 'status'], capture_output=True, text=True).stdout[:-1]
    if statusGet == 'Playing':
        status = ""
    else:
        status = ""
    list.append( playersData(status + " " + player.split(".")[0] + " " + info, player.strip()) )

# preparing menu
menuArray = []
for obj in list:
    menuArray.append(obj.display)
c = '"'+"\n".join(menuArray)+'"'

# displaying menu
#choice = subprocess.Popen(['echo', c, '|', 'rofi', '-dmenu', '-p', "Select Player:"], text=True).stdout
choice = os.popen('echo ' + c + ' | rofi -dmenu -i -p "Select Players" -theme ~/.config/rofi/rofidmenu.rasi').read()[:-1]

for obj in list:
    if obj.display == choice:
        os.system("echo " + obj.command + " > ~/.config/i3/scripts/player")