# hyprpaper change wallpaper in python

## Overview

This script provides a command-line interface to interactively select wallpapers and change the background using the Hypr wallpaper manager. It reads wallpaper data from a JSON file and allows the user to choose a wallpaper and a monitor to display it on.

## Requirements

- Python 3.x
- Hypr wallpaper manager
- JSON file containing wallpaper data

## Run the script
```
    python changewall.py
```

## Configuration
- Before executing the script, make sure to preload all the wallpapers in hyprpaper.conf.
- Configure `backgrounds.json` files as needed.
  ```
    {
      "name to display":"/path/to/file",
      "name to display":"/path/to/file"
    }
  ```
- (Optional) make an alias to launch the script in `~/.bashrc`
  ```
    alias = python "/path/to/changewall.py"
  ```
  
