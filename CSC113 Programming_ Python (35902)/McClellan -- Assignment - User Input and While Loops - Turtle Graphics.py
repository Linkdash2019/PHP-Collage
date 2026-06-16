import turtle
my_pen = turtle.Turtle()

while True:
    print("Enter square or octagon")
    user_input = input(">>> ")

    if user_input.lower() == "exit":
        break

    size = int(input("Input the size\n>>> "))
    color = input("Enter the color\n>>> ")

    try:
        my_pen.pencolor(color)
    except:
        my_pen.pencolor("black")

    if user_input.lower() == "square":
        my_pen.pendown()
        for i in range(4):
            my_pen.forward(25*size)
            my_pen.right(90)
        my_pen.penup()

    elif user_input.lower() == "octagon":
        my_pen.pendown()
        for i in range(8):
            my_pen.forward(25 * size)
            my_pen.right(45)
        my_pen.penup()
