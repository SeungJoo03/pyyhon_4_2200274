Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Turtle()
>>> t.shpae("turtle")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t.shpae("turtle")
AttributeError: 'Turtle' object has no attribute 'shpae'
>>> t.shape("turtle")
>>> 
>>> lista = [ ]
>>> color = input("색상 #1를 입력하시오: ")
색상 #1를 입력하시오: blue
>>> lista.append(color)
>>> color = input("색상 #2를 입력하시오: ")
색상 #2를 입력하시오: red
>>> lista.append(color)
>>> color = input("색상 #2를 입력하시오: ")
색상 #2를 입력하시오: black
>>> lista.append(color)
>>> 
>>> t.fillcolor(lista[0])
>>> t.begin_fill()
>>> t.circle(50)
t.end_fi
>>> ll()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l()
NameError: name 'l' is not defined
>>> t. end_fill()
>>> 
>>> t.up()
>>> t.goto(100, 0)
>>> t.down()
>>> t.fillcolor(lista[1]
t.begin_fill()
	    
SyntaxError: invalid syntax
>>> t.fillcolor(lista[1])
>>> t.begin_fill()
>>> t.circle(50)
t.end
>>> _fill()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    _fill()
NameError: name '_fill' is not defined
>>> t.end_fill()
>>> 
>>> t.up()
>>> t.goto(200, 0)
>>> t.down()
>>> t.fillcolor(lista [2])
>>> t.begin_fill()
>>> t.circle(50)
t.
>>> t.end_fill()
>>> t._screen.exitonclick()   # 화면을 마우스로 클릭해야 종료되게 하는 부분
