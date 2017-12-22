from datetime import datetime

class FileStream:
    path =""
    def __init__(self,path,name):
        print("File Stream initialized")
        local_time = datetime.now()
        self.name = "{name}{date}.mkv".format(name=name,date=local_time.strftime('%Y-%m-%d-%H%M%S'))
        self.path=path+"/"+self.name

    def getGstreamerSink(self):
        return """
            d. ! queue !  videoconvert ! videorate ! videoscale ! 
            video/x-raw,width=1920,height=1080,framerate=30/1 ! 
            x264enc bitrate=4000 key-int-max=2 speed-preset=veryfast ! video/x-h264,profile=baseline ! h264parse ! 
            queue ! matroskamux name=filemux 
            
            d. ! queue ! avenc_mp2 bitrate=192000 ! queue ! filemux. 
            
            filemux. ! filesink location="{path}"
        """.format(path=self.path)