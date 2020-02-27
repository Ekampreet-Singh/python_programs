import time

for hour in range(0,24):
    for minute in range(0,60):
        for second in range(0,60):
            print("{}:{}:{}".format(hour,minute,second))
            time.sleep(1)