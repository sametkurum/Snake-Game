#Snake Game Program
import tkinter as tk
import random 

def move_snake():
    global direction
    
    for i in range(len(snake_parts)-1,0,-1):
        x1, y1, x2, y2 = canvas.coords(snake_parts[i-1])
        canvas.coords(snake_parts[i], x1, y1, x2, y2)

    coords = canvas.coords(snake_parts[0])
    x1, y1, x2, y2 = coords

    if x1 < 0 or x2 > 500 or y1 < 0 or y2 > 500:
        print("GAME OVER")
        return 

    if direction == "Right":
        canvas.move(snake_parts[0], step, 0)

    elif direction == "Left":
        canvas.move(snake_parts[0], -step, 0)

    elif direction == "Up":
        canvas.move(snake_parts[0], 0, -step)
    
    elif direction == "Down":
        canvas.move(snake_parts[0], 0, step)

    check_eating()

    window.after(speed, move_snake)

def change_direction(new_direction):
    global direction
    direction = new_direction

def check_eating():
    global food
    coords_snake = canvas.coords(snake_parts[0])
    snake_x1, snake_y1, snake_x2, snake_y2 = coords_snake

    coords_food = canvas.coords(food)
    food_x1, food_y1, food_x2, food_y2 = coords_food

    if (food_x1 < snake_x2 and food_x2 > snake_x1 and
        food_y1 < snake_y2 and food_y2 > snake_y1):
        eating() 
    
def eating():
    global food
    canvas.delete(food)
    place_food()
    grow_snake()

def place_food():
    global food
    food_coords = random.randint(35, 475)
    food = canvas.create_oval(food_coords, food_coords, 
                              food_coords+15, food_coords+15, fill="red")
    
def grow_snake():
    last_coords = canvas.coords(snake_parts[-1])
    x1, y1, x2, y2 = last_coords

    new_part = canvas.create_oval(x1, y1, x2, y2, fill="green")
    snake_parts.append(new_part)
    

window = tk.Tk()
window.title("Snake Game")
window.geometry("500x500+450+100")
icon = tk.PhotoImage(file='my_logo.png')
window.iconphoto(True,icon)

speed = 100
direction = "Right"
step = 20

canvas= tk.Canvas(window, bg="black", width=500, height=500)
canvas.pack()

snake_parts = [canvas.create_oval(200, 200, 230, 230, fill="green")]

window.bind("<Right>", lambda e: change_direction("Right"))
window.bind("<Left>", lambda e: change_direction("Left"))
window.bind("<Up>", lambda e: change_direction("Up"))
window.bind("<Down>", lambda e: change_direction("Down"))

place_food()
move_snake()

window.mainloop()