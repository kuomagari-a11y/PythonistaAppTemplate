import keyboard
from tkinter import *

ball = {
    "dirx": 15,
    "diry": -15,
    "x": 350,
    "y": 300,
    "w": 10,
}
bar = {
    "x": 550,
    "y": 100,
    "w": 100,
}
count = 0

win = Tk()
cv = Canvas(win, width=600, height=400)
cv.pack()

def draw_ball():
    cv.create_oval(
        ball["x"] - ball["w"], ball["y"] - ball["w"],
        ball["x"] + ball["w"], ball["y"] + ball["w"],
        fill="green")

def draw_bar():
    cv.create_rectangle(
        bar["x"] - 5, bar["y"] - bar["w"],
        bar["x"] + 5, bar["y"] + bar["w"],
        fill="black")

def move_ball():
    global count
    bx = ball["x"] + ball["dirx"]
    by = ball["y"] + ball["diry"]
    
    if bx < 0:
        ball["dirx"] *= -1
    if by < 0 or by > 400:
        ball["diry"] = ball["diry"] * (-1)
    if bx > 550 and (by > bar["y"] - bar["w"] and  by < bar["y"] + bar["w"] ):
        ball["dirx"] *= -1
        count += 1
    if bx > 600:
        cv.create_text(100, 200, text="YOU LOSE", fill="red", font=("Bold", 20))
        win.quit()
 
    ball["x"] += ball["dirx"]
    ball["y"] += ball["diry"]

def move_bar():   
    if keyboard.is_pressed('up'):
        bar["y"] -= 10
    if keyboard.is_pressed('down'):
        bar["y"] += 10
    
    if bar["y"] < 0:
        bar["y"] = 0
    if bar["y"] > 400:
        bar["y"] = 400

def draw_score():
    global count
    cv.create_text(100, 20, text="Score: {}".format(count*100), fill="black", font=("Arial", 16))

def game_loop():
    cv.delete("all")
    draw_ball()
    draw_bar()
    move_ball()
    move_bar()
    draw_score()
    win.after(20, game_loop)

game_loop()
win.mainloop()
