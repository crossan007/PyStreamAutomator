#!/usr/bin/env python3

import argparse
from threading import Thread
import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstNet', '1.0')
from gi.repository import Gst, GstNet, GObject
import configparser
from lib.FacebookStream import FacebookStream



def exit_master():
    global mainloop
    print("Exiting")
    mainloop.quit()


def main():
    global args, mainloop
    #Gst.init([])
    global config 
    config = configparser.ConfigParser()
    config.read("streams.ini")
    if (config.get("StreamAutomatorSettings","StreamFacebook")):
        print("test")
        fbs = FacebookStream(config.get("Facebook","PageID"), config.get("Facebook","PageAccessToken"))
        fbs.getLiveAPIToken()

if __name__ == '__main__':
    mainloop = GObject.MainLoop()
    try:
        main()
        mainloop.run()
    except KeyboardInterrupt:
        exit_master()
