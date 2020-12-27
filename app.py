
import tkinter as tk
import random_gen as r


d_font = ("times", 40, "bold")
colours = ["red", "orange", "yellow", "green", "blue", "purple", 
           "black", "white", "pink", "brown", "grey"]

# calls random_gen to get random value in colours
while (True):
  bg_colour = r.get_random_num(colours)
  txt = r.get_random_num(colours)
  txt_colour = r.get_random_num(colours)

  # If background colour and text colour are not the same, break from loop.
  # So the text won't blend in with the background.
  if (bg_colour != txt_colour):
    break


def show_start():
  start_frame.pack(fill = "both", expand = True)
  

def show_game():
  start_frame.pack_forget()
  game_frame.pack(fill = "both", expand = True)


wn = tk.Tk()
wn.title("Colour Guessing Game")
wn.minsize(400, 400) # widthxheight


start_frame = tk.Frame(wn, background = "gold")
# game title
tk.Label(start_frame, 
         text = "Speed Colour\nGame", 
         background = "gold", 
         foreground = "black", 
         font = d_font, 
         ).pack(pady = 30)
# instructions label 
tk.Label(start_frame, 
         text = "Try to type the colour of the word on-screen quickly!\n \
                 \nClick 'Start' to begin.", 
         background = "gold", 
         foreground = "black", 
         font = ("times", 12)
         ).pack(anchor = "center")
# start button
tk.Button(start_frame, 
          text = "Start!", 
          width = 30,  
          command = lambda: show_game(), 
          ).pack(anchor = "center", expand = True)


game_frame = tk.Frame(wn, background = colours[bg_colour])
# colour text label
tk.Label(game_frame, 
         text = colours[txt], 
         background = colours[bg_colour], 
         foreground = colours[txt_colour], 
         font = d_font, 
         ).pack(pady = 70)
# entry box
tk.Entry(game_frame, 
         width = 30, 
         borderwidth = 5, 
         ).pack(anchor = "center", expand = True)



show_start()
wn.mainloop()
