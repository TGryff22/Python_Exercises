import time

my_time = int(input("Enter the time in seconds: "))

# for x in range(1, my_time):
    # print(x)
    # time.sleep(1) 

# for x in range(my_time,0, -1):
    # print(x)
    # time.sleep(1) 

for x in range(my_time,0, -1):
    seconds = x % 60    #  % is the modulus operator, it gives the remainder of the division
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 24
    days = int(x / 86400)
    print(f"{days}:{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIMES UP!")