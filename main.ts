let index = 0
input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . # .
        . . # # .
        . # # # .
        . # # . .
        # . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . # # . .
        # # # # #
        . # . . .
        # . . . .
        `)
    basic.showLeds(`
        . . # . .
        . # # # .
        # # # # #
        . . . . .
        # . # . #
        `)
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        `)
    basic.showLeds(`
        . . # # #
        # . # . #
        # # # # #
        . . . # .
        . . # . #
        `)
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        # # # # #
        . . # . .
        `)
    basic.showLeds(`
        . . # . .
        . # # # .
        # . # . #
        # # # # #
        . . # . .
        `)
    basic.showLeds(`
        . # . # .
        # # # # #
        . # . # .
        # # # # #
        # . . . #
        `)
})
input.onButtonPressed(Button.B, function () {
    if (true) {
        basic.showString("\"Don't give in to hate. That leads to the Dark Side.\"")
        basic.showString("\"You know, sometimes I amaze even myself.\"")
        basic.showString("\"Let the past die. Kill it.\"")
    }
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("\"Welcome to the space world\"")
    basic.showLeds(`
        . # . # .
        . # . # .
        . # . # .
        # # . # #
        . # . # .
        `)
    basic.showLeds(`
        . . . . .
        . # # # .
        # . # . #
        # . # . #
        . # # # .
        `)
    basic.showLeds(`
        # # . . .
        # . # . .
        # . # . .
        # . # . .
        # # . . .
        `)
})
basic.forever(function () {
    for (let index2 = 0; index2 < 0; index2++) {
        music.playTone(392, music.beat(BeatFraction.Quarter))
        music.rest(music.beat(BeatFraction.Eighth))
        music.playTone(392, music.beat(BeatFraction.Quarter))
        music.rest(music.beat(BeatFraction.Eighth))
        music.playTone(392, music.beat(BeatFraction.Quarter))
        music.rest(music.beat(BeatFraction.Eighth))
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.playTone(392, music.beat(BeatFraction.Whole))
        music.playTone(392, music.beat(BeatFraction.Whole))
        music.playTone(349, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Eighth))
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Eighth))
        music.playTone(294, music.beat(BeatFraction.Whole))
        music.playTone(523, music.beat(BeatFraction.Whole))
        music.playTone(523, music.beat(BeatFraction.Whole))
        music.playTone(392, music.beat(BeatFraction.Whole))
        music.playTone(349, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Eighth))
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Eighth))
        music.playTone(349, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Eighth))
        music.playTone(294, music.beat(BeatFraction.Whole))
        music.playTone(294, music.beat(BeatFraction.Whole))
        index += 1
    }
    music.stopAllSounds()
})
