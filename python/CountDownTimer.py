import time

class CountDownTimer:
    hours = int(input("How many Hours: 1-24\n"))
    minutes = int(input("How many minutes: 1-60\n"))
    seconds = int(input("how many seconds: 1-60\n"))

    while hours > 0 or minutes > 0 or seconds > 0:
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
        if seconds > 0:
            seconds -= 1
        elif minutes > 0:
            minutes -= 1
            seconds = 59
        elif hours > 0:
            hours -= 1
            minutes = 59
            seconds = 59

    print("Time is up!!")
         