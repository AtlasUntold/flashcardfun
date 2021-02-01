# flashcardfun
A small script I'm writing just for fun to store digital flashcards instead of using someone else's app

For my friend (or anyone who wants to be helpful):

The functionality of the module works as intended,
minus the following two issues:

So there are two issues I'm running into, I want to
allow a user to put all their terms and definitions in, one per 
line, and assign them to variables to call in my functions. So if
in "terms_defs.txt" they type out 20 terms and 20 definitions,
I want to create 20 variables and assign them. I'm thinking,
especially now that I'm typing this, that there's an easier way 
to do this.. such as looping through the file and looping through
one term and one definition at a time. So how might I do this?

The way I'm doing this is assigning them to a dict(flashcards) which is
comprised of variables representing the terms and definitions (T1: D1), and
then making a list of the terms from the dict (flashcard_list).


Next, I think I either found a fundamental problem with the way
I wrote my scripts, or found a gap in a knowledge that has me stuck.

If you take a look at lines 44-49, you'll see that I call on 
D1 and T1, but my initial intention was to use the variable 
(count) instead, such as D(count) or T(count), but I think I'm
already nesting too many elements and it's getting too complicated.

I think that the original solution can solve this problem, because
I can simple have one term variable and one definition variable,
assign the current line as I go through the txt file, and call on
that variable, removing the need to do the above.

Anyway, I hope this makes sense, and I hope you have notes for me!

