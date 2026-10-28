import turtle
import random

def setup_screen(width: int, height: int, bg_color: tuple) -> turtle.Screen:
    """
    Configures the turtle screen with user-defined parameters and RGB background.
    Input:
        width (int): Window width in pixels.
        height (int): Window height in pixels.
        bg_color (tuple): RGB tuple (0-255) for the background fill.
    Output:
        turtle.Screen: The configured screen object ready for vector graphics.
    """
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.colormode(255)
    screen.bgcolor(bg_color)
    screen.title("Interactive Turtle Pattern & Fractal Renderer")
    return screen

def setup_pen(color: tuple, speed: int, thickness: int) -> turtle.Turtle:
    """
    Creates and configures a custom turtle pen.
    Input:
        color (tuple): Initial RGB tuple (0-255) for the pen color.
        speed (int): Drawing speed (0 is fastest).
        thickness (int): Width of the drawing line.
    Output:
        turtle.Turtle: The configured turtle drawing object.
    """
    pen = turtle.Turtle()
    pen.color(color)
    pen.speed(speed)
    pen.width(thickness)
    pen.hideturtle()
    return pen

def draw_koch_curve(pen: turtle.Turtle, length: float, depth: int):
    """
    Recursively renders a Koch curve fractal using directional movements.
    Input:
        pen (turtle.Turtle): The turtle object used for drawing.
        length (float): The length of the current segment.
        depth (int): The recursion depth for the fractal.
    Output:
        None (Visual rendering on screen)
    """
    if depth == 0:
        pen.forward(length)
    else:
        length /= 3.0
        draw_koch_curve(pen, length, depth - 1)
        pen.left(60)
        draw_koch_curve(pen, length, depth - 1)
        pen.right(120)
        draw_koch_curve(pen, length, depth - 1)
        pen.left(60)
        draw_koch_curve(pen, length, depth - 1)

def draw_geometric_spiral(pen: turtle.Turtle, iterations: int):
    """
    Generates a vibrant logarithmic-style geometric spiral pattern.
    Input:
        pen (turtle.Turtle): The turtle object used for drawing.
        iterations (int): Number of line segments to draw.
    Output:
        None (Visual rendering on screen)
    """
    for i in range(iterations):
        r = (i * 5) % 255
        g = (i * 3) % 255
        b = (255 - i) % 255
        pen.pencolor(r, g, b)
        
        pen.forward(i * 2)
        pen.right(91) # 91 degrees creates a shifting spiral effect

if __name__ == "__main__":
    bg_rgb = (20, 10, 30)
    screen = setup_screen(800, 800, bg_rgb)
    screen.tracer(0) 

    pen = setup_pen(color=(255, 255, 255), speed=0, thickness=2)
    
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    draw_geometric_spiral(pen, iterations=150)
    pen.penup()
    pen.goto(-150, 150)
    pen.pendown()
    pen.pencolor(0, 255, 200) # Cyan color for the fractal
    
    koch_size = 300
    koch_depth = 4
    
    for _ in range(3):
        draw_koch_curve(pen, koch_size, koch_depth)
        pen.right(120)
        
    screen.update()

    screen.exitonclick()