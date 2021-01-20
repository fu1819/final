input.onButtonPressed(Button.A, function () {
    led.unplot(x, y)
    y += -1
    led.plot(x, y)
})
input.onButtonPressed(Button.AB, function () {
    x1 = x
    y1 = y
    b3 = randint(b2, 4)
    led.plot(b1, b3)
    basic.pause(1000)
    if (y == b3) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            . . . # #
            . . . # #
            `)
        basic.pause(1000)
    } else {
        basic.showLeds(`
            . . . # #
            . . . # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(1000)
    }
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    y += 1
    led.plot(x, y)
    led.unplot(x, y - 1)
})
let b3 = 0
let y1 = 0
let x1 = 0
let b2 = 0
let b1 = 0
let y = 0
let x = 0
x = 0
y = 0
led.plot(x, y)
b1 = 4
b2 = 0
