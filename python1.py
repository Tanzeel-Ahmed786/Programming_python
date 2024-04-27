'''EXERSISE # 1 
this program was written on 20 september 2023 when i was doing a yt course on pyhton basics by codewithharry'''
import time  
timestamp1 = time.monotonic()
print(time.strftime("Date : %d-%b(%m)-%Y \nTime : %I:%M:%S %p\nTime zone = %Z"))
x = time.localtime()
if 4 < x.tm_hour  < 12 : 
    print("Good morning.Sir!")
elif 12 < x.tm_hour < 18 :
    print("Good afternoon.Sir!")
elif 18 < x.tm_hour < 21 :
    print("Good evening.Sir!")
else :
    print("It's night.Sir!")
timestamp2 = time.monotonic()
timetaken = timestamp2 - timestamp1
print("Time taken by program is :",timetaken) 