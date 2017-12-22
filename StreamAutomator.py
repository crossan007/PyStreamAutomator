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
    global args, mainloop, config 
    sinksArray = []
    Gst.init([])
    config = configparser.ConfigParser()
    config.read("streams.ini")
    if (config.get("StreamAutomatorSettings","StreamFacebook")):
        fbs = FacebookStream(config.get("Facebook","PageID"), config.get("Facebook","PageAccessToken"))
        fbs.getGstreamerSink()
        sinksArray.append(fbs.getGstreamerSink())
    

    if (sinksArray.count == 1 ): 
        sinks = sinksArray[0]

    pipeline = """
        {src} ! {sinks}
    """.format(src=config.get("StreamAutomatorSettings","source"),sinks=sinksArray[0])
    print(pipeline)

     pipeline = Gst.parse_launch(pipelineText)
     self.pipeline.set_state(Gst.State.PLAYING)

if __name__ == '__main__':
    mainloop = GObject.MainLoop()
    try:
        main()
        mainloop.run()
    except KeyboardInterrupt:
        exit_master()
