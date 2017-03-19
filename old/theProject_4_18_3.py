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

START = [0, CENTER, 'Letter_Intro.gif']

BED1 = [1, CENTER, '1_Bed1_Full.gif']
BED1L = [1.1, CENTER, '1_Bed1_Full.gif', BLANK, "SAY:Door won't open||It's locked."]
BED1S = [1.2, CENTER, '1_Bed1_Full.gif', BLANK, "SAY:Alright, meow I'm in!!!||            (click around to explore)"]
# Bed mattress, Shawl, Painting
BED1M = [1.3, CENTER, '1_Bed1_Full.gif', BLANK, "SAY:"]
BED1P = [1.4, CENTER, '1_Bed1_Full.gif', BLANK, "SAY:"]
BED1H = [1.5, CENTER, '1_Bed1_Full.gif', BLANK, "SAY:"]

BATH1 = [2, CENTER, '2_Bath1_Full.gif']
BATH1C = [2.1, CENTER, 'Bathroom1_CU.gif']
BATH1E = [2.2, CENTER, '3_Bath1_Empty.gif']
# Bath1 glasses on the left, candles, one for empty, one for full
BATH1GF = [2.31, CENTER, '2_Bath1_Full.gif', BLANK, "SAY:"]
BATH1GE = [2.32, CENTER, '3_Bath1_Empty.gif', BLANK, "SAY:"]
BATH1CF = [2.41, CENTER, '2_Bath1_Full.gif', BLANK, "SAY:"]
BATH1CE = [2.42, CENTER, '3_Bath1_Empty.gif', BLANK, "SAY:"]

HALL1 = [3, CENTER, '4_Hall1_Full.gif']
HALL1_L = [3.1, CENTER, '4_Hall1_Full.gif', BLANK, "SAY:"]
# Hall1 PaintingL and PaintingR
HALL1PL = [3.2, CENTER, '4_Hall1_Full.gif', BLANK, "SAY:"]
HALL1PR = [3.3, CENTER, '4_Hall1_Full.gif', BLANK, "SAY:"]

STUDY1 = [4, CENTER, '5_Study1_Half.gif']
STUDY1O = [4.1, CENTER, '6_Study1_Full.gif']
# STUDY Couch, Book Left (three rows), Book Right (three rows)
STUDY1C = [4.2, CENTER, '5_Study1_Half.gif', BLANK, "SAY:"]
STUDY1CO = [4.21, CENTER, '6_Study1_Full.gif', BLANK, "SAY:"]
STUDY1BL = [4.3, CENTER, '5_Study1_Half.gif', BLANK, "SAY:"]
STUDY1BLO = [4.31, CENTER, '6_Study1_Full.gif', BLANK, "SAY:"]
STUDY1BR = [4.4, CENTER, '5_Study1_Half.gif', BLANK, "SAY:"]
STUDY1BRO = [4.41, CENTER, '6_Study1_Full.gif', BLANK, "SAY:"]

STUDY2 = [5, CENTER, '7_Study2_Full.gif']
STUDY2E = [5.1, CENTER, '8_Study2_Empty.gif']
STUDY2C = [5.2, CENTER, 'Letter_Hint3.gif']
# Study2 flowers with picture, both chandliers, both horses, pen and the base that holds the base, Lamp
STUDY2FF = [5.3, CENTER, '7_Study2_Full.gif', BLANK, "SAY:"]
STUDY2FE = [5.31, CENTER, '8_Study2_Empty.gif', BLANK, "SAY:"]
STUDY2CLF = [5.4, CENTER, '7_Study2_Full.gif', BLANK, "SAY:"]
STUDY2CLE = [5.41, CENTER, '8_Study2_Empty.gif', BLANK, "SAY:"]
STUDY2CRF = [5.5, CENTER, '7_Study2_Full.gif', BLANK, "SAY:"]
STUDY2CRE = [5.51, CENTER, '8_Study2_Empty.gif', BLANK, "SAY:"]
STUDY2HLF = [5.6, CENTER, '7_Study2_Full.gif', BLANK, "SAY:"]
STUDY2HLE = [5.61, CENTER, '8_Study2_Empty.gif', BLANK, "SAY:"]
STUDY2HRF = [5.7, CENTER, '7_Study2_Full.gif', BLANK, "SAY:"]
STUDY2HRE = [5.71, CENTER, '8_Study2_Empty.gif', BLANK, "SAY:"]
STUDY2PF = [5.8, CENTER, '7_Study2_Full.gif', BLANK, "SAY:"]
STUDY2PE = [5.81, CENTER, '8_Study2_Empty.gif', BLANK, "SAY:"]
STUDY2LF = [5.9, CENTER, '7_Study2_Full.gif', BLANK, "SAY:"]
STUDY2LE = [5.91, CENTER, '8_Study2_Empty.gif', BLANK, "SAY:"]

STAIRS = [6, CENTER, '9_Hall2_Full.gif']
# Stairs, entire desk and mirror
STAIRSM = [6.1, CENTER, '9_Hall2_Full.gif', BLANK, "SAY:"]

SAFEROOM = [7, CENTER, '14_Safe_Full.gif']
# Saferoom, face in the mirror, the glass
SAFEROOMF = [7.1, CENTER, '14_Safe_Full.gif', BLANK, "SAY:"]
SAFEROOMG = [7.2, CENTER, '14_Safe_Full.gif', BLANK, "SAY:"]

LIVING = [8, CENTER, '10_Living_Full_Note.gif']
LIVINGC = [8.1, CENTER, 'Letter_Hint5.gif']
LIVINGE = [8.2, CENTER, '10_Living_Full.gif']
LIVINGUV = [8.3, CENTER, '10_Living_Full_UV.gif']
LIVINGUVE = [8.31, CENTER, '10_Living_Full_UV.gif']
# Living mirror where the five will be and both lamps (l lamp will be double click if user has lightbulb)
LIVINGMF = [8.4, CENTER, '10_Living_Full_Note.gif', BLANK, "SAY:"]
LIVINGME = [8.41, CENTER, '10_Living_Full.gif', BLANK, "SAY:"]
LIVINGLLF1 = [8.5, CENTER, '10_Living_Full_Note.gif', BLANK, "SAY:"]
LIVINGLLE1 = [8.51, CENTER, '10_Living_Full.gif', BLANK, "SAY:"]
LIVINGLLF2 = [8.52, CENTER, '10_Living_Full_Note.gif', BLANK, "SAY:"]
LIVINGLLE2 = [8.53, CENTER, '10_Living_Full.gif', BLANK, "SAY:"]
LIVINGLLF3 = [8.52, CENTER, '10_Living_Full_Note.gif', BLANK, "SAY:"]
LIVINGLLE3 = [8.53, CENTER, '10_Living_Full.gif', BLANK, "SAY:"]
LIVINGLRF = [8.6, CENTER, '10_Living_Full_Note.gif', BLANK, "SAY:"]
LIVINGLRE = [8.7, CENTER, '10_Living_Full.gif', BLANK, "SAY:"]
LIVINGCF = [8.6, CENTER, '10_Living_Full_Note.gif', BLANK, "SAY:"]
LIVINGCE = [8.7, CENTER, '10_Living_Full.gif', BLANK, "SAY:"]

BED2 = [9, CENTER, '11_Bed2_Full.gif']
BED2D = [9.4, CENTER]
# Bed, PillowNShoes, Couch (top part)
BED2B = [9.1, CENTER, '11_Bed2_Full.gif', BLANK, "SAY:"]
BED2P = [9.2, CENTER, '11_Bed2_Full.gif', BLANK, "SAY:"]
BED2CT = [9.3, CENTER, '11_Bed2_Full.gif', BLANK, "SAY:"]

BATH2 = [10, CENTER, '12_Bath2_Full.gif']

SAFE_COMBO = [15, BLANK, 'END']

# Safe Animation
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
# 0 - Key
# 1 - Note in study 2
# 3 - Note in Livingroom
# 4 - Lightbulb
# 5 - already clicked on the lamp one time with lightbulb in hand
# 6 - another note
inventory = ['no', 'no', 'no', 'no', 'no', 'no']  # etc. add on if needed

# The initial accumulation of data onto the list.
position.append(START)        # Bind to position[0], so it will be numeric position of the player. how fancy.
position.append(inventory)    # Keep track of the Items, that's kind of Important.
position.append([])           # A placeholder for frames to be manipulated while passing through functions

for j in range(61):           # if you're gonna need more than 61 sub frames, this needs to be changed.
    position[2].append(j)
j = None

########################################################################################################################
# 3. Functions, hopefully you won't actually need to look at these.
########################################################################################################################
def check():  # [Checks to see if window is closed, helps keep un-needed errors down]
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


def hot_spots(goto1, point1=None, point2=None, stuff1=None, goto2=None, point3=Point(0, 0), point4=Point(0, 0), stuff2=None, goto3=None, point5=Point(0, 0), point6=Point(0, 0), stuff3=None, goto4=None, point7=Point(0, 0), point8=Point(0, 0), stuff4=None, goto5=None, point9=Point(0, 0), point0=Point(0, 0), stuff5=None, goto6=None, point10=Point(0, 0), point11=Point(0, 0), stuff6=None, goto7=None, point12=Point(0, 0), point13=Point(0, 0), stuff7=None, goto8=None, point14=Point(0, 0), point15=Point(0, 0), stuff8=None, goto9=None, point16=Point(0, 0), point17=Point(0, 0), stuff9=None, goto10=None, point18=Point(0, 0), point19=Point(0, 0), stuff10=None):
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
            if goto6:
                done = actually_check(temp, goto6, point10, point11, stuff6)
                if done:
                    return 6
            if goto7:
                done = actually_check(temp, goto7, point12, point13, stuff7)
                if done:
                    return 7
            if goto8:
                done = actually_check(temp, goto8, point14, point15, stuff8)
                if done:
                    return 8
            if goto9:
                done = actually_check(temp, goto9, point16, point17, stuff9)
                if done:
                    return 9
            if goto10:
                done = actually_check(temp, goto10, point18, point19, stuff10)
                if done:
                    return 10
        # cannot use pollMouse without rigged graphics library.
        # temp = win.pollMouse()
        # print(temp.getX(), temp.getY())


def thou_shall_be_circles(num, color):
    # Circle(centerPoint, radius) Constructs a circle with given center point and radius.
    if num == 1:  # this is the left circle
        temp = Circle(Point(143, 259), 5)
        temp.setFill(color)
    if num == 2:  # this is the middle circle
        temp = Circle(Point(177.5, 259), 5)
        temp.setFill(color)
    if num == 3:  # this is the right circle
        temp = Circle(Point(212, 259), 5)
        temp.setFill(color)
    return temp

def draw_image(wait=0):
    for i in range(1, (int((len(position[0]) - 1) / 2)) + 1):  # Gets how many images need to be displayed
        # if position[0][i * 2][-4:-3] == '.' or position[0][i * 2][-5:-4] == '.':  # if the image is an image
        # I thought the textbox was an Image, obviously you coded it, no worries, here's how its handled
        if position[0][i * 2][0:3] == 'SAY':
            # print(position[0][i * 2], " was treated as a text box call")
            giggle = position[0][i * 2][4:]
            # In case there is not a text phrase, this if handles it
            if len(giggle) > 1:
                temp1, temp2 = giggle.split("||")
            else:
                temp1, temp2 = None, None
            textbox(temp1, temp2)
        elif position[0][i * 2][0:3] == "END":
            combo()
            # for r in range(1, ((int(position[0][i * 2][0])) + 1)):
            #     position[2][i] = thou_shall_be_circles(r, "red")
            #     position[2][i].draw(win)
        # elif position[0][i * 2][1:6] == "GREEN":
        #     for g in range(1, ((int(position[0][i * 2][0])) + 1)):
        #         position[2][i] = thou_shall_be_circles(g, "green")
        #         position[2][i].draw(win)
        else:
            # print(position[0][i * 2], " was treated as an image.")
            position[2][i] = Image(position[0][(i * 2) - 1], position[0][i * 2])
            position[2][i].draw(win)
            time.sleep(wait)

def clear_image():
    # for loop points to correct frame, then undraws if its a graphics object
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
            # Draw Intro
            if position[0] == START:
                draw_image()
                hot_spots(BED1S, Point(0, 420), Point(540, 0))

            # Bed1 text boxes
            elif position[0] == BED1S or position[0] == BED1M or position[0] == BED1P or position[0] == BED1H or position[0] == BED1L:
                draw_image()
                hot_spots(BED1)

            # Bed1
            elif position[0] == BED1 and position[1][0] == 'no':
                draw_image()
                hot_spots(BATH1, Point(411, 285), Point(463, 156), None, BED1L, Point(160, 284), Point(187, 192), None, BED1M, Point(192, 202), Point(339, 137), None, BED1H, Point(334, 114), Point(454, 0), None, BED1P, Point(0, 286), Point(102, 187))

            #  Bed1, when user has key
            elif position[0] == BED1 and position[1][0] == 'yes':
                draw_image()
                hot_spots(BATH1, Point(411, 285), Point(463, 156), None, HALL1, Point(160, 284), Point(187, 192), None, BED1M, Point(192, 202), Point(339, 137), None, BED1H, Point(334, 114), Point(454, 0), None, BED1P, Point(0, 286), Point(102, 187))

            # Bath1, without key
            elif position[0] == BATH1 and position[1][0] == 'no':
                draw_image()
                hot_spots(BATH1C, Point(405, 76), Point(441, 46), 0, BED1, Point(247, 62), Point(290, 9), None, BATH1GF, Point(23, 129), Point(126, 53), None, BATH1CF, Point(215, 279), Point(329, 228))

            # When back at bath but already have key
            elif position[0] == BATH1 and position[1][0] == 'yes':
                # if the key is already taken, we're gonna pull a switcher roo, and display the bath w/o key
                position[0] = BATH1E
                draw_image()
                hot_spots(BED1, Point(247, 62), Point(290, 9), None, BATH1GE, Point(23, 129), Point(126, 53), None, BATH1CE, Point(215, 279), Point(329, 228))

            # the close up of the key
            elif position[0] == BATH1C:
                draw_image()
                hot_spots(BATH1, Point(0, 420), Point(540, 0), 0)

            # Bath1 text boxes (empty)
            elif position[0] == BATH1CE or position[0] == BATH1GE or position[0] == BATH1CF or position[0] == BATH1GF:
                draw_image()
                hot_spots(BATH1)

            # # Bath1 text boxes (with key in there)
            # elif position[0] == BATH1CF or position[0] == BATH1GF:
            #     draw_image()
            #     hot_spots(BATH1)

            # Hall1 with the note in hand
            elif position[0] == HALL1 and position[1][1] == 'yes':
                draw_image()
                hot_spots(BED1, Point(0, 105), Point(83, 44), None, STUDY1, Point(408, 279), Point(540, 0), None, STAIRS, Point(168, 253), Point(216, 114), None, HALL1PL, Point(73, 218), Point(147, 154), None, HALL1PR, Point(364, 224), Point(382, 160))

            # First encounter with the Hall
            elif position[0] == HALL1 and position[1][1] == 'no':
                draw_image()
                hot_spots(BED1, Point(0, 105), Point(93, 44), None, STUDY1, Point(408, 279), Point(540, 0), None, HALL1_L, Point(168, 253), Point(216, 114), None, HALL1PL, Point(73, 218), Point(147, 154), None, HALL1PR, Point(364, 224), Point(382, 160))

            # Text boxes for hall one
            elif position[0] == HALL1_L or position[0] == HALL1PL or position[0] == HALL1PR:
                draw_image()
                hot_spots(HALL1)

            # Study 1
            elif position[0] == STUDY1:
                draw_image()
                hot_spots(HALL1, Point(232, 52), Point(307, 7), None, STUDY1O, Point(258, 290), Point(277, 251), None, STUDY1C, Point(74, 207), Point(431, 104), None, STUDY1BL, Point(149, 332), Point(250, 213), None, STUDY1BR, Point(363, 326), Point(458, 208))

            # Study open , after clicked on the books
            elif position[0] == STUDY1O:
                draw_image()
                hot_spots(HALL1, Point(232, 52), Point(307, 7), None, STUDY2, Point(0, 420), Point(67, 118), None, STUDY1CO, Point(74, 207), Point(431, 104), None, STUDY1BLO, Point(149, 332), Point(250, 213), None, STUDY1BRO, Point(363, 326), Point(458, 208))

            # Text boxes for the study1
            elif position[0] == STUDY1C or position[0] == STUDY1BR or position[0] == STUDY1BL:
                draw_image()
                hot_spots(STUDY1)

            # Text boxes for the study1 with open bookcase
            elif position[0] == STUDY1CO or position[0] == STUDY1BRO or position[0] == STUDY1BLO:
                draw_image()
                hot_spots(STUDY1O)

            # Display normal, there's a check on inventory because of the next if statement
            elif position[0] == STUDY2 and position[1][1] == "no":
                draw_image()
                hot_spots(STUDY1O, Point(247, 62), Point(290, 9), None, STUDY2C, Point(327, 87), Point(386, 45), 1, STUDY2FF, Point(78, 172), Point(156, 83), None, STUDY2PF, Point(207, 158), Point(311, 78), None, STUDY2LF, Point(374, 232), Point(452, 90), None, STUDY2CLF, Point(28, 420), Point(148, 304), None, STUDY2CRF, Point(383, 420), Point(492, 305), None, STUDY2HLF, Point(112, 281), Point(159, 251), None, STUDY2HRF, Point(366, 276), Point(404, 251))

            elif position[0] == STUDY2C:
                draw_image()
                hot_spots(STUDY2, Point(0, 420), Point(540, 0))

            # if already have note, switcheroo
            elif position[0] == STUDY2 and position[1][1] == "yes":
                position[0] = STUDY2E  # see above
                draw_image()
                hot_spots(STUDY1O, Point(247, 62), Point(290, 9), None, STUDY2FE, Point(78, 172), Point(156, 83), None, STUDY2PE, Point(207, 158), Point(311, 78), None, STUDY2LE, Point(374, 232), Point(452, 90), None, STUDY2CLE, Point(28, 420), Point(148, 304), None, STUDY2CRE, Point(383, 420), Point(492, 305), None, STUDY2HLE, Point(112, 281), Point(159, 251), None, STUDY2HRE, Point(366, 276), Point(404, 251))

            # Text boxes for study2 with the note in it
            elif position[0] == STUDY2FF or position[0] == STUDY2PF or position[0] == STUDY2LF or position[0] == STUDY2CLF or position[0] == STUDY2CRF or position[0] == STUDY2HLF or position[0] == STUDY2HRF or position[0] == STUDY2FE or position[0] == STUDY2PE or position[0] == STUDY2LE or position[0] == STUDY2CLE or position[0] == STUDY2CRE or position[0] == STUDY2HLE or position[0] == STUDY2HRE:
                draw_image()
                hot_spots(STUDY2)

            # Text boxes for study2 without the note
            # elif position[0] == STUDY2FE or position[0] == STUDY2PE or position[0] == STUDY2LE or position[0] == STUDY2CLE or position[0] == STUDY2CRE or position[0] == STUDY2HLE or position[0] == STUDY2HRE:
            #     draw_image()
            #     hot_spots(STUDY2)

            # Stairs shot,
            elif position[0] == STAIRS:
                draw_image()
                hot_spots(SAFEROOM, Point(229, 203), Point(330, 102), None, HALL1, Point(0, 50), Point(50, 0), None, LIVING, Point(171, 237), Point(187, 100), None, HALL1, Point(0, 172), Point(118, 0), None, HALL1, Point(0, 420), Point(55, 177), None, HALL1, Point(55, 420), Point(55, 177), None, HALL1, Point(55, 420), Point(118, 280), None, STAIRSM, Point(432, 325), Point(510, 118))

            # Stairs text box
            elif position[0] == STAIRSM:
                draw_image()
                hot_spots(STAIRS)

            # Saferoom, todo: fix so that the user cannot directly open the safe (duh)
            elif position[0] == SAFEROOM:
                draw_image()
                hot_spots(SAFE_COMBO, Point(182, 420), Point(350, 300), None, STAIRS, Point(463, 36), Point(530, 4), None, SAFEROOMF, Point(243, 255), Point(283, 221), None, SAFEROOMG, Point(185, 160), Point(343, 31))

            # Saferoom text boxes
            elif position[0] == SAFEROOMF or position[0] == SAFEROOMG:
                draw_image()
                hot_spots(SAFEROOM)

            ###########################################
            # GG..... [good god]
            ###########################################
            # living room,
            # if at living, and does not have the note, and does not have the lightbulb
            elif position[0] == LIVING and position[1][3] == "no" and position[1][4] == "no":
                draw_image()
                hot_spots(STAIRS, Point(253, 31), Point(301, 4), None, BED2, Point(426, 219), Point(456, 144), None, LIVINGC, Point(297, 97), Point(331, 73), 3, LIVINGMF, Point(241, 266), Point(314, 172), None, LIVINGCF, Point(206, 139), Point(343, 107), None, LIVINGLLF1, Point(0, 190), Point(80, 131), None, LIVINGLRF, Point(475, 189), Point(540, 133), None, LIVINGCF, Point(0, 187), Point(136, 135))

            # if at living, and does have the note, and does not have the lightbulb
            elif position[0] == LIVING and position[1][3] == "yes" and position[1][4] == "no":
                draw_image()
                hot_spots(STAIRS, Point(253, 31), Point(301, 4), None, BED2, Point(426, 219), Point(456, 144), None, LIVINGME, Point(241, 266), Point(314, 172), None, LIVINGCE, Point(206, 139), Point(343, 107), None, LIVINGLLE1, Point(0, 190), Point(80, 131), None, LIVINGLRE, Point(475, 189), Point(540, 133), None, LIVINGCE, Point(0, 187), Point(136, 135))

            # if at living, and have the note, and does have the lightbulb, but has not clicked on the lamp yet
            elif position[0] == LIVING and position[1][3] == "yes" and position[1][4] == "yes" and position[1][5] == "no":
                draw_image()
                hot_spots(STAIRS, Point(253, 31), Point(301, 4), None, BED2, Point(426, 219), Point(456, 144), None, LIVINGME, Point(241, 266), Point(314, 172), None, LIVINGCE, Point(206, 139), Point(343, 107), None, LIVINGLLE2, Point(0, 190), Point(80, 131), 5, LIVINGLRE, Point(475, 189), Point(540, 133), None, LIVINGCE, Point(0, 187), Point(136, 135))

            # if at living, and has the note and the lightbulb, and has clicked on the lamp a first time already
            elif position[0] == LIVING and position[1][3] == "yes" and position[1][4] == "yes" and position[1][5] == "yes":
                draw_image()
                hot_spots(STAIRS, Point(253, 31), Point(301, 4), None, BED2, Point(426, 219), Point(456, 144), None, LIVINGME, Point(241, 266), Point(314, 172), None, LIVINGCE, Point(206, 139), Point(343, 107), None, LIVINGLLE3, Point(0, 190), Point(80, 131), None, LIVINGLRE, Point(475, 189), Point(540, 133), None, LIVINGCE, Point(0, 187), Point(136, 135))

            # if at living and does not have the note, but does have the lightbulb
            elif position[0] == LIVING and position[1][3] == "no" and position[1][4] == "yes":
                draw_image()
                hot_spots(STAIRS, Point(253, 31), Point(301, 4), None, BED2, Point(426, 219), Point(456, 144), None, LIVINGC, Point(297, 97), Point(331, 73), 3, LIVINGMF, Point(241, 266), Point(314, 172), None, LIVINGCF, Point(206, 139), Point(343, 107), None, LIVINGLLF2, Point(0, 190), Point(80, 131), 5, LIVINGLRF, Point(475, 189), Point(540, 133), None, LIVINGCF, Point(0, 187), Point(136, 135))

            # close up on the note/letter
            elif position[0] == LIVINGC:
                draw_image()
                hot_spots(LIVING, Point(0, 420), Point(520, 0))

            # If user has clicked on the lamp that final time
            elif position[0] == LIVINGLLE3 or position[0] == LIVINGLLF3:
                draw_image()
                hot_spots(LIVINGUV)

            # If user has not gotten the note todo: get a new image
            elif position[0] == LIVINGUV and position[1][3] == "no":
                position[0] = LIVINGUVE
                draw_image()
                hot_spots(STAIRS, Point(253, 31), Point(301, 4), None, BED2, Point(426, 219), Point(456, 144), None, LIVINGC, Point(297, 97), Point(331, 73), 3, LIVINGMF, Point(241, 266), Point(314, 172), None, LIVINGCF, Point(206, 139), Point(343, 107), None, LIVINGLRF, Point(475, 189), Point(540, 133), None, LIVINGCF, Point(0, 187), Point(136, 135))

            # If user has the note
            elif position[0] == LIVINGUV and position[1][3] == "yes":
                draw_image()
                hot_spots(STAIRS, Point(253, 31), Point(301, 4), None, BED2, Point(426, 219), Point(456, 144), None, LIVINGME, Point(241, 266), Point(314, 172), None, LIVINGCE, Point(206, 139), Point(343, 107), None, LIVINGLRE, Point(475, 189), Point(540, 133), None, LIVINGCE, Point(0, 187), Point(136, 135))

            elif position[0] == LIVINGMF or position[0] == LIVINGME or position[0] == LIVINGLLF1 or position[0] == LIVINGLLE1 or position[0] == LIVINGLLF2 or position[0] == LIVINGLLE2 or position[0] == LIVINGLRF or position[0] == LIVINGLRE or position[0] == LIVINGCF or position[0] == LIVINGCE:
                draw_image()
                hot_spots(LIVING)

            # # living room without the note
            # elif position[0] == LIVING and position[1][3] == "yes":
            #     position[0] = LIVINGE
            #     draw_image()
            #     hot_spots(STAIRS, Point(253, 31), Point(301, 4), None, BED2, Point(426, 219), Point(456, 144), None, LIVINGME, Point(241, 266), Point(314, 172), None, LIVINGCE, Point(206, 139), Point(343, 107), None, LIVINGLLE, Point(0, 190), Point(80, 131), None, LIVINGLRE, Point(475, 189), Point(540, 133), None, LIVINGCE, Point(0, 187), Point(136, 135))

            # Living room text boxes
            # elif position[0] == LIVINGMF or position[0] == LIVINGLLF or position[0] == LIVINGLRF or position[0] == LIVINGCF or position[0] == LIVINGME or position[0] == LIVINGLLE or position[0] == LIVINGLRE or position[0] == LIVINGCE:
            #     draw_image()
            #     hot_spots(LIVING)

            # Bedroom2, without having the lighbulb
            elif position[0] == BED2 and position[1][4] == "no":
                draw_image()
                hot_spots(LIVING, Point(240, 47), Point(298, 6), None, BATH2, Point(12, 48), Point(91, 23), None, BED2P, Point(311, 84), Point(388, 49), None, BED2D, Point(478, 135), Point(506, 81), 4, BED2B, Point(337, 161), Point(470, 100), None, BED2CT, Point(0, 187), Point(136, 135))

            elif position[0] == BED2 and position[1][4] == "yes":
                draw_image()
                hot_spots(LIVING, Point(240, 47), Point(298, 6), None, BATH2, Point(12, 48), Point(91, 23), None, BED2P, Point(311, 84), Point(388, 49), None, BED2B, Point(337, 161), Point(470, 100), None, BED2CT, Point(0, 187), Point(136, 135))

            # Bedroom2 text boxes
            elif position[0] == BED2CT or position[0] == BED2B or position[0] == BED2P:
                draw_image()
                hot_spots(BED2)

            elif position[0] == BED2D:
                draw_image()
                hot_spots(BED2, Point(0, 420), Point(540, 0))

            # Bathroom2 todo: stuff, stuff needs to be done.
            elif position[0] == BATH2:
                draw_image()
                hot_spots(BED2, Point(15, 206), Point(81, 151))  # ,None, ???, Point(337, 218), Point(350, 116)

            # This triggers the safe combo todo: make a back button for giggles and stuff
            elif position[0] == SAFE_COMBO:
                draw_image()
                hot_spots(SAFE_ANIMATE)

            # Animates the safe opening, point of no return
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
                print("ERROR: position is out of bounds @: ", position[0][0])
                print(" (i.e. has values that aren't being tested).")
                print("Please dispatch a team of highly trained monkeys to fix it. Please.")
                win.getMouse()
                quit()

            # Clear Image, might not be needed at all. (in certain situations)
            clear_image()

########################################################################################################################
# 5. The stuff Evan made
########################################################################################################################
###__IMAGE SHORTCUTS__### :
safe_base = Image(Point(270, 210), "01_safe_plain.gif")
safe_r1 = Image(Point(270, 210), "01_safe_red1.gif")
safe_r2 = Image(Point(270, 210), "01_safe_red2.gif")
safe_r3 = Image(Point(270, 210), "01_safe_red3.gif")
safe_g3 = Image(Point(270, 210), "01_safe_green3.gif")
safe_fail = Image(Point(270, 210), "01_safe_fail.gif")
safe_win = Image(Point(270, 210), "01_safe_win.gif")

inputs = []

def combo():
    win.setCoords(0.0, 420, 540, 0.0)
    safe_base.draw(win)
    inputs = []
    combo = [7,3,5]
    clickCounter = 0
    while True:
        p = win.getMouse()
        pX = p.getX()
        pY = p.getY()
        if pX >= 130 and pX <= 224 and pY >= 197 and pY <= 305:
            clickCounter = clickCounter + 1
            print("Click Counter =", clickCounter)
            if clickCounter == 1:
                safe_r1.draw(win)

                if pX >= 130 and pX <= 156 and pY >= 279 and pY <= 305:
                    print("7")
                    inputs.append(7)
            elif clickCounter == 2:
                safe_r2.draw(win)

                if pX >= 202 and pX <= 224 and pY >= 197 and pY <= 223:
                    print("3")
                    inputs.append(3)
            elif clickCounter == 3:
                safe_r3.draw(win)

                if pX >= 165 and pX <= 189 and pY >= 238 and pY <= 263:
                    print("5")
                    inputs.append(5)
                    print(inputs)
                    if inputs == combo:
                        safe_win.draw(win)
                        if win.getMouse():
                            break                   ###__EXIT LOOP TO VIDEO__###
                    else:
                        safe_fail.draw(win)         ###__EXCEPTION = 5__###
                        safe_base.undraw()
                        safe_r1.undraw()
                        safe_r2.undraw()
                        safe_r3.undraw()

                        if win.getMouse():
                            safe_base.draw(win)
                            safe_fail.undraw()
                            clickCounter = 0
                            inputs = []             ###__RINSE AND REPEAT__###
                else:
                    safe_fail.draw(win)
                    safe_base.undraw()
                    safe_r1.undraw()
                    safe_r2.undraw()
                    safe_r3.undraw()

                    if win.getMouse():
                        safe_base.draw(win)
                        safe_fail.undraw()
                        clickCounter = 0
                        inputs = []                 ###__RINSE AND REPEAT__###

    print("cool, you win.")
    win.setCoords(0.0, 0.0, 540, 420)

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
    # Orginal text size was 20
    name1 = Text(Point(135,135), "CAT BURGLAR:")
    name1.draw(win)
    name1.setFill("white")
    name1.setSize(13)
    name1.setFace("courier")
    #  name1.setStyle("bold")

    text1 = Text(Point(213,112), line1) #change x-coordinate to align
    text1.draw(win)
    text1.setFill("white")
    text1.setSize(13)
    text1.setFace("courier")
    #  text1.setStyle("bold")
    #  text1.setStyle("italic")
    #  text1.setStyle("bold italic")

    text2 = Text(Point(141,89), line2) #change x-coordinate to align
    text2.draw(win)
    text2.setFill("white")
    text2.setSize(13)
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
    # DEBRIEF ========================
    ###SKY_STARS### :

    bgsky = Rectangle(Point(-50,-50), Point(600,600))
    bgsky.draw(win)
    bgsky.setFill("Black")

    sstar1 = Circle(Point(30,300), 1)
    sstar1.draw(win)
    sstar1.setFill("white")

    sstar2 = Circle(Point(65,210), 1)
    sstar2.draw(win)
    sstar2.setFill("white")

    sstar3 = Circle(Point(90,250), 1)
    sstar3.draw(win)
    sstar3.setFill("white")

    sstar4 = Circle(Point(145,300), 1)
    sstar4.draw(win)
    sstar4.setFill("white")

    sstar5 = Circle(Point(160,200), 1)
    sstar5.draw(win)
    sstar5.setFill("white")

    sstar6 = Circle(Point(250,380), 1)
    sstar6.draw(win)
    sstar6.setFill("white")

    sstar7 = Circle(Point(225,300), 1)
    sstar7.draw(win)
    sstar7.setFill("white")

    sstar8 = Circle(Point(300,350), 1)
    sstar8.draw(win)
    sstar8.setFill("white")

    sstar9 = Circle(Point(150,350), 1)
    sstar9.draw(win)
    sstar9.setFill("white")

    sstar11 = Circle(Point(450,380), 1)
    sstar11.draw(win)
    sstar11.setFill("white")

    sstar12 = Circle(Point(345,310), 1)
    sstar12.draw(win)
    sstar12.setFill("white")

    sstar13 = Circle(Point(200,390), 1)
    sstar13.draw(win)
    sstar13.setFill("white")

###CLOUDS### :

    bgcloud = Rectangle(Point(-50,-50), Point(600,150))
    bgcloud.draw(win)
    bgcloud.setFill("LightSkyBlue4")
    bgcloud.setOutline("LightSkyBlue4")

    cloud1 = Circle(Point(-25,150), 50)
    cloud1.draw(win)
    cloud1.setFill("LightSkyBlue4")
    cloud1.setOutline("LightSkyBlue4")

    cloud2 = Circle(Point(35,120), 50)
    cloud2.draw(win)
    cloud2.setFill("LightSkyBlue4")
    cloud2.setOutline("LightSkyBlue4")

    cloud3 = Circle(Point(100,130), 40)
    cloud3.draw(win)
    cloud3.setFill("LightSkyBlue4")
    cloud3.setOutline("LightSkyBlue4")

    cloud4 = Circle(Point(158,125), 45)
    cloud4.draw(win)
    cloud4.setFill("LightSkyBlue4")
    cloud4.setOutline("LightSkyBlue4")

    cloud5 = Circle(Point(202,150), 30)
    cloud5.draw(win)
    cloud5.setFill("LightSkyBlue4")
    cloud5.setOutline("LightSkyBlue4")

    cloud6 = Circle(Point(260,153), 40)
    cloud6.draw(win)
    cloud6.setFill("LightSkyBlue4")
    cloud6.setOutline("LightSkyBlue4")

    cloud7 = Circle(Point(310,150), 30)
    cloud7.draw(win)
    cloud7.setFill("LightSkyBlue4")
    cloud7.setOutline("LightSkyBlue4")

    cloud8 = Circle(Point(350,125), 50)
    cloud8.draw(win)
    cloud8.setFill("LightSkyBlue4")
    cloud8.setOutline("LightSkyBlue4")

    cloud9 = Circle(Point(400,130), 35)
    cloud9.draw(win)
    cloud9.setFill("LightSkyBlue4")
    cloud9.setOutline("LightSkyBlue4")

    cloud10 = Circle(Point(450,130), 45)
    cloud10.draw(win)
    cloud10.setFill("LightSkyBlue4")
    cloud10.setOutline("LightSkyBlue4")

    cloud11 = Circle(Point(510,145), 40)
    cloud11.draw(win)
    cloud11.setFill("LightSkyBlue4")
    cloud11.setOutline("LightSkyBlue4")

    cloud12 = Circle(Point(540,165), 15)
    cloud12.draw(win)
    cloud12.setFill("LightSkyBlue4")
    cloud12.setOutline("LightSkyBlue4")

###MANSION### :

    mansion = Rectangle(Point(370,-50), Point(600,600))
    mansion.draw(win)
    mansion.setFill("Black")
    mansion.setOutline("lightsteelblue")

    ledge1 = Rectangle(Point(310,310), Point(600,330))
    ledge1.draw(win)
    ledge1.setFill("Black")
    ledge1.setOutline("lightsteelblue")
    ledge1.move(45,-206)

    ledge2 = Rectangle(Point(310,310), Point(600,330))
    ledge2.draw(win)
    ledge2.setFill("Black")
    ledge2.move(61,-207)

    window1 = Rectangle(Point(310,310), Point(370,440))
    window1.draw(win)
    window1.setFill("steelblue")
    window1.move(150,-50)
    window1.setOutline("lightsteelblue")

    window2 = Rectangle(Point(310,310), Point(370,440))
    window2.draw(win)
    window2.setFill("steelblue")
    window2.move(80,-50)
    window2.setOutline("lightsteelblue")

    window3 = Rectangle(Point(310,310), Point(370,440))
    window3.draw(win)
    window3.setFill("steelblue")
    window3.move(80,-185)
    window3.setOutline("lightsteelblue")

    window4 = Rectangle(Point(310,310), Point(370,440))
    window4.draw(win)
    window4.setFill("steelblue")
    window4.move(150,-185)
    window4.setOutline("lightsteelblue")

###TEXT### :
    # Original text size was 15
    text1 = Text(Point(180,380), "You are the world renown cat burglar")
    text1.draw(win)
    text1.setFill("white")
    text1.setSize(11)
    text1.setFace("courier")
    #text1.setStyle("italic")

    text2 = Text(Point(157,355), "Jean Paw Jean - treasure hunter")
    text2.draw(win)
    text2.setFill("white")
    text2.setSize(11)
    text2.setFace("courier")
    #text2.setStyle("italic")

    text3 = Text(Point(170,330), "extraordinaire.  You arrive at the")
    text3.draw(win)
    text3.setFill("white")
    text3.setSize(11)
    text3.setFace("courier")
    #text2.setStyle("italic")

    text4 = Text(Point(188,305), "mansion of the late Baron Richrichman,")
    text4.draw(win)
    text4.setFill("white")
    text4.setSize(11)
    text4.setFace("courier")
    #text2.setStyle("italic")

    text5 = Text(Point(188,280), "whose estate is at a complete loss for")
    text5.draw(win)
    text5.setFill("white")
    text5.setSize(11)
    text5.setFace("courier")
    #text2.setStyle("italic")

    text6 = Text(Point(183,255), "the location of his greatest fortune:")
    text6.draw(win)
    text6.setFill("white")
    text6.setSize(11)
    text6.setFace("courier")
    #text2.setStyle("italic")

    text7 = Text(Point(108,230), "The Goliath Diamond.")
    text7.draw(win)
    text7.setFill("white")
    text7.setSize(11)
    text7.setFace("courier")
    text7.setStyle("italic")

###TEXT_BREAK### :

    text8 = Text(Point(180,180), "Luckily for you, his last letter was")
    text8.draw(win)
    text8.setFill("white")
    text8.setSize(11)
    text8.setFace("courier")
    #text2.setStyle("italic")

    text9 = Text(Point(180,155), "intercepted in route... and with it,")
    text9.draw(win)
    text9.setFill("white")
    text9.setSize(11)
    text9.setFace("courier")
    #text2.setStyle("italic")

    text10 = Text(Point(180,130), "perhaps a clue as to the location of")
    text10.draw(win)
    text10.setFill("white")
    text10.setSize(11)
    text10.setFace("courier")
    #text2.setStyle("italic")

    text11 = Text(Point(149,105), "the invaluable missing stone.")
    text11.draw(win)
    text11.setFill("white")
    text11.setSize(11)
    text11.setFace("courier")
    #text2.setStyle("italic")

    clickme = Text(Point(170,50), "Click to read letter")
    clickme.draw(win)
    clickme.setFill("white")
    clickme.setSize(12)
    clickme.setFace("courier")
    clickme.setStyle("italic")

    # =================== END OF DEBRIEF
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

    # ==== undraw debrief
    bgsky.undraw()
    sstar1.undraw()
    sstar2.undraw()
    sstar3.undraw()
    sstar4.undraw()
    sstar5.undraw()
    sstar6.undraw()
    sstar7.undraw()
    sstar8.undraw()
    sstar9.undraw()
    sstar11.undraw()
    sstar12.undraw()
    sstar13.undraw()

    bgcloud.undraw()

    cloud1.undraw()
    cloud2.undraw()
    cloud3.undraw()
    cloud4.undraw()
    cloud5.undraw()
    cloud6.undraw()
    cloud7.undraw()
    cloud8.undraw()
    cloud9.undraw()
    cloud10.undraw()
    cloud11.undraw()
    cloud12.undraw()

    mansion.undraw()

    ledge1.undraw()
    ledge2.undraw()

    window1.undraw()
    window2.undraw()
    window3.undraw()
    window4.undraw()

    clickme.undraw()

    text1.undraw()
    text2.undraw()
    text3.undraw()
    text4.undraw()
    text5.undraw()
    text6.undraw()
    text7.undraw()
    text8.undraw()
    text9.undraw()
    text10.undraw()
    text11.undraw()

    # end of debrief undraw


##############################################################
# CALL MAIN HERE AT THE BOTTOM!
##############################################################
main()