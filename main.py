
state = 0
GREENLIGHT = 1
REDLIGHT = 2
movement = 0
radio.set_group(1)

def on_received_number(receivedNumber):
    global state
    state = receivedNumber
radio.on_received_number(on_received_number)

def on_forever():
    global REDLIGHT
    global GREENLIGHT
    global state

    if state == GREENLIGHT:
        basic.show_icon(IconNames.YES)
    elif state == REDLIGHT:
        basic.show_icon(IconNames.NO)
basic.forever(on_forever)

def on_forever2():
    global movement
    if state == REDLIGHT:
        movement = abs(input.acceleration(Dimension.STRENGTH) - 1000)
        if movement > 100:
            game.game_over()
basic.forever(on_forever2)
