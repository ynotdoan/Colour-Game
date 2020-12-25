
import tkinter as tk
import random_gen as r


wn = tk.Tk()
wn.title("Colour Guessing Game")
wn.minsize(400, 400) # widthxheight


d_font = ("times", 50, "bold")
colours = ["red", "orange", "yellow", "green", "blue", "purple", 
           "black", "white", "pink", "brown", "grey"]

# calls random_gen to get random value in colours
while (True):
  bg_colour = r.get_random_num(colours)
  print (bg_colour)
  txt = r.get_random_num(colours)
  print (colours[txt])
  txt_colour = r.get_random_num(colours)
  print (txt_colour)
  
  if (bg_colour != txt_colour):
    break

m_frame = tk.Frame(wn, 
                   background = colours[bg_colour])
m_frame.pack(fill = "both", expand = True)

lbl = tk.Label(m_frame, 
               text = colours[txt], 
               background = colours[bg_colour], 
               foreground = colours[txt_colour], 
               font = d_font)
lbl.pack()

wn.mainloop()
