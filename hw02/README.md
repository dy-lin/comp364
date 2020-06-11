# Assignment 2: Conway's Game of Life
## DUE: Friday October 20, 2017 11:59 PM 

In this assignment, we're going to be writing a "game" that simulates a self propagating population of organisms known as "[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)".

In 1970, mathematician John Horton Conway wanted to find a set of simple rules that if applied to an environment would produce complex and self sustaining patterns.

He modeled the world as an _NxN_ grid where each cell in the grid can be either alive or dead (1 or 0).

The goal was to start with some initial grid where some cells are alive and some are dead, and then have the grid updated repetitively using these simple rules:

### Rules:

1. Any living cell that has **fewer than** 2 living neighbours dies in the next generation (as if by underpopulation).
1. Any living cell that has **exactly** 2 or 3 living neighbours lives in the next generation.
1. Any living cell that has **more** than 3 living neighbours dies (as if by overpopulation).
1. Any dead cell that has **exactly** 3 living neighbours comes back to life in the next generation (as if by reproduction).

So say we have an initial grid `G_initial` with some cells having value 0 (dead) and others having value 1 (alive). The goal is to come up with values for each entry in `G_next` by looking at each cell in `G_initial[i][j]` and seeing if it will be alive or dead in `G_next[i][j]`. Using the rules above we can always determine if a cell will be alive or dead in the next generation. Once we can do this, we can just repeat the procedure as many times as we want to simulate the evolution of our world.

Turns out that with these 4 simple rules Conway was able to simulate some very interesting patterns which have had a large impact on many fields such as biology, physics, computer science, mathematics, and philosophy. Conway was able to show that with a few simple rules and an initial state, complex patterns can emerge without any external intervention.

Here is a video of some interesting patterns that can emerge if you have the right starting state: https://www.youtube.com/watch?v=C2vgICfQawE&t=15s

You can also watch Conway himself talking about how he invented the game and how he is a bit tired of everyone associating him to only that: https://www.youtube.com/watch?v=R9Plq-D1gEk

And definitely read the [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) article.

#### Requirements

In this assignment we'll be working with the python package numpy, as well as two visualization packages so we can make cool animations. Since you are using anaconda this will be very easy to install. All you have to do is open your Terminal or Command Prompt and type in the following commands:

```
conda install numpy
conda install matplotlib
conda install -c conda-forge jsanimation
```

If this is not working, please Google it. If that doesn't work go to office hours and we will help you with the installation. Try this out as soon as possible.

**NOTA BENE:** This is a very well studied problem and you will find many examples online of other people's implementations of the game of life. It's perfectly okay to look at other sources for inspiration but keep in mind that we do run plagiarism checks so make sure that the code comes from you in the end.
