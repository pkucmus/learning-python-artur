def bootle_song():
    result = ''
    bootles = 99

    while bootles:
        result += """{0} bottles of beer on the wall, {0} bottles of beer.
Take one down, pass it around, {1} bottles of beer on the wall.
                """.format(bootles, bootles-1)
        bootles -= 1

    return result

print bootle_song()