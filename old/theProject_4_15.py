__author__ = ['Armando Silveira', 'Evan Seitz', 'Anthony Bhansali']

from graphics import *

win = GraphWin("Cat Burglar: The Heist!", 540, 420)
win.setCoords(0.0, 0.0, 540, 420)
win.setBackground("black")


########################################################################################################################
# 1. GAME CONSTANTS
########################################################################################################################
# todo: make sure these constants are actually right, they're demos right now.
CENTER = Point(270, 210)
BLANK = Point(0, 0)

BED1 = [1, CENTER, '1_Bed1_Full.gif']
BED1L = [1.1, CENTER, '1_Bed1_Full.gif', BLANK, "SAY:Door won't open||It's locked."]
BATH1 = [2, CENTER, '2_Bath1_Full.gif']
BATH1C = [2.1, CENTER, 'Bathroom1_CU.gif']
BATH1E = [2.2, CENTER, '3_Bath1_Empty.gif']
HALL1 = [3, CENTER, '4_Hall1_Full.gif']
STUDY1 = [4, CENTER, '5_Study1_Half.gif']
STUDY1O = [4.1, CENTER, '6_Study1_Full.gif']
STUDY2 = [5, CENTER, '7_Study2_Full.gif']
STUDY2E = [5.1, CENTER, '8_Study2_Empty.gif']
STAIRS = [6, CENTER, '9_Hall2_Full.gif']
SAFEROOM = [7, CENTER, '14_Safe_Full.gif']
LIVING = [8, CENTER, '10_Living_Full.gif']
BED2 = [9, CENTER, '11_Bed2_Full.gif']
BATH2 = [10, CENTER, '12_Bath2_Full.gif']

# safe animation test
SAFE_ANIMATE = [99]
for k in range(1, 61):
    SAFE_ANIMATE.append(CENTER)
    SAFE_ANIMATE.append("z_" + str(k) + ".gif")

END = [100, CENTER, 'diamond_get.gif', BLANK, "SAY:Congratz||You Won!"]  # Uses the text box.

########################################################################################################################
# 2. Forming up position and inventory
########################################################################################################################
position = []

# This is ANY additional player information we might need. Keys, notes, anything, put it here. done.
inventory = ['no', 'no', 'no', 'no']  # etc. add on if needed

# The initial accumulation of data onto the list.
position.append(BED1)     # Bind to position[0], so it will be numeric position of the player. how fancy.
position.append(inventory)    # Keep track of the Items, that's kind of Important.
position.append([])           # A placeholder for frames to be manipulated while passing through functions

for j in range(61):           # if you're gonna need more than 31 sub frames, this needs to be changed.
    position[2].append(j)
j = None

########################################################################################################################
# 3. Functions, hopefully you won't actually need to look at these.
########################################################################################################################
def check():
    if win.isClosed():
        quit()

def actually_check(temp, goto, point1, point2, stuff=None):
    x = temp.getX()
    y = temp.getY()
    left = point1.getX()
    right = point2.getX()
    top = point1.getY()
    bottom = point2.getY()
    # for testing purposes todo: remove
    print("Function calling for: ", "Left: ", left, "Top: ", top, "Right: ", right, "Bottom: ", bottom)
    print("Value received: ", int(x), int(y))
    # The usage of integer callers are imperative; since checkmouse is returning floats.
    if int(x) >= left:
        if int(x) <= right:
            if int(y) >= bottom:
                if int(y) <= top:
                    position[0] = goto
                    if stuff != None:  # If there's inventory to be changed, change it.
                        position[1][stuff] = 'yes'
                        # return position, position[1][stuff]
                    # return position, position[1]
                    return 1


def hot_spots(goto1, point1=None, point2=None, stuff1=None, goto2=None, point3=Point(0, 0), point4=Point(0, 0), stuff2=None, goto3=None, point5=Point(0, 0), point6=Point(0, 0), stuff3=None, goto4=None, point7=Point(0, 0), point8=Point(0, 0), stuff4=None, goto5=None, point9=Point(0, 0), point0=Point(0, 0), stuff5=None):
    if not point1:
        position[0] = goto1
        return 0
    while True:
        # Very Beary Important.
        check()
        temp = win.checkMouse()
        done = None

        # if the user has clicked somewhere
        if temp:
            done = actually_check(temp, goto1, point1, point2, stuff1)
            if done:
                return 1
            if goto2:
                done = actually_check(temp, goto2, point3, point4, stuff2)
                if done:
                    return 2
            if goto3:
                done = actually_check(temp, goto3, point5, point6, stuff3)
                if done:
                    return 3
            if goto4:
                done = actually_check(temp, goto4, point7, point8, stuff4)
                if done:
                    return 4
            if goto5:
                done = actually_check(temp, goto5, point9, point0, stuff5)
                if done:
                    return 5
        # cannot use pollMouse without ghetto rigged graphics library.
        # temp = win.pollMouse()
        # print(temp.getX(), temp.getY())
        # todo: delete two lines below, I was being stupid
        # So that them if statements ain't gonna be doing what they ain't gotta be doin.
        # temp = None


def draw_image(wait=0):
    print("Drawing image")
    # This shit is insane, I know. # todo: remove this comment
    for i in range(1, (int((len(position[0]) - 1) / 2)) + 1):  # Gets how many images need to be displayed
        # if position[0][i * 2][-4:-3] == '.' or position[0][i * 2][-5:-4] == '.':  # if the image is an image
        if position[0][i * 2][0:3] == 'SAY':
            # print(position[0][i * 2], " was treated as a text box call")  # todo: debugging
            giggle = position[0][i * 2][4:]
            temp1, temp2 = giggle.split("||")
            textbox(temp1, temp2)
        else:  # I thought the textbox was an Image, obviously you coded it, no worries, here's how its handled
            # print(position[0][i * 2], " was treated as an image.")  # todo: debugging
            position[2][i] = Image(position[0][(i * 2) - 1], position[0][i * 2])
            position[2][i].draw(win)
            time.sleep(wait)

def clear_image():
    for i in range(len(position[2])):
        if str(type(position[2][i])) == "<class 'graphics.Image'>":
            position[2][i].undraw()

########################################################################################################################
# 4. Main program, followed by main game loop.
########################################################################################################################
def main():
    print("This is a demo so there may be outputs for planning and testing purposes.")
    # Draw and undraw Evan's title
    title(win)

    # position[0] is where the player is
    # position[1] is what the player has

    ##################################################################################################################
    # MAIN GAME LOOP
    ##################################################################################################################
    while True:
            # Bed1, starting position
            if position[0] == BED1 and position[1][0] == 'no':
                draw_image()
                hot_spots(BATH1, Point(411, 285), Point(463, 156), None, BED1L, Point(160, 284), Point(187, 192))
            # Bed1, notify user that the bed is locked
            elif position[0] == BED1L:
                draw_image()
                hot_spots(BED1)

            #  Bed1, when user has key
            elif position[0] == BED1 and position[1][0] == 'yes':
                draw_image()
                hot_spots(BATH1, Point(411, 285), Point(463, 156), None, HALL1, Point(160, 284), Point(187, 192))

            # Bath1, without key
            elif position[0] == BATH1 and position[1][0] == 'no':
                draw_image()
                hot_spots(BATH1C, Point(405, 76), Point(441, 46), 0, BED1, Point(247, 62), Point(290, 9))

            # When back at bath but already have key
            elif position[0] == BATH1 and position[1][0] == 'yes':
                # if the key is already taken, we're gonna pull a switcher roo, and display the bath w/o key
                position[0] = BATH1E
                draw_image()
                hot_spots(BED1, Point(247, 62), Point(290, 9))

            # the close up of the key
            elif position[0] == BATH1C:
                draw_image()
                hot_spots(BATH1, Point(0, 420), Point(540, 0), 0)

            # Hall1 goes no where
            elif position[0] == HALL1:
                draw_image()
                hot_spots(BED1, Point(0, 105), Point(83, 44), None, STUDY1, Point(408, 279), Point(540, 0), None, STAIRS, Point(168, 253), Point(216, 114))

            # Study 1
            elif position[0] == STUDY1:
                draw_image()
                hot_spots(HALL1, Point(232, 52), Point(307, 7), None, STUDY1O, Point(0, 420), Point(67, 118))

            elif position[0] == STUDY1O:
                draw_image()
                hot_spots(HALL1, Point(232, 52), Point(307, 7), None, STUDY2, Point(0, 420), Point(67, 118))

            elif position[0] == STUDY2 and position[1][1] == "no":
                draw_image()
                hot_spots(STUDY1O, Point(247, 62), Point(290, 9), None, STUDY2, Point(327, 87), Point(386, 45), 1)

            elif position[0] == STUDY2 and position[1][1] == "yes":
                position[0] = STUDY2E  # see above
                draw_image()
                hot_spots(STUDY1O, Point(247, 62), Point(290, 9), None)

            elif position[0] == STAIRS:
                draw_image()
                hot_spots(SAFEROOM, Point(229, 203), Point(330, 102), None, HALL1, Point(0, 50), Point(50, 0), None, LIVING, Point(171, 237), Point(187, 100))

            elif position[0] == SAFEROOM:
                draw_image()
                hot_spots(SAFE_ANIMATE, Point(182, 420), Point(350, 300), None, STAIRS, Point(463, 36), Point(530, 4))

            elif position[0] == LIVING:
                draw_image()
                hot_spots(STAIRS, Point(253, 31), Point(301, 4), None, BED2, Point(426, 219), Point(456, 144))

            elif position[0] == BED2:
                draw_image()
                hot_spots(LIVING, Point(240, 47), Point(298, 6), None, BATH2, Point(12, 48), Point(91, 23))

            elif position[0] == BATH2:
                draw_image()
                hot_spots(BED2, Point(15, 206), Point(81, 151))  # ,None, ???, Point(337, 218), Point(350, 116)

            elif position[0] == SAFE_ANIMATE:
                draw_image(0.05)
                hot_spots(END)

            # End frame
            elif position[0] == END:
                draw_image()
                win.getMouse()
                win.close()
                quit()
            else:
                print("ERROR: position is out of bounds @: ", position[0][0], " (i.e. has values that aren't being tested). Go fix it. Please.")
                win.getMouse()
                quit()

            # Think of this as a FPS counter, so your computer doesn't explode
            # time.sleep(0.01)
            # For debugging
            print(position)
            # Clear Image, might not be needed at all.
            clear_image()

########################################################################################################################
# 5. The stuff Evan made
########################################################################################################################
def textbox(line1="I like diamonds... meeow.", line2="Who's there!?"):
    # win = GraphWin("Introduction", 540, 420)
    # win.setCoords(0.0,0.0,540,420)

    #rectangle border:

    border1 = Rectangle(Point(45,45), Point(495,155))
    border1.draw(win)
    border1.setFill("White")
    border1.setOutline("Black")

    border2 = Rectangle(Point(50,50), Point(490,150))
    border2.draw(win)
    border2.setFill("Navy")
    border2.setOutline("Navy")

    #triangle in corner:
    #use for back-to-back text boxes (triangle1).
    #use to suggest action via mouseclick (triangle2).

    #triangle1 = Polygon(Point(450,80), Point(470,80), Point(460,70))
    #triangle1.draw(win)
    #triangle1.setFill("white")
    #triangle1.setOutline("white")
    #triangle1.move(5,-7.5)

    triangle2 = Polygon(Point(450,90), Point(460,80), Point(450,70))
    triangle2.draw(win)
    triangle2.setFill("white")
    triangle2.setOutline("white")
    triangle2.move(17,-7.5)

    #text:
    #change y-coordinates in increments of 23 for each new line

    name1 = Text(Point(135,135), "CAT BURGLAR:")
    name1.draw(win)
    name1.setFill("white")
    name1.setSize(20)
    name1.setFace("courier")
    #  name1.setStyle("bold")

    text1 = Text(Point(213,112), line1) #change x-coordinate to align
    text1.draw(win)
    text1.setFill("white")
    text1.setSize(20)
    text1.setFace("courier")
    #  text1.setStyle("bold")
    #  text1.setStyle("italic")
    #  text1.setStyle("bold italic")

    text2 = Text(Point(141,89), line2) #change x-coordinate to align
    text2.draw(win)
    text2.setFill("white")
    text2.setSize(20)
    text2.setFace("courier")
    #  text2.setStyle("bold")
    text2.setStyle("italic")
    #  text2.setStyle("bold italic")

    # For now this is going to undraw the thing
    win.getMouse()

    border1.undraw()
    border2.undraw()
    name1.undraw()
    triangle2.undraw()
    text1.undraw()
    text2.undraw()


def title(win):
    #night sky:
    bg = Rectangle(Point(-50,-50), Point(600,600))
    bg.draw(win)
    bg.setFill("black")

    moon = Circle(Point(420,320), 30)
    moon.draw(win)
    moon.setFill("PaleGoldenrod")

    moon1 = Circle(Point(430,325), 25)
    moon1.draw(win)
    moon1.setFill("black")

    star103 = Circle(Point(30,350), 1.5)
    star103.draw(win)
    star103.setFill("white")

    star102 = Circle(Point(65,310), 1)
    star102.draw(win)
    star102.setFill("white")

    star101 = Circle(Point(90,380), 2)
    star101.draw(win)
    star101.setFill("white")

    star10 = Circle(Point(145,340), 1)
    star10.draw(win)
    star10.setFill("white")

    star19 = Circle(Point(160,370), 1)
    star19.draw(win)
    star19.setFill("white")

    star18 = Circle(Point(250,380), 1.5)
    star18.draw(win)
    star18.setFill("white")

    star17 = Circle(Point(225,300), 1)
    star17.draw(win)
    star17.setFill("white")

    star16 = Circle(Point(300,350), 2)
    star16.draw(win)
    star16.setFill("white")

    star15 = Circle(Point(350,350), 1)
    star15.draw(win)
    star15.setFill("white")

    star14 = Circle(Point(365,320), 1)
    star14.draw(win)
    star14.setFill("white")

    star13 = Circle(Point(450,380), 1)
    star13.draw(win)
    star13.setFill("white")

    star12 = Circle(Point(465,310), 1)
    star12.draw(win)
    star12.setFill("white")

    star11 = Circle(Point(500,390), 2)
    star11.draw(win)
    star11.setFill("white")

    #back row of clouds:

    bg4 = Rectangle(Point(-50,-50), Point(600,150))
    bg4.draw(win)
    bg4.setFill("SteelBlue4")
    bg4.setOutline("SteelBlue4")

    c407 = Circle(Point(-25,150), 50)
    c407.draw(win)
    c407.setFill("SteelBlue4")
    c407.setOutline("SteelBlue4")

    c406 = Circle(Point(35,120), 50)
    c406.draw(win)
    c406.setFill("SteelBlue4")
    c406.setOutline("SteelBlue4")

    c405 = Circle(Point(100,130), 40)
    c405.draw(win)
    c405.setFill("SteelBlue4")
    c405.setOutline("SteelBlue4")

    c400 = Circle(Point(158,125), 45)
    c400.draw(win)
    c400.setFill("SteelBlue4")
    c400.setOutline("SteelBlue4")

    c404 = Circle(Point(202,150), 20)
    c404.draw(win)
    c404.setFill("SteelBlue4")
    c404.setOutline("SteelBlue4")

    c403 = Circle(Point(220,175), 15)
    c403.draw(win)
    c403.setFill("SteelBlue4")
    c403.setOutline("SteelBlue4")

    c402 = Circle(Point(230,190), 8)
    c402.draw(win)
    c402.setFill("SteelBlue4")
    c402.setOutline("SteelBlue4")

    c401 = Circle(Point(251,200), 18)
    c401.draw(win)
    c401.setFill("SteelBlue4")
    c401.setOutline("SteelBlue4")

    c40 = Circle(Point(260,153), 40)
    c40.draw(win)
    c40.setFill("SteelBlue4")
    c40.setOutline("SteelBlue4")

    c49 = Circle(Point(275,192), 10)
    c49.draw(win)
    c49.setFill("SteelBlue4")
    c49.setOutline("SteelBlue4")

    c48 = Circle(Point(288,180), 12)
    c48.draw(win)
    c48.setFill("SteelBlue4")
    c48.setOutline("SteelBlue4")

    c47 = Circle(Point(310,150), 30)
    c47.draw(win)
    c47.setFill("SteelBlue4")
    c47.setOutline("SteelBlue4")

    c46 = Circle(Point(350,125), 50)
    c46.draw(win)
    c46.setFill("SteelBlue4")
    c46.setOutline("SteelBlue4")

    c45 = Circle(Point(400,130), 35)
    c45.draw(win)
    c45.setFill("SteelBlue4")
    c45.setOutline("SteelBlue4")

    c44 = Circle(Point(450,130), 45)
    c44.draw(win)
    c44.setFill("SteelBlue4")
    c44.setOutline("SteelBlue4")

    c43 = Circle(Point(475,168), 8)
    c43.draw(win)
    c43.setFill("SteelBlue4")
    c43.setOutline("SteelBlue4")

    c42 = Circle(Point(510,145), 40)
    c42.draw(win)
    c42.setFill("SteelBlue4")
    c42.setOutline("SteelBlue4")

    c41 = Circle(Point(540,165), 15)
    c41.draw(win)
    c41.setFill("SteelBlue4")
    c41.setOutline("SteelBlue4")

    #second row of clouds (from back):

    bg3 = Rectangle(Point(-50,-50), Point(600,100))
    bg3.draw(win)
    bg3.setFill("LightSkyBlue4")
    bg3.setOutline("LightSkyBlue4")

    c38 = Circle(Point(35,120), 60)
    c38.draw(win)
    c38.setFill("LightSkyBlue4")
    c38.setOutline("LightSkyBlue4")

    c37 = Circle(Point(105,110), 40)
    c37.draw(win)
    c37.setFill("LightSkyBlue4")
    c37.setOutline("LightSkyBlue4")

    c36 = Circle(Point(145,127), 15)
    c36.draw(win)
    c36.setFill("LightSkyBlue4")
    c36.setOutline("LightSkyBlue4")

    c35 = Circle(Point(200,100), 55)
    c35.draw(win)
    c35.setFill("LightSkyBlue4")
    c35.setOutline("LightSkyBlue4")

    c300 = Circle(Point(280,105), 60)
    c300.draw(win)
    c300.setFill("LightSkyBlue4")
    c300.setOutline("LightSkyBlue4")

    c34 = Circle(Point(280,105), 60)
    c34.draw(win)
    c34.setFill("LightSkyBlue4")
    c34.setOutline("LightSkyBlue4")

    c33 = Circle(Point(370,95), 60)
    c33.draw(win)
    c33.setFill("LightSkyBlue4")
    c33.setOutline("LightSkyBlue4")

    c32 = Circle(Point(370,95), 60)
    c32.draw(win)
    c32.setFill("LightSkyBlue4")
    c32.setOutline("LightSkyBlue4")

    c31 = Circle(Point(470,105), 60)
    c31.draw(win)
    c31.setFill("LightSkyBlue4")
    c31.setOutline("LightSkyBlue4")

    #third row of clouds (from back):

    bg2 = Rectangle(Point(-50,-50), Point(600,75))
    bg2.draw(win)
    bg2.setFill("LightSkyBlue3")
    bg2.setOutline("LightSkyBlue3")

    c27 = Circle(Point(-10,70), 80)
    c27.draw(win)
    c27.setFill("LightSkyBlue3")
    c27.setOutline("LightSkyBlue3")

    c26 = Circle(Point(120,50), 80)
    c26.draw(win)
    c26.setFill("LightSkyBlue3")
    c26.setOutline("LightSkyBlue3")

    c25 = Circle(Point(250,60), 70)
    c25.draw(win)
    c25.setFill("LightSkyBlue3")
    c25.setOutline("LightSkyBlue3")

    c24 = Circle(Point(400,70), 75)
    c24.draw(win)
    c24.setFill("LightSkyBlue3")
    c24.setOutline("LightSkyBlue3")

    c23 = Circle(Point(520,80), 85)
    c23.draw(win)
    c23.setFill("LightSkyBlue3")
    c23.setOutline("LightSkyBlue3")

    c22 = Circle(Point(190,90), 25)
    c22.draw(win)
    c22.setFill("LightSkyBlue3")
    c22.setOutline("LightSkyBlue3")

    c21 = Circle(Point(325,80), 40)
    c21.draw(win)
    c21.setFill("LightSkyBlue3")
    c21.setOutline("LightSkyBlue3")

    #front row of clouds:

    c18 = Circle(Point(0,20), 80)
    c18.draw(win)
    c18.setFill("LightSkyBlue")
    c18.setOutline("LightSkyBlue")

    c17 = Circle(Point(150,10), 80)
    c17.draw(win)
    c17.setFill("LightSkyBlue")
    c17.setOutline("LightSkyBlue")

    c16 = Circle(Point(260,7), 70)
    c16.draw(win)
    c16.setFill("LightSkyBlue")
    c16.setOutline("LightSkyBlue")

    c15 = Circle(Point(400,20), 75)
    c15.draw(win)
    c15.setFill("LightSkyBlue")
    c15.setOutline("LightSkyBlue")

    c14 = Circle(Point(550,30), 85)
    c14.draw(win)
    c14.setFill("LightSkyBlue")
    c14.setOutline("LightSkyBlue")

    c13 = Circle(Point(75,50), 20)
    c13.draw(win)
    c13.setFill("LightSkyBlue")
    c13.setOutline("LightSkyBlue")

    c12 = Circle(Point(325,45), 20)
    c12.draw(win)
    c12.setFill("LightSkyBlue")
    c12.setOutline("LightSkyBlue")

    c11 = Circle(Point(470,45), 40)
    c11.draw(win)
    c11.setFill("LightSkyBlue")
    c11.setOutline("LightSkyBlue")

#text:

    title1 = Text(Point(270,290), "Cat Burglar")
    title1.draw(win)
    title1.setFill("white")
    title1.setSize(35)
    title1.setFace("courier")
    title1.setStyle("bold")

    title2 = Text(Point(270,247), "The Heist")
    title2.draw(win)
    title2.setFill("white")
    title2.setSize(27)
    title2.setFace("courier")

    underline = Line(Point(155,268), Point(385,268))
    underline.draw(win)
    underline.setFill("white")
    underline.setWidth(1.5)

    title3 = Text(Point(270,155), "Click anywhere to begin")
    title3.draw(win)
    title3.setFill("white")
    title3.setSize(16)
    title3.setFace("courier")

    title4 = Text(Point(270,40), "2015CSC2301")
    title4.draw(win)
    title4.setFill("white")
    title4.setSize(15)
    title4.setFace("courier")
    title4.setStyle("bold")

    win.getMouse()

    # undraw screen

    c11.undraw()
    c12.undraw()
    c13.undraw()
    c14.undraw()
    c15.undraw()
    c16.undraw()
    c17.undraw()
    c18.undraw()

    c21.undraw()
    c22.undraw()
    c23.undraw()
    c24.undraw()
    c25.undraw()
    c26.undraw()
    c27.undraw()

    c300.undraw()
    c31.undraw()
    c32.undraw()
    c33.undraw()
    c34.undraw()
    c35.undraw()
    c36.undraw()
    c37.undraw()
    c38.undraw()

    c400.undraw()
    c41.undraw()
    c42.undraw()
    c43.undraw()
    c44.undraw()
    c45.undraw()
    c46.undraw()
    c47.undraw()
    c48.undraw()
    c49.undraw()
    c40.undraw()
    c401.undraw()
    c402.undraw()
    c403.undraw()
    c404.undraw()
    c405.undraw()
    c406.undraw()
    c407.undraw()

    star11.undraw()
    star12.undraw()
    star13.undraw()
    star14.undraw()
    star15.undraw()
    star16.undraw()
    star17.undraw()
    star18.undraw()
    star19.undraw()
    star10.undraw()
    star101.undraw()
    star102.undraw()
    star103.undraw()

    moon.undraw()
    moon1.undraw()

    bg.undraw()
    bg2.undraw()
    bg3.undraw()
    bg4.undraw()

    title1.undraw()
    title2.undraw()
    title3.undraw()
    title4.undraw()

    underline.undraw()


##############################################################
# CALL MAIN HERE AT THE BOTTOM!
##############################################################
main()