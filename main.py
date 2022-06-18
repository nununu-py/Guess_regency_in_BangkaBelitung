from turtle import Turtle, Screen
import pandas

data = pandas.read_csv("bangka_belitung_regency.csv")
all_regency = data.regency.to_list()
print(all_regency)

screen = Screen()
screen.setup(height=600, width=1000)
screen.title("Guess regency game")
image = "blank_states_img.gif"
image2 = "bangka-belitung27.gif"
screen.addshape(image2)

display_guess = Turtle()
display_guess.shape(image2)

guess = 0
list_user_guess = []

while guess < 7:
    user_guess = screen.textinput(title="Guess regency", prompt=f"Correct Answer {guess}/7 ").title()
    list_user_guess.append(user_guess)
    if user_guess in all_regency:
        display_guess = Turtle()
        display_guess.hideturtle()
        display_guess.penup()
        data_regency = data[data.regency == user_guess]
        display_guess.goto(int(data_regency.x), int(data_regency.y))
        display_guess.write(arg=f"{user_guess}", align="center", font=("Arial", 10, "bold"))
        guess += 1
        wrong_user_guess = [wrong_answer for wrong_answer in list_user_guess if wrong_answer not in all_regency]
        invalid_guess = pandas.DataFrame(wrong_user_guess)
        invalid_guess.to_csv("invalid_user_guess.csv")
    elif user_guess == "Exit":
        break

screen.exitonclick()
