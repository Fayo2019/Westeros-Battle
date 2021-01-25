# Westeros-Battle
A challenge set up by the website Hackajob

THE TASK:

It was a techy reinactment of Game of Thrones (which I hadn't actually seen the end of :,() where the sevwn kingdoms army fought the white walkers. Each side had 2 kinds of fighters with different (attack, defense) stats.

Seven Kingdoms Army:

1 dragon = (600,600)
1 infantry = (2,2) and the initial figure is hardcoded to 5000 in the challenge

White Walker army:

1 White lord = (50,100)
1 White walker = (1,3) and the initial figure is hardcoded to 10000 in the challenge

Expected inputs were no_of_dragons, no_of_white_lords and first attacking army
The expected output was a string in the format "a|b" where a is the winning side and b is the number of turns taken.

The rule was if any unit has any attack points remaining for that turn they must use them if, and any enemy not killed regains their defense (Which I think of more as health) for the next turn.
