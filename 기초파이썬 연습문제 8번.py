Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Turtle()
>>> t.shape("turtle")
>>> 
>>> lista = []
>>> lista.append(int(input("x1:  ")))
x1:  0
>>> lista.append(int(input("y1:  ")))
y1:  0
>>> lista.append(int(input("x2:  ")))
x2:  100
>>> lista.append(int(input("y2:  ")))
y2:  100
>>> lista.append(int(input("x3:  ")))
x3:  200
>>> lista.append(int(input("y3:  ")))
y3:  100
>>> t.goto(lista[0], lista[1])
>>> t.goto(lista[2]. lista[3])
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t.goto(lista[2]. lista[3])
AttributeError: 'int' object has no attribute 'lista'
>>> t.goto(lista[2], lista[3])
>>> t.goto(lista[4], lista[5])
>>> t._screen.exitonclick()
