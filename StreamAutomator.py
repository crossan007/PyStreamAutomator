#!/usr/bin/env python3

import argparse
from threading import Thread
import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstNet', '1.0')
from gi.repository import Gst, GstNet, GObject
import configparser
from lib.FacebookStream import FacebookStream
from lib.FileStream import FileStream



def exit_master():
    global mainloop
    print("Exiting")
    mainloop.quit()


def main():
    global args, mainloop, config 
    sinksText = ""
    Gst.init([])
    config = configparser.ConfigParser()
    config.read("streams.ini")
    if (config.get("StreamAutomatorSettings","StreamFacebook")=="true"):
        fbs = FacebookStream(config.get("Facebook","PageID"), config.get("Facebook","PageAccessToken"))
        sinksText += fbs.getGstreamerSink()

    if (config.get("StreamAutomatorSettings","StreamFile")=="true"):
        filestr = FileStream(config.get("File","Path"), config.get("File","Name"))
        sinksText +=  filestr.getGstreamerSink()
    



    pipelineText = """
        {src} ! tee name=tee 
        
        {sinks}
    """.format(src=config.get("StreamAutomatorSettings","source"),sinks=sinksText)
    print(pipelineText)

    pipeline = Gst.parse_launch(pipelineText)
    pipeline.set_state(Gst.State.PLAYING)

if __name__ == '__main__':
    mainloop = GObject.MainLoop()
    try:
        main()
        mainloop.run()
    except KeyboardInterrupt:
        exit_master()
