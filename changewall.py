import json
import os
import subprocess

# File paths
filepath = "Path to hyprpaper.conf"
databasepath = "Path to the JSON with all the wallpapers"

# Function to display menu and select a wallpaper
def menu(data):
    # Display the available wallpapers
    for i, key in enumerate(data.keys()):
        print(str(i) + " - " + key)

    # Prompt user to select a wallpaper
    selected = int(input("Select the wallpaper: "))
    while selected < 0 or selected >= len(data):
        selected = int(input("Invalid selection. Select the wallpaper again: "))

    # Get the selected wallpaper name
    name = list(data.keys())[selected]
    wallpaper = data[name]

    # Get the display names
    hyprout = subprocess.check_output(["hyprctl", "-j", "monitors"]).decode('utf-8')
    monitors = json.loads(hyprout)
    monitor_names = [monitor['name'] for monitor in monitors]

    for i in range(len(monitor_names)):
        print(str(i) + " - " + monitor_names[i])
    decision = int(input("Insert the monitor number: "))
    while decision < 0 or decision >= len(monitor_names):
        decision = int(input("Invalid selection. Select the monitor again: "))

    monitor = monitor_names[decision]

    return wallpaper, monitor

# Main function
def main():
    # Read wallpaper data from the JSON file
    with open(databasepath, 'r') as database:
        data = json.load(database)

    # Display menu, select a wallpaper, and change the background
    wallpaper,monitor=menu(data)
    command="hyprctl hyprpaper wallpaper \""+monitor+", "+wallpaper+"\""
    os.system(command)

# Run the main function
main()
