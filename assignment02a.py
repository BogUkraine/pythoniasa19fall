"""
Assignment 2-A
==============

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""

def poem():
    array = [['the house that Jack built.', 'lay in the house that Jack built.'],
             ['the malt', 'ate the malt'],
             ['the rat,', 'killed the rat,'],
             ['the cat,', 'worried the cat,'],
             ['the dog,', 'tossed the dog,'],
             ['the cow with the crumpled horn,', 'milked the cow with the crumpled horn,'],
             ['the maiden all forlorn,', 'kissed the maiden all forlorn,'],
             ['the man all tattered and torn,','married the man all tattered and torn,'],
             ['the priest all shaven and shorn,','waked the priest all shaven and shorn,'],
             ['the cock that crowed in the morn,','kept the cock that crowed in the morn,'],
             ['the farmer sowing his corn,','']]

    res = ''

    for i in range (len(array)):
        for j in range(i+1):
            if j == 0:
                res += 'This is ' + array[i-j][0]
            else:
                res += 'That ' + array[i-j][1]
            res += '\n'
        res += '\n'
    return res[:-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
