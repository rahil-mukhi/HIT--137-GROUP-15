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


