a=201811123018
b=0
f=open('201811123018.log','r')
for lines in f:
    part=lines.split(':',-1)[2]
    number=part.split(',',-1)[0]
    if number==a:
        b=b+1
print(b)