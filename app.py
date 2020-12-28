
import tkinter as tk
import time
import random_gen as r


b_font = ("times", 40, "bold")
s_font = ("times", 12, "bold")
# colours program can choose from
colours = ["red", "orange", "yellow", "green", "blue", "purple", 
           "black", "white", "pink", "brown", "grey"]


def get_colours():
  '''
  Uses random_gen to get a random colour for each variable.
  '''
  # makes variables global to be accessible by rest of program
  global bg_colour, txt, txt_colour
  # calls random_gen to get random value in colours and assigns to variables
  while (True):
    bg_colour = r.get_random_num(colours)
    txt = r.get_random_num(colours)
    txt_colour = r.get_random_num(colours)

    # If background colour and text colour are not the same, break from loop.
    # So the text won't blend in with the background.
    if (bg_colour != txt_colour):
      break


def show_start():
  '''
  Displays start frame with title and instructions.
  '''
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
  '''
  Displays game frame with different background/text colours.
  '''
  frame.destroy()
  # calls get_colours to get new randomized colours each time game starts
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
  # calls check_entry every time 'Enter' is pressed
  entry.bind("<Return>", lambda event: check_entry(entry.get()))


def show_result(frame):
  '''
  Displays results frame with time and options to replay/Displays
  '''
  frame.destroy()
  
  result_frame = tk.Frame(wn, background = "green")
  # congrats message
  tk.Label(result_frame, 
          text = "Correct!!", 
          background = "green", 
          foreground = "black", 
          font = b_font, 
          ).pack(anchor = "center", pady = 20)
  tk.Label(result_frame, 
           text = f"Nice job! You guessed the right colour in {time_diff:.2f} s.\n\
                    \nClick 'Play again' to play the game again \nor 'EXIT' to close the program.", 
           background = "green", 
           foreground = "black", 
           font = s_font, 
           ).pack(anchor = "center", pady = 20)
  # replay button
  tk.Button(result_frame, 
            text = "Play again", 
            background = "grey", 
            foreground = "white", 
            width = 20, 
            font = s_font, 
            command = lambda: show_game(result_frame), 
            ).pack(anchor = "center", pady = 10)
  # quit button
  tk.Button(result_frame, 
            text = "EXIT", 
            background = "grey", 
            foreground = "white", 
            width = 20, 
            font = s_font, 
            command = quit
            ).pack(anchor = "center", pady = 10)
  
  result_frame.pack(fill = "both", expand = True)

  
def check_entry(entry):
  '''
  Checks whether entry is right or not.
  '''
  global time_diff
  
  incorrect_message = tk.Label(game_frame, 
                               text = "Incorrect! Try again...", 
                               background = colours[bg_colour], 
                               foreground = colours[txt_colour], 
                               font = s_font, 
                               )
  
  if (entry == colours[txt_colour]):
    # gets current time when guess is correct and finds time difference
    time_diff = time.perf_counter() - start_time
    show_result(game_frame)
  elif (entry != colours[txt_colour]):
    # displays message that guess is wrong and disappears after 1 sec
    incorrect_message.pack(anchor = "center", side = "bottom")
    wn.after(1000, incorrect_message.destroy)


wn = tk.Tk()
wn.title("Colour Guessing Game")
wn.minsize(400, 400) # widthxheight
wn.iconphoto(False, tk.PhotoImage(file = "colourGame-logo.png"))

show_start()
wn.mainloop()
