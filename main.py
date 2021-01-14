y = 0

def on_button_pressed_a():
    global y
    y += -1
    led.plot(0, y)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global y
    y += 1
    led.plot(0, y)
input.on_button_pressed(Button.B, on_button_pressed_b)
