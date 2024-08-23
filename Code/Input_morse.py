import keyboard
import time
import csv
import pandas as pd

gflag=0
flag=1
j=0
dur=[]
gap=[]

print("Use 'm' for morse '\n' Use 'e' for end of the commands ")

with open('Input_morse.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["X", "Y"])
    while True:
        if keyboard.is_pressed('m'):
            if flag :
                start=time.time()
                if gflag :
                    gap=(start-final)
                    ++j
                    writer.writerow([gap,dur])
                flag=0
        elif flag==0 :
            final=time.time()
            dur=(final-start)
            ++j
            flag=1
            gflag=1
        if keyboard.is_pressed('e'):
            ++j
            gap=(start-final)
            writer.writerow([gap,dur])
            break;
data = pd.read_csv("Input_morse.csv")
pd.set_option('display.max_rows', None)
print(data)
