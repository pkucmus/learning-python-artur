def map_lengths(strings):
    return {i:len(i) for i in strings}

print map_lengths(['ala','ma','kota']) == {'ala':3, 'ma':2, 'kota':4}