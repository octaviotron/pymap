# pymap
Random Map Surface generator with Python

There was a need of having random maps for a game project, so I started to read theory and realize there are really wierd and complex math below it. I was too complicated for me so I decided to use very-very simple math calculations and very-very simple algorithm logics. 

This code uses only built-in Python functions, only "random" is imported so so no extra modules needs to be installed.

That is how it works:

1) One simple matrix(x,y) function creates a random matrix with X long and Y heigh, with values from 0 to 254. Note the numbers in yellow.

![first matrix](https://user-images.githubusercontent.com/37819159/62019546-608eff00-b18d-11e9-9a5b-007f45399062.png)

2) One simple populate() functions iterates all matrix values and adds a random number in between all cells, keeping values into dots range (blue numbers). Note "12" and "90" values are calculated in row (horizontal) processing. For more complex generation "diamond square algorithm" can be used (see https://en.wikipedia.org/wiki/Diamond-square_algorithm)

![second matrix](https://user-images.githubusercontent.com/37819159/62019547-608eff00-b18d-11e9-8d5f-162bbfed882c.png)

3) The previous procedure repeats. 

![third matrix](https://user-images.githubusercontent.com/37819159/62019548-608eff00-b18d-11e9-9c81-7bde3b8930f6.png)

4) This is it. This method uses only built-in python basic functions, just needed to import "random" module but who knows... maybe in the future I make a simple-too-random-number-generation function ;-)

The size of the starting random matrix gives the "variation" of the map: bigger starting matrix generates more different zones, if the starting matrix is small, there will be less different terrain zones.

The amount of repetitions gives "smoothness" to the result.


TODO: update the code to Python3



