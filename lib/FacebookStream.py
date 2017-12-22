import requests
import json

class FacebookStream:
    pageID = 0
    pageAccessToken = 0
    
    def __init__(self,pageID,pageAccessToken):
        self.pageID = pageID
        self.pageAccessToken = pageAccessToken
        

    def getLiveAPIToken(self):
        URL = "https://graph.facebook.com/"+self.pageID+"/live_videos?access_token="+self.pageAccessToken
        r = requests.post(URL)
        StreamDetails = r.json()
        print(StreamDetails['secure_stream_url'])

    def getGstreamerSink(self):
        print ("test")