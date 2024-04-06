# Circle Mouse Movement

## Overview
This Python script enables the generation of circular mouse movement patterns on the screen. It utilizes the PyAutoGUI library to control the mouse cursor and performs circular movements based on specified parameters.

## Features
- Generates circular mouse movement patterns on the screen.
- Customizable parameters such as circle size and speed.
- Can be used for testing, demonstration, or fun purposes.

## Installation
1. Ensure you have Python installed on your system.
2. Install the required dependencies:
    ```
    pip install pyautogui
    ```
3. Clone this repository or download the `circular_mouse_movement.py` file.

4. or just copy the code and paste it in your .py file

## Usage
1. Import the `round_move_mouse` function from `circular_mouse_movement.py`.
2. Call the `round_move_mouse` function with the desired size parameter.
3. Adjust parameters as needed for different circular movement patterns.

Example:
```python
from circular_mouse_movement import round_move_mouse

# Generate a circular mouse movement, Here 5 is the circle size !!!
round_move_mouse(5)
