#for use with REPLIT


import random
import turtle
screen = turtle.Screen()
a = turtle.Turtle()
a.speed(1000)
screen.bgcolor("black")
# variables
ecopts = 10
money = 25
ecopts_nextturn = 0
money_nextturn = 0
highscore = 0
total_money = 01
turn = 1

def citydrawing():
  print("Loading graphics, please wait...")
  a.pensize(1)
  a.setheading(0)
  a.color("white")
  a.penup()
  a.goto(0,-260)
  a.pendown()
  a.left(45)
  a.forward(375)
  for i in range(3):
    a.left(90)
    a.forward(375)
  a.penup()
  a.goto(-290, 180)
  a.pendown()
  a.left(90)
  a.forward(75)
  a.right(90)
  a.forward(25)
  a.left(90)
  a.forward(15)
  a.right(90)
  a.forward(65)
  a.pu()
  a.goto(-275, 155)
  a.color("brown")
  a.write("Mountains")
  a.goto(250, 125)
  a.pd()
  a.left(90)
  a.forward(90)
  a.color("yellow")
  a.pu()
  a.goto(275, 200)
  a.pd()
  a.right(15)
  a.pensize(5)
  for i in range(180):
    a.forward(.5)
    a.right(1)
  a.pensize(1)
  a.pu()
  a.goto(250, 100)
  a.color("gold")
  a.write("Mine")
  a.pu()
  a.goto(290, -200)
  a.pd()
  a.color(79, 53, 0)
  a.right(118)
  a.pensize(15)
  a.forward(75)
  a.pu()
  a.right(90)
  a.forward(30)
  a.left(90)
  a.pd()
  a.color("green")
  a.begin_fill()
  a.circle(30)
  a.end_fill()
  a.pu()
  a.goto(230, -180)
  a.write("forest")
  a.pu()
  a.goto(-290, -180)
  a.pd()
  a.color("blue")
  a.pensize(2)
  a.right(45)
  for i in range(180):
    a.forward(.5)
    a.right(.5)
  for i in range(180):
    a.forward(.5)
    a.right(-.5)
  a.pu()
  a.goto(-290, -210)
  a.write("ocean")
  a.goto(0, 0)

def windturbinedrawing():
  a.showturtle()
  a.left(90)
  a.pu()
  a.goto(-165, -25)
  a.pd()
  a.pensize(10)
  a.color("white")
  a.forward(75)
  a.color("white")
  for i in range(3):
    a.left(120)
    a.forward(25)
    a.backward(25)
  a.pensize(1)
  a.color("black")
  a.dot()
  a.color("white")
  a.backward(75)
  a.hideturtle()


def solardrawing():
  a.showturtle()
  a.pu()
  a.goto(-110, -25)
  a.pd()
  a.color(6, 17, 102)
  a.begin_fill()
  a.forward(50)
  a.right(90)
  a.forward(75)
  a.right(90)
  a.forward(50)
  a.right(90)
  a.forward(75)
  a.right(90)
  a.end_fill()
  a.forward(12.5)
  a.color("white")
  a.right(90)
  for i in range(3):
    a.forward(75)
    a.backward(75)
    a.left(90)
    a.pu()
    a.forward(12.5)
    a.pd()
    a.right(90)
  a.pu()
  a.forward(18.75)
  a.pd()
  a.right(90)
  for j in range(3):
    a.forward(50)
    a.backward(50)
    a.left(90)
    a.pu()
    a.forward(18.75)
    a.pd()
    a.right(90)
    a.hideturtle()

def geothermaldrawing():
  a.showturtle()
  a.setheading(0)
  a.pu()
  a.goto(0, -25)
  a.pd()
  a.color(61, 61, 61)
  a.pensize(20)
  a.forward(50)
  a.backward(40)
  a.left(90)
  a.pensize(8)
  a.color("grey")
  a.forward(50)
  a.color(61, 61, 61)
  a.pensize(5)
  a.dot()
  a.pensize(8)
  a.color("grey")
  a.backward(50)
  a.right(90)
  a.forward(30)
  a.left(90)
  a.forward(50)
  a.color(61, 61, 61)
  a.pensize(5)
  a.dot()
  a.pensize(8)
  a.color("grey")
  a.backward(50)
  a.hideturtle()

def ffdrawing():
  a.showturtle()
  a.setheading(90)
  a.pu()
  a.goto(75, -25)
  a.pd()
  a.color("red")
  a.pensize(1)
  for i in range(4):
    a.forward(50)
    a.right(90)
  a.forward(50)
  a.right(90)
  a.forward(10)
  a.left(90)
  a.forward(40)
  a.right(90)
  a.forward(5)
  a.right(90)
  a.forward(40)
  a.hideturtle()

def hydrodrawing():
  a.showturtle()
  a.pu()
  a.goto(165, 30)
  a.pd()
  a.color("blue")
  a.setheading(0)
  a.pensize(30)
  a.forward(30)
  a.color("grey")
  a.pu()
  a.goto(200, 50)
  a.pd()
  a.pensize(1)
  a.begin_fill()
  a.forward(10)
  a.right(90)
  a.forward(80)
  a.right(90)
  a.forward(60)
  a.right(90)
  a.forward(50)
  a.right(90)
  a.forward(50)
  a.left(90)
  a.forward(30)
  a.right(90)
  a.end_fill()
  a.forward(10)
  a.right(90)
  a.forward(80)
  a.left(90)
  a.begin_fill()
  a.forward(30)
  a.left(120)
  a.forward(58)
  a.left(150)
  a.forward(45)
  a.left(90)
  a.end_fill()
  a.color("blue")
  a.pu()
  a.forward(35)
  a.pd()
  a.left(45)
  for i in range(90):
    a.forward(.2)
    a.right(1)
  for j in range(90):
    a.forward(.2)
    a.left(1)
  a.setheading(90)
  a.pu()
  a.forward(20)
  a.left(90)
  a.forward(30)
  a.right(180)
  a.pd()
  a.setheading(0)
  a.left(45)
  for k in range(90):
    a.forward(.2)
    a.right(1)
  for l in range(90):
    a.forward(.2)
    a.left(1)
  a.hideturtle()

def powerplantdrawing():
  a.setheading(0)
  a.pensize(1)
  if wind_buy == 1:
    windturbinedrawing()
  if solar_buy == 1:
    solardrawing()
  if geo_buy == 1:
    geothermaldrawing()
  if ff_buy == 1:
    ffdrawing()
  if hydro_buy == 1:
    hydrodrawing()




citydrawing()

#infastructure variables
solar_buy = 0
wind_buy = 0
hydro_buy = 0
ff_buy = 0
geo_buy = 0
# game setup
print("Welcome to EcoAge! Your goal is to try to build the greatest city you can. You have to collect money to build things such as energy efficient infastructure. You obtain ecopts from building these. You can get things from the natural resource locations, but you risk losing ecopts. Negative ecopoints or negative money will result in GAME OVER")

input("Press 1 to continue")

# citydrawing()
while True:
  powerplantdrawing()
  print("your money = " + str(money))
  print("ecopts = " + str(ecopts))


  print("turbine = " + str(wind_buy))
  print("solar = " + str(solar_buy))
  print("hydroelectric = " + str(hydro_buy))
  print("geothermal = " + str(geo_buy))
  print("fossil fuel = " + str(ff_buy))
  
  useraction = input("What would you like to do? Press 1 to collect resources, 2 to got to the store, 3 to end turn, 4 to quit the game.")

#Collect
  if useraction == "1":
    print("one")
    # choose an area
    natrecsaction = input("Welcome to natural resources! Press 1 for mountains, 2 for forest, 3 for ocean, and 4 for mine")
    if natrecsaction == "1":
      print("you chose mountains!")
      # picking money and ecopts randomly
      mtsrandommoney = random.randint(0, 30)
      mtsrandomecopts = random.randint(-8, 0)
      # adding random earnings to money and ecopts
      money += mtsrandommoney
      ecopts += mtsrandomecopts
      # tellin gthe user what they earned
      print("you earned " + str(mtsrandommoney) + " money and " + str(mtsrandomecopts) + "ecopts")
    elif natrecsaction == "2": 
      print("you chose forest!")
      forrandommoney = random.randint(0, 30)
      forrandomecopts = random.randint(-8, 0)
      money += forrandommoney
      ecopts += forrandomecopts
      print("you earned " + str(forrandommoney) + " money and " + str(forrandomecopts) + "ecopts")
    elif natrecsaction == "3":
      print("you chose ocean!")
      ocnrandommoney = random.randint(0, 30)
      ocnrandomecopts = random.randint(-8, 0)
      money += ocnrandommoney
      ecopts += ocnrandomecopts
      print("you earned " + str(ocnrandommoney) + " money and " + str(ocnrandomecopts) + "ecopts")
    elif natrecsaction == "4":
      print("you chose mine!")
      minrandommoney = random.randint(0, 30)
      minrandomecopts = random.randint(-8, 0)
      money += minrandommoney
      ecopts += minrandomecopts
      print("you earned " + str(minrandommoney) + " money and " + str(minrandomecopts) + "ecopts")



#Store
  if useraction == "2":
    print("Welcome to the store! You can buy: wind:$20 (+4 ecoPts) , solar:$10 (+2 ecoPts), geothermal:$30 (+6 ecoPts), hydroelectric:$50 (+10 ecoPts), fossil fuels:$5 (-4 ecoPts)")

    #input for what to buy 
    storebuy = input("Choose what to buy! Press 1 for wind, 2 for solar, 3 for geothermal, 4 for hydroelectric, and 5 for fossil fuels.")
    #user input

    
    #buying a wind turnbine
    if storebuy == "1":
      print("You bought a wind turbine -20 dollars, +4 ecopts, +1 wind turbine")
      wind_buy += 1
      money -= 20
      ecopts_nextturn += 4


    #buying a solar
    elif storebuy == "2":
      print("You bought a solar farm -10 dollars, +2 ecopts, +1 solar farm")
      solar_buy += 1
      money -= 10
      ecopts_nextturn += 2
      
      
    #buying a geothermal
    elif storebuy == "3":
      print("You bought a geothermal plant -30 dollars, +6 ecopts, +1 geothermal")
      geo_buy += 1
      money -= 30
      ecopts_nextturn += 6
      
    #buying a hydroelectric
    elif storebuy == "4":
      print("You bought a hydroelectric plant -50 dollars, +2 ecopts, +1 hydro plant")
      hydro_buy += 1
      money -= 50
      ecopts_nextturn += 10 
      
    #buying a fossill fuel
    elif storebuy == "5":
      print("You bought a fossil fuel plant -5 dollars, -4 ecopts, +1 fossil fuels")
      ff_buy += 1
      money -= 5
      ecopts_nextturn -= 4




#New turn      
  if useraction == "3":
    print("\n\n\n\n\nnew turn!\n")
    money += money_nextturn - turn
    ecopts += ecopts_nextturn - turn
    turn *= 2 
  

#End Game
  if useraction == "4" or ecopts <= -1 or money <= -1:
    print("your final score was " + str(ecopts) + " ecopts and " + str(money) + " money")
    if ecopts > highscore:
      highscore = ecopts
      
    break
