from tkinter import *
import tkinter as tk
#from Vault_Animation import (safevideo)


##def safevideo():
##        if __name__=="__main__":
##        safevideo():

######

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


######

root = tk.Tk()

root.title("The Safe")
w = 540
h = 420
canvas = tk.Canvas(root, width=w, height=h)
canvas.pack()
img1 = tk.PhotoImage(file='vault_ext.gif')
img2 = tk.PhotoImage(file='vault_ext_text.gif')
img2_ref = canvas.create_image(w//2, h//2, image=img2)
img1_ref = canvas.create_image(w//2, h//2, image=img1)

counter = 0
combo = [7,3,5]
inputs = []

def printer(event):
                       
                global counter
                x, y = event.x, event.y
         
                if event.x in range (130,224) and event.y in range(197,305):   ##RED LIGHTS##
                    if counter == 0:
                        canvas.create_oval(146, 158, 140, 164, outline="indianred2", fill="red", width=1.5)
                    
                    elif counter == 1:
                        canvas.create_oval(180.5, 158, 174.5, 164, outline="indianred2", fill="red", width=1.5)
                    
                    elif counter == 2:
                        canvas.create_oval(209, 158, 215, 164, outline="indianred2", fill="red", width=1.5)           
                    
                    counter = counter + 1
                  
                if event.x in range(130,156) and event.y in range(279,305):
                    print("7")
                    inputs.append(7)
                
                elif event.x in range(202,224) and event.y in range(197,223):
                    print("3")
                    inputs.append(3)
                
                elif event.x in range(165,189) and event.y in range(238,263):
                    print("5")
                    inputs.append(5)

                #print(inputs)

                while counter > 2:
                    if inputs == combo:   #GREEN LIGHTS##
                        canvas.create_oval(146, 158, 140, 164, outline="palegreen1", fill="green2", width=1.5)
                        canvas.create_oval(180.5, 158, 174.5, 164, outline="palegreen1", fill="green2", width=1.5)
                        canvas.create_oval(209, 158, 215, 164, outline="palegreen1", fill="green2", width=1.5)
                        ###print("CORRECT!")###
                        break
                        safevideo()
                        ###CUT TO VIDEO###                           

                    else:
                        print("WRONG!")###
                        break
                        
                        canvas.configure(image=img2)
                        canvas.image = img2
                        ###CUT TO TEXT BOX###
                        ###RESTART PROGRAM###

canvas.bind("<Button-1>", printer)
root.mainloop()


