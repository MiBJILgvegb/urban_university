from time import sleep
from module_5.clUser import *
from module_5.clVideo import *

class UrTube:
    errors=["Имя и пароль должны быть строками.",
            "Пользователь не найден.",
            "Не подходящие данные для регистрации.",
            "Имя пользователя уже занято.",
            "Ошибка поиска.",
            "Войдите в аккаунт, чтобы смотреть видео.",
            "Вам нет 18 лет, пожалуйста покиньте страницу.",
            "Видео не найдено.",
            "Конец видео."]
    
    adult_age=18
    users=[]
    videos=[]
    current_user=None

    def __init__(self):
        users=[]
        videos=[]
        current_user=None
    def __del__(self):
        users=[]
        videos=[]
        current_user=None

    def __nickname_used(self,nickname):
        finded=False
        i=0
        if(len(self.users)>0):
            while(not finded and (i<len(self.users))):
                if(nickname==self.users[i].nickname):
                    finded=True
                    i=len(self.users)
                i+=1
        return finded
    def __is_auth(self,user):
        return isinstance(user,User)
    def __is_adult(self,is_adult):
        if(is_adult):
            return self.current_user.age>=self.adult_age
    def __get_video(self,video_name):
        #finded=False
        i=0
        #while(not finded or i<len(self.videos)):
        while(i<len(self.videos)):
            if(self.videos[i].title==video_name):
                #finded=True
                return self.videos[i]
            i+=1
        return None
    def __show(self,s):
        print(f'\r{s}', end="")

    def log_in(self,nickname, password):
        if(not(isinstance(nickname,str))or(not(isinstance(password,str)))):
            print(self.errors[0])
            return None
        if(0==len(self.users)):
            print(self.errors[1])
            return None
        finded=False
        i=0
        while(not finded or (i<len(self.users))):
            if(self.nickname_used(nickname)):
                if(hash(password)==self.users[i].password):
            #if((nickname==self.users[i].nickname)and(hash(password)==self.users[i].password)):
                   finded=True
                   self.current_user=self.users[i]
            i+=1
        return True
    def register(self,nickname, password, age):
        if(not(isinstance(nickname,str))or(not(isinstance(password,str)))or(not(isinstance(age,int)))):
            print(self.errors[2])
            return None
        if(self.__nickname_used(nickname)):
            print(self.errors[3])
            return None
        user=User(nickname, hash(password), age)
        self.users.append(user)
        self.current_user=user
        user=None
        return True
    def log_out(self):
        self.current_user=None
        return True
    def add(self,*args):
        for w in args:
            if(not isinstance(w,Video)):
                continue
            else:
                self.videos.append(w)
        pass
    def get_videos(self,video_name):
        result=None
        if(not isinstance(video_name,str)):
            print(self.errors[4])
            return v
        i=0
        while(i<len(self.videos)):
            if( self.videos[i].title.lower().find(video_name.lower())>-1 ):
                v=self.videos[i].title
                if(result==None):
                    result=[v]
                else:
                    result.append(v)
                v=None
            i+=1
        return result
    def watch_video(self,video_name):
        if(not self.__is_auth(self.current_user)):
            print(self.errors[5])
            return False
        current_video=self.__get_video(video_name)
        if(not isinstance(current_video,Video)):
            print(self.errors[7])
            return False
        if(not self.__is_adult(current_video.adult_mode)):
            print(self.errors[6])
            return False
        
        current_video.time_now=0
        print(f"Начат просмотр видео '{video_name}")
        while current_video.time_now<=current_video.duration:
            self.__show(f"{current_video.time_now}/{current_video.duration}")
            sleep(1)
            current_video.time_now+=1
        current_video.time_now=0
        print(f"\n{self.errors[8]}")