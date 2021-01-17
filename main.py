def on_received_number(receivedNumber):
    global state
    state = receivedNumber
radio.on_received_number(on_received_number)

def on_forever():
    REDLIGHT = 0
    GREENLIGHT = 0
    state = 0
    if state == GREENLIGHT:
        basic.show_icon(IconNames.YES)
    elif state == REDLIGHT:
        basic.show_icon(IconNames.NO)
basic.forever(on_forever)

state = 0
state = 0
GREENLIGHT = 1
REDLIGHT = 2
radio.set_group(1)