import os
import subprocess

# config
rofiOption = ""

# get list of players
players = subprocess.run(['playerctl', '-l'], capture_output=True, text=True).stdout.split("\n")
players.pop(len(players)-1)

# create list and input players info into class of its own
list = []
for i, player in enumerate(players):
    info = subprocess.run(['playerctl', '-p', player, 'metadata', '--format', "({{ artist }} - {{ title }})"], capture_output=True, text=True).stdout[:-1]
    statusGet = subprocess.run(['playerctl', '-p', player, 'status'], capture_output=True, text=True).stdout[:-1]
    selected = ' ' if i == 0 else ''
    if statusGet == 'Playing':
        status = " "
    else:
        status = " "
    list.append(selected + status + player.split(".")[0] + " " + info)

# preparing menu
menu = '"'+"\n".join(list)+'"'

# displaying menu
choice = os.popen('echo ' + menu + ' | rofi -dmenu -i -p "Select Players" ' + rofiOption).read()[:-1]

for i, obj in enumerate(list):
    if obj == choice:
        for j in range(i):
            os.system("playerctld shift")