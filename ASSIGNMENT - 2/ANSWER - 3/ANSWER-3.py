# GROUP NAME : CAS/DAN GROUP-15
# GROUP MEMBERS: 385218 RAHIL MUKHI
#                374427 RENISH VEKARIYA
#                384646 RUHINA RAJABALI
#                383635 RUSHABHKUMAR SAVAJ

import turtle
def draw_branch(branch_length, left_angle, right_angle, depth, reduction_factor, first_branch=True):
    if depth == 0:
        return

    # Set the color based on whether it's the Trunk or Leaves
    if first_branch:
        t.pencolor("brown")
    else:
        t.pencolor("green")

    # Drawing of the branch
    t.pensize(max(1, depth))  # Adjusting the pen size based on depth
    t.forward(branch_length)

    # Drawing of the left branch
    t.left(left_angle)
    draw_branch(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor, False)

    # Return to the original direction and position
    t.right(left_angle + right_angle)
    draw_branch(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor, False)

    # Return to the original direction
    t.left(right_angle)
    t.backward(branch_length)

    # Taking input from the user
left_arrow = int(input("Enter the left branch angle (in degrees): "))
right_arrow = int(input("Enter the right branch angle (in degrees): "))
starting_branch_length = int(input("Enter the starting branch length : "))
recursion_depth = int(input("Enter the recursion depth: "))
reduction_factor = float(input("Enter the branch length reduction factor: "))

# Setting up of the turtle screen
screen = turtle.Screen()
screen.title("Recursive Tree Pattern")

# Setting up of the turtle
t = turtle.Turtle()
t.speed("fast")
t.penup()

# Adjusting the start position to center the tree
t.goto(0, -starting_branch_length * 2)

t.pendown()
t.left(90)  # Pointing the turtle towards upwards

# Drawing the tree
draw_branch(starting_branch_length, left_arrow, right_arrow, recursion_depth, reduction_factor)

t.hideturtle()  # Hide the turtle after the tree is drawn

input("Press Enter to exit...")


