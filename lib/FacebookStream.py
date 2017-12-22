import requests
import json

class FacebookStream:
    pageID = 0
    pageAccessToken = 0
    StreamLocation = 0
    
    def __init__(self,pageID,pageAccessToken):
        print("Facebook Stream initialized")
        self.pageID = pageID
        self.pageAccessToken = pageAccessToken
        self.StreamLocation = self.getLiveAPIURL()
        

    def getLiveAPIURL(self):
        print("Getting Facebook Stream URL")
        URL = "https://graph.facebook.com/"+self.pageID+"/live_videos?access_token="+self.pageAccessToken
        r = requests.post(URL)
        StreamDetails = r.json()
        return(StreamDetails['secure_stream_url'])

    def getGstreamerSink(self):
        return """
            tee. ! matroskademux name=fbdemux
            fbdemux. ! queue ! videoconvert ! videorate ! videoscale ! 
            video/x-raw,width=1280,height=720,framerate=30/1 ! 
            x264enc bitrate=4000 key-int-max=2 speed-preset=veryfast ! video/x-h264,profile=baseline ! h264parse ! 
            queue ! flvmux name=fbmux 
            
            fbdemux. ! queue ! audioresample ! audio/x-raw,rate=44100 ! queue ! voaacenc bitrate=128000 ! queue ! fbmux. 
            
            fbmux. ! rtmpsink location="{location}"
        """.format(location=self.StreamLocation)