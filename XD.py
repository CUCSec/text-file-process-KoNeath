import os

iid=input()
a=0
for root, dirs, files in os.walk(r'C:\Users\Ko_Ne\Desktop\text-file-process-KoNeath'):
    if os.path.basename(files)==iid:
        f=open(files,'r')
        for lines in f:
            part=lines.split(':',-1)[2]
            number=part.split(',',-1)[0]
            if number==iid:
                a=a+1
        f.close()
print(a)