import random
import turtle

def Head():
    tartaruga=turtle.Turtle()
    tartaruga.penup()    
    tartaruga.setpos(-200,160)
    tartaruga.pendown()
    tartaruga.color("orange")
    tartaruga.circle(20)
    
def Body():
    tartaruga=turtle.Turtle()
    tartaruga.penup()
    tartaruga.setpos(-200,160)
    tartaruga.pendown()
    tartaruga.color("orange")
    tartaruga.right(90)
    tartaruga.forward(100)
    
def RightArm():
    tartaruga=turtle.Turtle()
    tartaruga.penup()
    tartaruga.setpos(-200, 140)
    tartaruga.pendown()
    tartaruga.color("orange")
    tartaruga.right(45)
    tartaruga.forward(30)
    
def LeftArm():
    tartaruga=turtle.Turtle()
    tartaruga.penup()
    tartaruga.setpos(-200, 140)
    tartaruga.pendown()
    tartaruga.color("orange")
    tartaruga.left(45)
    tartaruga.backward(30)
    
def RightLeg():
    tartaruga=turtle.Turtle()
    tartaruga.penup()
    tartaruga.setpos(-200, 60)
    tartaruga.pendown()
    tartaruga.color("orange")
    tartaruga.right(45)
    tartaruga.forward(30)
    
def LeftLeg():
    tartaruga=turtle.Turtle()
    tartaruga.penup()
    tartaruga.setpos(-200, 60)
    tartaruga.pendown()
    tartaruga.color("orange")
    tartaruga.left(45)
    tartaruga.backward(30)
    
window = turtle.Screen()    # cria uma janela
window.bgcolor("black")
window.title("Forca")

tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(-300,0)
tartaruga.pendown()
tartaruga.color("orange")
tartaruga.left(90)
tartaruga.forward(250)
tartaruga.right(90)
tartaruga.forward(100)
tartaruga.right(90)
tartaruga.forward(50)

arquivo=open("entrada.txt","r", encoding='utf-8')
lines=arquivo.readlines()
print(lines)

#make empty clean list
listalimpa=[]
#count for each word in the dirty list
for number in range(0, len(lines)):
    #picking a dirty word
    palavra=lines[number]
    #clean the dirty word
    cleanpalavra = palavra.strip()
    #add the clean word to the clean list
    listalimpa.append(cleanpalavra)
print(listalimpa)  

#picking up a word
choice=listalimpa[random.randint(0, len(listalimpa)-1)]
print(choice)

#desenhando as linhas
tartaruga=turtle.Turtle()
tartaruga.color("green")
tartaruga.penup()
tartaruga.setpos(-290,0)
tartaruga.pendown()
for i in range(0, len(choice)):
    tartaruga.pendown()
    tartaruga.forward(40)
    tartaruga.penup()
    tartaruga.forward(20)

#starting gameplay
right=0
wrong=0
while wrong<6 and right<len(choice):
    guess = window.textinput("Guess", "Input a letter")
    while len(guess) != 1:
        guess = window.textinput("Guess", "Input a letter")
    start = 0
    while start != -1:
        start = choice.find(guess, start)    
        if start!=-1:
            tartaruga.setpos(-290+60*start,0)
            tartaruga.write(choice[start],font=("Arial",20,"normal"))
            right +=1
            start += 1
            
    if guess not in choice: 
        wrong+=1
        if wrong==1:
            Head()
        elif wrong==2:
            Body()
        elif wrong==3:
            RightArm()
        elif wrong==4:
            LeftArm()
        elif wrong==5:
            RightLeg()
        elif wrong==6:
            LeftLeg()
          
window.exitonclick()
