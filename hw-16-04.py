from turtle import *
from math import pi
colormode(255)
speed(-1)
#calculate area circle
r=int(input('radius? '))
area = pi*r**2
print('Area = ',round(area,2))

#Converter
def conv(x):
    f=32+1.8*x
    print(x,'(C)= ', f ,'(F)')
conv(int(input('celcius?????')))

#draw
def draw(x):
    begin_fill()
    for _  in range(0,x):
        forward(100)
        left(360/x)
    end_fill()
    print(draw(int(input('zzzz'))))  
color('red','blue')
draw(10)


#circle
def cir(x):
    for _ in range(0,x):
        circle(50)
        left(360/x)
    print(cir(int(input('zzzz'))))
cir(100)
    


    
