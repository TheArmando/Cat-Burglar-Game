from tkinter import *

def safevideo():

    root = Tk()
    root.title("The Safe")

    frame=[]

    for i in range(1,62):
        fname="z_"+str(i)+".gif"
        frame+=[PhotoImage(file=fname)]

    wrap = Canvas(root, width=560, height=420)
    wrap.pack()

    def do_animation(currentframe):
            def do_image():
                    wrap.create_image(280,210,image=frame[currentframe], 
    tag='ani')
            # Delete the current picture if one exists
            wrap.delete('ani')
            try:
                    do_image()
            except IndexError:
                    # End of image list reached, decision:
                    currentframe = 60
                    do_image()
                    #currentframe = 0
                    #do_image()
            wrap.update_idletasks() #Force redraw
            currentframe = currentframe + 1
            # Call again to keep the animation running in a loop
            root.after(40, do_animation, currentframe) #frame rate
 
    # Start the animation loop just after the Tkinter loop begins
    root.after(10, do_animation, 0)

    root.mainloop()

safevideo()
