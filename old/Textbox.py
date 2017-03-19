from graphics import *

def textbox():
    win = GraphWin("Introduction", 540, 420)
    win.setCoords(0.0,0.0,540,420)

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
    
    text1 = Text(Point(213,112), "I like diamonds... meeow.") #change x-coordinate to align
    text1.draw(win)
    text1.setFill("white")
    text1.setSize(20)
    text1.setFace("courier")
    #  text1.setStyle("bold")
    #  text1.setStyle("italic")
    #  text1.setStyle("bold italic")

    text2 = Text(Point(141,89), "Who's there!?") #change x-coordinate to align
    text2.draw(win)
    text2.setFill("white")
    text2.setSize(20)
    text2.setFace("courier")
    #  text2.setStyle("bold")
    text2.setStyle("italic")
    #  text2.setStyle("bold italic")
    win.getMouse()
    
textbox()
