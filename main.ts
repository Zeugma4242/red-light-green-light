radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    state = receivedNumber
})
basic.forever(function on_forever() {
    let REDLIGHT = 0
    let GREENLIGHT = 0
    let state = 0
    if (state == GREENLIGHT) {
        basic.showIcon(IconNames.Yes)
    } else if (state == REDLIGHT) {
        basic.showIcon(IconNames.No)
    }
    
})
let state = 0
state = 0
let GREENLIGHT = 1
let REDLIGHT = 2
radio.setGroup(1)
