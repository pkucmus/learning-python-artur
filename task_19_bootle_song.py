def bootle_song():
    bootles = 99

    while bootles:
        print   """{0} bottles of beer on the wall, {0} bottles of beer.
Take one down, pass it around, {1} bottles of beer on the wall.
                """.format(bootles, bootles-1)
        bootles -= 1

bootle_song()