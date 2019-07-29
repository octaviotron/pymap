# pymap
Random Map Surface generator with Python

There was a need of having random maps for a game project, so I started to read theory and realize there are really wierd and complex math below it. I was too complicated for me so I decided to use very-very simple math calculations and very-very simple algorithm logics. That is how it works:

- One simple matrix(x,y) function creates a random matrix with X long and Y heigh, with values from 0 to 254
- One simple populate() functions iterates all matrix values and adds a random number in between all cells, keeping values into dots range
- The previous procedure repeats. The size of the starting random matrix gives the "variation" of the map and the amount of repetitions gives "smoothness" to the result.
- This is it. This method even uses only built-in python basic functions, only importing "random" module



