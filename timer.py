import time
my_time=int(input("Enter the time (in seconds)upto which you wanna run the timer:"))
for i in range(my_time,0,-1):
    second=int(i%60)
    minutes=int(i/60)
    hours=int(i/3600)
    print(f"{hours:02}:{minutes:02}:{second:02}")
    time.sleep(1)
print("TIME UP!!")
