class Video:
    title=""
    duration=0
    time_now=-1
    adult_mode=False

    def __new__(cls, *args,**kwargs):
        title=""
        duration=0
        time_now=-1
        adult_mode=False

        return object.__new__(cls)
    def __del__(self):
        title=""
        duration=0
        time_now=-1
        adult_mode=False

    def __init__(self,title,duration,time_now=0,adult_mode=False):
        if(isinstance(title,str)):
            self.title=title
        if(isinstance(duration,int)):
            self.duration=duration
        if(isinstance(time_now,int)):
            self.time_now=time_now
        if(isinstance(adult_mode,bool)):
            self.adult_mode=adult_mode

    def __str__(self):
        return self.title