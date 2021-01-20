def on_button_pressed_a():
    global y
    led.unplot(x, y)
    y += -1
    led.plot(x, y)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global x1, y1
    x1 = x
    y1 = y
    led.plot(b1, randint(b2, 4))
    basic.pause(1000)
    if y == b2:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            . . . # #
            . . . # #
            """)
        basic.pause(1000)
    else:
        basic.show_leds("""
            . . . # #
            . . . # #
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global y
    y += 1
    led.plot(x, y)
    led.unplot(x, y - 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

y1 = 0
x1 = 0
b2 = 0
b1 = 0
y = 0
x = 0
x = 0
y = 0
led.plot(x, y)
b1 = 4
b2 = 0