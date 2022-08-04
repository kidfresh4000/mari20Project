index = 0

def on_button_pressed_a():
    basic.show_leds("""
        . . . # .
                . . # # .
                . # # # .
                . # # . .
                # . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                # # # # #
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . # # . .
                # # # # #
                . # . . .
                # . . . .
    """)
    basic.show_leds("""
        . . # . .
                . # # # .
                # # # # #
                . . . . .
                # . # . #
    """)
    basic.show_leds("""
        . . # . .
                . . # . .
                . . # . .
                . . # . .
                . . # . .
    """)
    basic.show_leds("""
        . . # # #
                # . # . #
                # # # # #
                . . . # .
                . . # . #
    """)
    basic.show_leds("""
        . . # . .
                . . # . .
                . . # . .
                # # # # #
                . . # . .
    """)
    basic.show_leds("""
        . . # . .
                . # # # .
                # . # . #
                # # # # #
                . . # . .
    """)
    basic.show_leds("""
        . # . # .
                # # # # #
                . # . # .
                # # # # #
                # . . . #
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if True:
        basic.show_string("\"Don't give in to hate. That leads to the Dark Side.\"")
        basic.show_string("\"You know, sometimes I amaze even myself.\"")
        basic.show_string("\"Let the past die. Kill it.\"")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_string("\"Welcome to the space world\"")
    basic.show_leds("""
        . # . # .
                . # . # .
                . # . # .
                # # . # #
                . # . # .
    """)
    basic.show_leds("""
        . . . . .
                . # # # .
                # . # . #
                # . # . #
                . # # # .
    """)
    basic.show_leds("""
        # # . . .
                # . # . .
                # . # . .
                # . # . .
                # # . . .
    """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    global index
    for index2 in range(3):
        music.play_tone(392, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.EIGHTH))
        music.play_tone(392, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.EIGHTH))
        music.play_tone(392, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.EIGHTH))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.play_tone(349, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.EIGHTH))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.EIGHTH))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.play_tone(349, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.EIGHTH))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.EIGHTH))
        music.play_tone(349, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.EIGHTH))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        index += 1
    music.stop_all_sounds()
basic.forever(on_forever)
