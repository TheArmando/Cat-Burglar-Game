from graphics import *

def debrief():
    win = GraphWin("Introduction", 540, 420)
    win.setCoords(0.0,0.0,540,420)

###SKY_STARS### :    

    bgsky = Rectangle(Point(-50,-50), Point(600,600))
    bgsky.draw(win)
    bgsky.setFill("Black")

    star1 = Circle(Point(30,300), 1)
    star1.draw(win)
    star1.setFill("white")

    star2 = Circle(Point(65,210), 1)
    star2.draw(win)
    star2.setFill("white")

    star3 = Circle(Point(90,250), 1)
    star3.draw(win)
    star3.setFill("white")

    star4 = Circle(Point(145,300), 1)
    star4.draw(win)
    star4.setFill("white")

    star5 = Circle(Point(160,200), 1)
    star5.draw(win)
    star5.setFill("white")

    star6 = Circle(Point(250,380), 1)
    star6.draw(win)
    star6.setFill("white")

    star7 = Circle(Point(225,300), 1)
    star7.draw(win)
    star7.setFill("white")

    star8 = Circle(Point(300,350), 1)
    star8.draw(win)
    star8.setFill("white")

    star9 = Circle(Point(150,350), 1)
    star9.draw(win)
    star9.setFill("white")

    star11 = Circle(Point(450,380), 1)
    star11.draw(win)
    star11.setFill("white")

    star12 = Circle(Point(345,310), 1)
    star12.draw(win)
    star12.setFill("white")

    star13 = Circle(Point(200,390), 1)
    star13.draw(win)
    star13.setFill("white")

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

    text1 = Text(Point(180,380), "You are the world renown cat burglar")
    text1.draw(win)
    text1.setFill("white")
    text1.setSize(15)
    text1.setFace("courier")
    #text1.setStyle("italic")

    text2 = Text(Point(157,355), "Jean Paw Jean - treasure hunter")
    text2.draw(win)
    text2.setFill("white")
    text2.setSize(15)
    text2.setFace("courier")
    #text2.setStyle("italic")

    text3 = Text(Point(170,330), "extraordinaire.  You arrive at the")
    text3.draw(win)
    text3.setFill("white")
    text3.setSize(15)
    text3.setFace("courier")
    #text2.setStyle("italic")

    text4 = Text(Point(188,305), "mansion of the late Baron Richrichman,")
    text4.draw(win)
    text4.setFill("white")
    text4.setSize(15)
    text4.setFace("courier")
    #text2.setStyle("italic")

    text5 = Text(Point(188,280), "whose estate is at a complete loss for")
    text5.draw(win)
    text5.setFill("white")
    text5.setSize(15)
    text5.setFace("courier")
    #text2.setStyle("italic")

    text6 = Text(Point(183,255), "the location of his greatest fortune:")
    text6.draw(win)
    text6.setFill("white")
    text6.setSize(15)
    text6.setFace("courier")
    #text2.setStyle("italic")

    text7 = Text(Point(108,230), "The Goliath Diamond.")
    text7.draw(win)
    text7.setFill("white")
    text7.setSize(15)
    text7.setFace("courier")
    text7.setStyle("italic")

###TEXT_BREAK### :    

    text8 = Text(Point(180,180), "Luckily for you, his last letter was")
    text8.draw(win)
    text8.setFill("white")
    text8.setSize(15)
    text8.setFace("courier")
    #text2.setStyle("italic")

    text9 = Text(Point(180,155), "intercepted in route... and with it,")
    text9.draw(win)
    text9.setFill("white")
    text9.setSize(15)
    text9.setFace("courier")
    #text2.setStyle("italic")

    text10 = Text(Point(180,130), "perhaps a clue as to the location of")
    text10.draw(win)
    text10.setFill("white")
    text10.setSize(15)
    text10.setFace("courier")
    #text2.setStyle("italic")

    text11 = Text(Point(149,105), "the invaluable missing stone.")
    text11.draw(win)
    text11.setFill("white")
    text11.setSize(15)
    text11.setFace("courier")
    #text2.setStyle("italic")

    clickme = Text(Point(170,50), "Click to read letter")
    clickme.draw(win)
    clickme.setFill("white")
    clickme.setSize(16)
    clickme.setFace("courier")
    clickme.setStyle("italic")

debrief()
