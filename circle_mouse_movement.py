import pyautogui
import math
import time

def round_move_mouse(size):
    # Get the screen dimensions
    screen_width, screen_height = pyautogui.size()

    random_x = screen_width // 2
    random_y = screen_height // 2

    pyautogui.moveTo(random_x, random_y, duration=0.3,_pause=False)

    radius = min(screen_width, screen_height) // size
    speed = 100000000  # Adjust the speed as needed

    # Calculate the circle path
    num_steps = 10000
    angle_step = (2 * math.pi) / num_steps

    # Move the mouse cursor in a circle
    for i in range(num_steps):
        x = random_x + int(math.cos(i * angle_step) * radius)
        y = random_y + int(math.sin(i * angle_step) * radius)
        pyautogui.moveTo(x, y, duration=0,_pause=False) 
        time.sleep(1 / speed)


# Driver Code:
# Here 5 is the Size of the Circle 
round_move_mouse(4)