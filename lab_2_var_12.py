import turtle

# Выносим переменные в глобальную область
left_bound = -50
right_bound = 50 
bottom_bound = 0  # Начинаем с нуля!
stripes = 0

def perform_switch_case(state, t, turn):
    global left_bound, right_bound, bottom_bound, stripes
    
    x = round(t.position()[0]+60)
    y = round(t.position()[1]-10)

    if state == "INIT":
        if True:
            state = "LEFT"
            t.setheading(180)  # ←
            return state, turn
        
    if state == "LEFT":
        t.forward(10)

        if x <= left_bound:
            state = "DOWN"
            if stripes >= 4:  # После 4 полос останавливаемся
                state = "STOP"
                return state, turn
            t.setheading(270)  # ↓
            bottom_bound -= 10  # Фиксированный шаг вниз
            stripes += 1
            return state, turn
            
            
            
        return state, turn
        
    if state == "DOWN":
        t.forward(10)

        if y <= bottom_bound:
            # Определяем направление по текущей X-координате
            if x <= left_bound:  # Мы слева - идем направо
                state = "RIGHT"
                t.setheading(0)  # →
            else:  # Мы справа - идем налево
                state = "LEFT"
                t.setheading(180)  # ←
            return state, turn
            
        return state, turn
        
    if state == "RIGHT":
        t.forward(10)

        if x >= right_bound:
            state = "DOWN" 
            t.setheading(270)  # ↓
            bottom_bound -= 10  # Фиксированный шаг вниз
            stripes += 1
            return state, turn
            
        return state, turn
        
    return state, turn

def draw():
    start_state = "INIT"
    end_state = "STOP" 
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(5)
    turn = 0

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)

        
    turtle.done()

if __name__ == "__main__":
    draw()
