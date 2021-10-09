'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle, width, top_left_x, top_left_y) - to outline dartboard
  drawLine(myturtle, x_start, y_start, x_end, y_end) - to draw axes
  drawCircle(myturtle, radius) - to draw the circle
  setUpDartboard(myscreen, myturtle) - to set up the board using the above functions
  isInCircle(myturtle, circle_center_x, circle_center_y, radius) - determine if dot is in circle
  throwDart(myturtle)
  playDarts(myturtle) - a simulated game of darts between two players
  montePi(myturtle, num_darts) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################

'''
description- sets up the dartboard for the game
args- myScreen(turtle) and myturtle(turtle)
return- none
'''
def setUpDartboard(myScreen, myturtle):
	myScreen.setworldcoordinates(-2,-2,2,2)
	drawSquare(myturtle,2,-1,1)
	drawLine(myturtle,0,1,0,-1)
	drawLine(myturtle,-1,0,1,0)
	drawCircle(myturtle,1)
'''
description- draws the square of the dartboard
args- myturtle(turtle), width(int), top_left_x, top_left_y
return- none
'''
def drawSquare(myturtle, width, top_left_x, top_left_y):
	myturtle.up()
	myturtle.goto(top_left_x,top_left_y)
	myturtle.down()
	for i in range(4):
		myturtle.forward(width)
		myturtle.right(90)
'''
description- draws the axis 
args- myturtle(turtle), x_start, y_start, x_end and y_end 
return- none
'''
def drawLine(myturtle, x_start, y_start, x_end, y_end):
	myturtle.up()
	myturtle.goto(x_start, y_start)
	myturtle.down()
	myturtle.goto(x_end, y_end)
	myturtle.up()
'''
description- draws the circle
args- myturtle(turtle) and radius(integer)
return- none
'''
def drawCircle(myturtle, radius):
	myturtle.up()
	myturtle.goto(0,-1)
	myturtle.down()
	myturtle.circle(radius)
'''
description- checks whether the turtle is within 1 unit away from the origin or not
args- myturtle(turtle)
return- true(bool) and false(bool)
'''
def isInCircle(myturtle):
	if myturtle.distance(0,0)<1:
		return True
	else:
		return False
'''
description- throws the darts at random
args- myturtle(turtle)
return- true(bool) and false(bool)
'''
def throwDart(myturtle):
	myturtle.speed(0)
	myturtle.up()
	x = random.uniform(-1,1)
	y = random.uniform(-1,1)
	myturtle.goto(x,y)
	myturtle.down()
	if isInCircle(myturtle):
		myturtle.color("green")
		myturtle.dot()
		return True
	else:
		myturtle.color("red")
		myturtle.dot()
		return False
'''
description- calculates who win the game outn of the two players
args- myturtle(turtle)
return-	PLAYER ONE WINS!(string) or "PLAYER TWO WINS!"(string) or "ITS A TIE!"(string)
'''
def playDarts(myturtle):
	player_one_score = 0
	player_two_score = 0
	
	for i in range(10):
		throwDart(myturtle)
		if isInCircle(myturtle):
			player_one_score +=1
	
		throwDart(myturtle)
		if isInCircle(myturtle):
			player_two_score +=1
			
	print ("player one you have", str(player_one_score) ,"points")
	print ("player two you have", str(player_two_score) ,"points")
		
	if player_one_score > player_two_score:
		print( "PLAYER ONE WINS!")
	elif player_one_score < player_two_score:
		print( "PLAYER TWO WINS!")
	else:
		print( "ITS A TIE!")
'''
description- gives the approximation of pi 
args- darty(turtle), number_darts(integer)
return- approximation of pi(float)
'''
def montePi(darty, number_darts):
	inside_count = 0
	for i in range(number_darts):
		throwDart(darty)
		if isInCircle(darty): 
	 		inside_count +=1
	return ((inside_count/number_darts)*4)	
	 

#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
