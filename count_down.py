import time


def countdown_timer(seconds):
    while seconds:
        mins,secs = divmod(seconds,60)
        timeformat = '{}:{}'.format(mins,secs)
        print(timeformat,end='\r')
        time.sleep(1)
        seconds-=1

    print("time's up")

print("PLease enter the countdown seconds")
countdown_timer(5)