def on_button_pressed_a():
    basic.clear_screen()
    basic.pause(500)
    basic.show_string("Szia!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.clear_screen()
    basic.pause(500)
    basic.show_number(randint(0, 10))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.clear_screen()
    basic.pause(500)
    basic.show_number(2022)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.HAPPY)