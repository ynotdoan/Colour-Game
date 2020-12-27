
import tkinter as tk
import time
import random_gen as r


d_font = ("times", 40, "bold")
colours = ["red", "orange", "yellow", "green", "blue", "purple", 
           "black", "white", "pink", "brown", "grey"]

def get_colours():
  # makes variables global to be accessible by rest of program
  global bg_colour, txt, txt_colour
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
  
def show_game(frame):
  frame.pack_forget()
  game_frame.pack(fill = "both", expand = True)
  
def show_result():
  game_frame.pack_forget()
  result_frame.pack(fill = "both", expand = True)
  
def check_entry(entry):
  if (entry == colours[txt_colour]):
    show_result()
  elif (entry != colours[txt_colour]):
    print ("OOF")
    

wn = tk.Tk()
wn.title("Colour Guessing Game")
wn.minsize(400, 400) # widthxheight

get_colours()
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
          command = lambda: show_game(start_frame), 
          ).pack(anchor = "center", expand = True)


game_frame = tk.Frame(wn, background = colours[bg_colour])
# colour text label
tk.Label(game_frame, 
         text = colours[txt], 
         background = colours[bg_colour], 
         foreground = colours[txt_colour], 
         font = d_font, 
         ).pack(pady = 70)
# entry instructions
tk.Label(game_frame, 
         text = "Click 'Enter' to check", 
         background = colours[bg_colour], 
         foreground = colours[txt_colour], 
         font = ("times", 12), 
         ).pack(anchor = "center")
# entry box
entry = tk.Entry(game_frame, 
                 width = 30, 
                 borderwidth = 5, 
                 )
entry.pack(anchor = "center", expand = True)
entry.bind("<Return>", lambda event: check_entry(entry.get()))


result_frame = tk.Frame(wn, background = "green")
# congrats message
tk.Label(result_frame, 
         text = "Correct!! ", 
         background = "green", 
         foreground = "black", 
         font = d_font, 
         ).pack(anchor = "center")
# press key to continue
result_frame.focus_set()
result_frame.bind("<Return>", lambda event: show_game(result_frame))


show_start()
wn.mainloop()
