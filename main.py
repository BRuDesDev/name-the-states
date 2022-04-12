import turtle
import pandas


def get_mouse_click_coor(x, y):
    print(x, y)


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screen.listen()

# List of correct states
correct_states = []

# Getting data from CSV
data = pandas.read_csv("50_states.csv")
# Creating States List
states_lst = data["state"].to_list()

turtle.onscreenclick(get_mouse_click_coor)

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states_lst if state not in correct_states]
        # missing_states = []
        # for state in states_lst:
        #     if state not in correct_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(states_lst)
        new_data.to_csv("states_to_learn")
        break
    if answer_state in states_lst:
        states_lst.remove(answer_state)
        correct_states.append(answer_state)
        state = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Move turtle to state and write name
        t.goto(int(state.x), int(state.y))
        t.write(answer_state, align="center", font=("Arial", 10, "bold"))

