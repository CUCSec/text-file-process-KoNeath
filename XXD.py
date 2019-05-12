a='201811123018'
b=0
f=open(r'C:\Users\Ko_Ne\Desktop\text-file-process-KoNeath\log_files\201811123018.log',mode='r', encoding='utf8')
for lines in f:
        part=lines.split('：')[2]
        print(part)
        number=part.split(',')[0]
        print(number)
        if number==a:
                b=b+1
print(b)