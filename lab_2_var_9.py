import turtle

# Глобальные переменные
right_bound = 0
columns = 0

def perform_switch_case(state, t, turn):
    global right_bound, columns
    
    x = round(t.position()[0])
    y = round(t.position()[1]-60)

    if state == "INIT":
        if True:
            state = "UP"
            t.setheading(90)
            return state, turn
        return state, turn
        
    if state == "UP":
        t.forward(10)

        if columns >= 5:
            if y<= 40:
                state = "UP"
                return state, turn
            else: 
                state = "STOP"
                return state, turn

        if y >= 50:
            state = "RIGHT"
            t.setheading(0)
            return state, turn
        return state, turn
        
    if state == "RIGHT":
        t.forward(10)

        if x >= right_bound:
            if y >= 50:
                state = "DOWN"
                t.setheading(270)
                return state, turn
            else:
                state = "UP"
                t.setheading(90)
                return state, turn
        return state, turn
        
    if state == "DOWN":
        t.forward(10)

        if y <= -50:
            state = "RIGHT"
            t.setheading(0)
            right_bound += 10
            columns += 1
            return state, turn
        return state, turn
        
    return state, turn


def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(5)
    turn = 1

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)
        
    turtle.done()


if __name__ == "__main__":
    draw()
