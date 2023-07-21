# the lay down
This is a script to test for power-of-two solutions to the Moser's Circle Theorem. Trivial solutions are 1, 2, 3, 4, 5, and 10, but nothing above that for aaaages.
On my laptop, I was able to check to some 500 million iterations, but I'm sure someone will check more.
# how it works
Using the math module for python, the script runs each number into a function that matches the theorem [(here's a good video if you have no idea what I'm talking about)](https://www.youtube.com/watch?v=YtkIWDE36qU) and then checks if its base two logarithm is a whole number (so it's a power of two). Additionally, every power of two iterations, it will send out a failure message so you know kind of where it's at.
# how to run
If you have python installed, you should be able to double-click on this file. I assume it works about the same pretty far back in the version history, but it was written for 3.10, so keep that in mind.
If you don't have python installed, [go here.](https://www.python.org/downloads/)
- Matthew
