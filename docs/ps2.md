# Robot Cleaning Simulations

I import the classes from ps2.py, including Position, RectangularRoom, Robot (and its subclasses StandardRobot and RandomWalkRobot). Nothing too complex here, just a hacky way of dealing with storing robot positions in a room represented as a NumPy Array.

## Classes in Action

```python

import ps2

from ps2_verify_movement37 import testRobotMovement
import ps2_visualize

loc = ps2.Position(2, 2)
bad_loc = ps2.Position(10, 10)
room = ps2.RectangularRoom(6, 8)
print(room.isPositionInRoom(loc))
print(room.isPositionInRoom(bad_loc))
```

The robot is initialized in the 6 x 8 room with a set movement speed and at a random location. Upon initialization the tile it is on is marked as clean (so it starts out with one clean tile before moving). Then, moving again, it updates the position and the number of cleaned tiles.

```python
robot = ps2.StandardRobot(room, 1)
print(robot.getRobotPosition())
print(robot.room.getNumCleanedTiles())
robot.updatePositionAndClean()
print(robot.getRobotPosition())
print(robot.room.getNumCleanedTiles())
```

The runSimulation function has args of the number of robots, speed, width, height, clean threshold and number of trials. The robots are initialized and trials are run until a set percent of the room has been covered by the robot, counting the number of steps taken, and returning the average of these steps over a number of trials. Here, we see that a randomly walking robot will take much longer than a straight "bouncing" robot to clean a room.

```python
print(ps2.runSimulation(1, 1.0, 10, 10, 0.9, 30, ps2.StandardRobot))
print(ps2.runSimulation(1, 1.0, 10, 10, 0.9, 30, ps2.RandomWalkRobot))
```

Finally, we can run these trials for different combinations of the number of robots, or the aspect ratio (ratio of height to width), and see how many time steps it takes to clean the room.

```python

style.use('fivethirtyeight')

ps2.showPlot1("Steps to Clean for different numbers of robots", "Number Robots", "Steps to clean 80% of Room")
ps2.showPlot2("Steps to Clean for different room shapes (aspect ratio)", "Ratio of Width to Height", "Steps to clean 80% of Room")
```

## Appendix

Print out RectangularRoom, Robot, StandardRobot, RandomWalkRobot, RunSimulation classes

### RectangularRoom

```python
class RectangularRoom(object):
    """

    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """

    def __init__(self, width, height):
        # Create array to represent room, with all False values
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=bool)

        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """

    def cleanTileAtPosition(self, pos):
        (c, r) = math.floor(pos.getX()), math.floor(pos.getY())
        # adjust position which begins at 1, 1, to grid which begins at 0, 0
        # This is pretty hacky, but for some reason a position that passed the isPositionInRoom is out of bounds..
        if (0  0)
        """
        # A position object is stored as self attribute
        self.room = room
        self.pos = self.room.getRandomPosition()
        self.room.cleanTileAtPosition(self.pos)
        self.angle = randint(0, 359)
        self.speed = speed

    def getRobotPosition(self):
        """
        Return the position of the robot.
        returns: a Position object giving the robot's position.
        """
        return self.pos

    def getRobotDirection(self):
        """
        Return the direction of the robot.
        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.angle

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.
        position: a Position object.
        """
        self.pos = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.
        direction: integer representing an angle in degrees
        """
        self.angle = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        been cleaned.
        """
        raise NotImplementedError # don't change this!
```

## Summary

This problem set demonstrates:

1. **Object-Oriented Programming**: Creating classes for Room and Robot
2. **Simulation**: Running multiple trials to analyze robot behavior
3. **Data Analysis**: Comparing different robot strategies
4. **Visualization**: Plotting results using matplotlib
5. **Algorithm Design**: Implementing different movement strategies

The key insight is that systematic movement patterns (like StandardRobot) are much more efficient than random movement (RandomWalkRobot) for cleaning tasks.
