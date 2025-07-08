import datetime
import time
def setalarm():
    y,m,d,h,mi,s=eval(input("enter the date and time to set the alarm (year,month,date,hour,minute,sec)format :- "))
    set_alarm=datetime.datetime(y,m,d,h,mi,s)
    print("Alarm is set at ",set_alarm)
    
    while True:
        current_time=datetime.datetime.now()
        if current_time>=set_alarm:
            print("hey alarm is triggered")
        time.sleep(1)
        return set_alarm

def showalarm(alarms):
    print("Your Saved Alarms Are :-")
    for alarm in alarms:
        print(alarm)
    
def main():
    alarms=[]
    ch=0
    print("Welcome To Alarm Clock\nFuctions are:-\n1.Set Alarm\n 2.Show Alarms")
    while ch!=3:
        ch=int(input("enter your choice :- "))
        if ch==1:
            alarm_time=setalarm()
            alarms.append(alarm_time)
        if ch==2:
            showalarm(alarms)
        if ch==3:
            break
    print(" Thankyou !!!")
main()
        