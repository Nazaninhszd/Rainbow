import turtle
list=['maroon','light green','dark slate blue','medium violet red'] 
t=turtle.Turtle()
t.shape('turtle')
t.width(3)
t.speed(2)
for i in range(4):
    for c in list :
        t.color(c)
        t.forward(200)
        t.left(90)
    
    
