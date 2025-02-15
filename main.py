import turtle
import pandas as panda

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data_from_csv = panda.read_csv("50_states.csv")
total_states = state_data_from_csv["state"].to_list()
total_states_count = len(total_states)
total_correct_states = []

while len(total_correct_states) < total_states_count:
    input_state = screen.textinput(
        title=f"Guess the State {len(total_correct_states)}/{total_states_count}",
        prompt="What's another state's name?",
    )
    if len(input_state) > 0:
        for i in range(total_states_count):
            current_state_name = total_states[i]
            if input_state.lower() == current_state_name.lower():
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                total_correct_states.append(current_state_name)
                state_current_data = state_data_from_csv[
                    state_data_from_csv.state == current_state_name
                ]
                t.goto(int(state_current_data.x), int(state_current_data.y))
                t.write(current_state_name)
                t.pendown()


turtle.mainloop()
