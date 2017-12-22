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
            264videotee. ! queue ! flvmux name=fbmux 
            44audiotee. ! queue  ! fbmux. 
            fbmux. ! rtmpsink location="{location}"
        """.format(location=self.StreamLocation)