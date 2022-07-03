# To-do List:
+ [x] make the database
+ [x] get the messages into the code and store them in the database
+ [ ] traffic lights
+ [ ] verification if the vehicle can enter a street
  + [ ] traffic light
  + [ ] 
+ [ ] make various instances of the simulation
+ [ ] generate a new scenario when another stops
+ [ ] make the queries to get the data from the database
+ [ ] make the interface  with the analysis

# Simulator
+ will represent the *streets* and the *intersections* of a city
+ the graph containing streets (edges) and intersections (nodes) will be generated randomly at each execution of the program
+ it must notify it's state at each cycle
+ it must execute for a predefined time
+ when a simulation ends, a new one must be started

## Street
+ streets are edges of the graph
+ streets can be navigated in both directions
+ each street must have a max car capacity
+ The street length is randomized
+ the number of cycles needed to cross a street is based on car speed and street length


## Intersection
+ intersections are nodes of the graph
+ there are **terminal intersections**, which have just one street connected to them.
  + each terminal intersection adds a random number of cars to the simulation at each cycle;
+ each intersection must be controlled by a set of *traffic lights*

## Car
+ when a car reach a terminal intersection, it is removed from the simulation
+ a car can't change direction after entering a street
+ when a car passes a intersection, it's speed must vary in a random way
+ when a car enters a intersection, it must choose a random street to go to (except the one it is currently on)
+ a car can only enter a street if:
  + the street's max car capacity is not reached
  + it has gained exclusive access to the street (philosopher's dinner problem)


# Data Source
+ multiple simulation instances
