# TopWallpaper

Simple Daily Wallpaper Set

Author: Matthew Balshaw
Date: 28-12-2017

Usage:
This script was only verified with windows 10 64bit, with python 2.7 installed
You will need to install praw (Reddit intefacing library)
The rest of the packages should come with a default install of python
1) Navigate to where python is installed (should be C:\Python27)
2) Navigate to the "Scripts" folder
3) Open a cmd window:
    a) Hold windows key + x
    b) press "r"
    c) type cmd
    d) hit enter
4) Drag pip.exe into the command window
6) Paste the following line into the cmd window
 install --upgrade https://github.com/praw-dev/praw/archive/master.zip
6) Hit enter
7) After a minute, PRAW should be installed, you are now ready to run the script

The script can be placed anywhere on your computer. Double click to run.
Running the script once will connect to reddit, download the top 5 wallpers,
save them into a dated folder and set the first one as the wallpaper

If you don't like the daily wallpaper, you can always go into the created folders and set one manually

To have your wallpaper automatically be changed, you can add it as a windows task
1) Search from the start menu for "Task Scheduler"
2) Select "Add Basic Task"
3) Follow the wizard and select this script when it asks you for the program to run
