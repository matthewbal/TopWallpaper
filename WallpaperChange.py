"""
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

You will need to get a reddit api client ID and secret key from 
https://www.reddit.com/prefs/apps
This step is straightforward, just login and click create new app.
Use this github page for the url redirect and about page.
"""

import praw
import urllib
import os
import ctypes
import sys
import inspect
import datetime
import json

def GetSettings():
    cfg = "config.json"
    if os.path.isfile(cfg):
        data = json.load(open(cfg))
    else:
        data = {}
        data['subreddit'] = "wallpapers"
        data['posts'] = 5
        data['client_id'] = "PUT IN CLIENT ID HERE"
        data['client_secret'] = "PUT IN SECRET KEY HERE"
        data['user_agent'] = "001"
        with open(cfg, 'w') as outfile:
            json.dump(data, outfile)

    return data

def Login(data):
    reddit = praw.Reddit(client_id=data['client_id'],
                     client_secret=data['client_secret'],
                     user_agent=data['user_agent'])
    if reddit.read_only:
        print "Got a connection"
        return reddit
    else:
        print "Failed"
    return False

def GetWalls(reddit, sub, postNum):
    walls = []
    sortOrder = 1
    for submission in reddit.subreddit(sub).top('day',limit=postNum):
        wall = {}
        wall['title'] = submission.title.encode('ascii', 'ignore').replace(" ", "_")
        wall['link'] = submission.url
        wall['sub'] = sub
        wall['order'] = str(sortOrder)
        sortOrder+=1
        walls.append(wall)        
    return walls

def MakeDirIfNone(today):
    if not os.path.exists(today):
        os.makedirs(today)

def SavePic(link, title, sub):
    now = datetime.datetime.now()
    today = str(now.year) + "_" + str(now.month) + "_" + str(now.day)
    MakeDirIfNone(sub+"_"+today)
    fullPath = sub+"_"+today+"/"+title+".jpg"
    urllib.urlretrieve(link, fullPath)
    return fullPath

def SetWallpaper(relPath):
    realPath = os.path.dirname(os.path.abspath(inspect.stack()[0][1])) + "\\" + relPath
    ctypes.windll.user32.SystemParametersInfoA(20, 0, realPath, 3)

if __name__ == "__main__":

    configData = GetSettings()
    r = Login(configData)
    walls = GetWalls(r, configData['subreddit'], configData['posts'])
    for wall in walls:
        wall['path'] = SavePic(wall['link'], wall['order']+"_"+wall['title'], wall['sub'])
    SetWallpaper(str(walls[0]['path']))




