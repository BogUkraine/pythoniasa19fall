"""
Assignment 1-A
==============

Update the Python script below to make it more compact and readable; use at least variables and f-strings.
For those who are already familiar with Python – write the best code you can to conform to the Zen of Python.

"""

poem = '''
This is the house that Jack built.

This is the malt 
That lay in the house that Jack built.

This is the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cow with the crumpled horn, 
That toss'd the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the maiden all forlorn, 
That milk'd the cow with the crumpled horn, 
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the priest all shaven and shorn, 
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milked the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cock that crow'd in the morn, 
That waked the priest all shaven and shorn, 
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn, 
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the farmer sowing his corn, 
That kept the cock that crow'd in the morn, 
That waked the priest all shaven and shorn,
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That killed the rat, 
That ate the malt 
That lay in the house that Jack built.
'''
array = [['the house that Jack built', 'lay in the house that Jack built'],
         ['the malt', 'ate the malt'],
         ['the rat', 'kill\'d the rat'],
         ['the cat', 'worried the cat'],
         ['the dog', 'toss\'d the dog'],
         ['the cow with the crumpled horn', 'milk\'d the cow with the crumpled horn'],
         ['the maiden all forlorn', 'kissed the maiden all forlorn'],
         ['the man all tatter\'d and torn','married the man all tatter\'d and torn'],
         ['the priest all shaven and shorn','waked the priest all shaven and shorn'],
         ['the cock that crow\'d in the morn','kept the cock that crow\'d in the morn'],
         ['the farmer sowing his corn','']]

for i in range (len(array)):
    for j in range(i+1):
        if j == 0:
            print('This is ' + array[i-j][0])
        else:
            print('That ' + array[i-j][1])
    print()

