
import tkinter as tk
import time
import random_gen as r


b_font = ("times", 40, "bold")
s_font = ("times", 12, "bold")
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
  start_frame = tk.Frame(wn, background = "gold")
  # game title
  tk.Label(start_frame, 
          text = "Speed Colour\nGame", 
          background = "gold", 
          foreground = "black", 
          font = b_font, 
          ).pack(pady = 30)
  # instructions label 
  tk.Label(start_frame, 
          text = "Try to type the colour of the word on-screen quickly!\n \
                  \nClick 'Start' to begin.", 
          background = "gold", 
          foreground = "black", 
          font = s_font, 
          ).pack(anchor = "center")
  # start button
  tk.Button(start_frame, 
            text = "Start!", 
            width = 30, 
            font = s_font, 
            command = lambda: show_game(start_frame), 
            ).pack(anchor = "center", expand = True)
  
  start_frame.pack(fill = "both", expand = True)


def show_game(frame):
  frame.destroy()
  get_colours()
  
  global game_frame, start_time
  
  game_frame = tk.Frame(wn, background = colours[bg_colour])
  # colour text label
  tk.Label(game_frame, 
          text = colours[txt], 
          background = colours[bg_colour], 
          foreground = colours[txt_colour], 
          font = b_font, 
          ).pack(pady = 70)
  # entry instructions
  tk.Label(game_frame, 
          text = "Click 'Enter' to check", 
          background = colours[bg_colour], 
          foreground = colours[txt_colour], 
          font = s_font, 
          ).pack(anchor = "center")
  # entry box
  entry = tk.Entry(game_frame, 
                  width = 30, 
                  borderwidth = 5, 
                  )
  entry.pack(anchor = "center", expand = True)

  game_frame.pack(fill = "both", expand = True)
  # starts timer after game_frame is shown
  start_time = time.perf_counter()
  entry.bind("<Return>", lambda event: check_entry(entry.get()))


def show_result(frame):
  frame.destroy()
  
  result_frame = tk.Frame(wn, background = "green")
  # congrats message
  tk.Label(result_frame, 
          text = f"Correct!! {time_diff:.2f} s", 
          background = "green", 
          foreground = "black", 
          font = b_font, 
          ).pack(anchor = "center", expand = True)
  # more labels here...
  # quit button
  tk.Button(result_frame, 
            text = "EXIT", 
            background = "grey", 
            foreground = "white", 
            width = 20, 
            font = s_font, 
            command = quit
            ).pack(anchor = "center", expand = True)
  
  result_frame.pack(fill = "both", expand = True)
  result_frame.focus_set()
  result_frame.bind("<Return>", lambda event: show_game(result_frame))
  
def check_entry(entry):
  global time_diff
  
  if (entry == colours[txt_colour]):
    # gets current time when guess is correct and finds time difference
    time_diff = time.perf_counter() - start_time
    show_result(game_frame)
  elif (entry != colours[txt_colour]):
    # displays incorrect message 
    incorrect = tk.Label(game_frame, 
                         text = "Incorrect! Try again...", 
                         background = colours[bg_colour], 
                         foreground = colours[txt_colour], 
                         font = s_font, 
                         )
    incorrect.pack(anchor = "center", side = "bottom"), 
    incorrect.after(1000, incorrect.destroy())
    

wn = tk.Tk()
wn.title("Colour Guessing Game")
wn.minsize(400, 400) # widthxheight

show_start()
wn.mainloop()
