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
            h264videotee. ! queue ! matroskamux name=filemux 
            44audiotee. ! queue ! filemux. 
            filemux. ! filesink location="{path}"
        """.format(path=self.path)