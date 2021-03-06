# 6.00.2x Problem Set 2: Simulating robots

import math
from random import randint

import ps2_visualize
import pylab

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.5:
#from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5 

# For Python 3.6:
# from ps2_verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6

from ps2_verify_movement37 import testRobotMovement

# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1

import os
from random import randint
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np


class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
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
        if (0 <= pos.getY() < self.height) & (0 <= pos.getX() < self.width):
            self.grid[r - 1, c - 1] = True

        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # raise NotImplementedError

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.
        Assumes that (m, n) represents a valid tile inside the room.

        m and n: integers
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.grid[n - 1, m - 1]
        # raise NotImplementedError
    
    def getNumTiles(self):
        return self.grid.shape[0] * self.grid.shape[1]
        # Return the total number of tiles in the room, returns: an integer
        # raise NotImplementedError

    def getNumCleanedTiles(self):
        return sum(sum(self.grid))
        # Return the total number of clean tiles in the room.
        # raise NotImplementedError

    def getRandomPosition(self):
        # Return a random position inside the room, returns: a Position object.
        # second element of shape is number of columns, representing x distance. adjust position
        # by subtracting one since that is done when adjusting math position to matrix position
        rand_x, rand_y = randint(1, self.grid.shape[1]), randint(1, self.grid.shape[1])
        return Position(rand_x - 1, rand_y - 1)
        # raise NotImplementedError

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if (0 <= pos.getY() < self.height) & (0 <= pos.getX() < self.width):
            return True
        else:
            return False
        # raise NotImplementedError


# loc = Position(2, 2)
#
# t = RectangularRoom(6, 8)
# print(t.isPositionInRoom(Position(6.0, 8.0)))


# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
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

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        has_moved = False
        while not has_moved:
            new = self.pos.getNewPosition(self.angle, self.speed)
            if self.room.isPositionInRoom(new):
                self.setRobotPosition(new)
                self.room.cleanTileAtPosition(self.pos)
                has_moved = True
            else:
                self.angle = randint(0, 359)


# Uncomment this line to see your implementation of StandardRobot in action!
# testRobotMovement(StandardRobot, RectangularRoom)

# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, toprint = False):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """

    results = [None] * num_trials

    # Run number of trials and keep track with results list
    for trial in range(0, num_trials):
        my_room = RectangularRoom(width, height)
        my_bots = {}
        
        # Initialize robots
        for i in range(1, num_robots + 1):
            my_bots[i] = robot_type(my_room, speed)

        steps = 0
        while my_room.getNumCleanedTiles()/my_room.getNumTiles() < min_coverage:
            for bot in my_bots.values():
                bot.room = my_room
                bot.updatePositionAndClean()
                my_room = bot.room
            steps += 1
            if ((toprint) & (steps%100 == 0)):
                print("Took Step ", steps)
        results[trial] = steps
        if toprint:
            print("Finished Trial: ", trial)

    return sum(results)/len(results)
# Uncomment this line to see how much your simulation takes on average
# print(runSimulation(1, 1.0, 10, 10, 0.9, 30, StandardRobot))



# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        has_moved = False
        while not has_moved:
            self.angle = randint(0, 359)
            new = self.pos.getNewPosition(self.angle, self.speed)
            if self.room.isPositionInRoom(new):
                self.setRobotPosition(new)
                self.room.cleanTileAtPosition(self.pos)
                has_moved = True

# testRobotMovement(StandardRobot, RectangularRoom)
# testRobotMovement(RandomWalkRobot, RectangularRoom)

def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()



    
def showPlot2(title, x_label, y_label):

    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in range(10, 18):
    #for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot, False))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot, False))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 6
# NOTE: If you are running the simulation, you will have to close it 
# before the plot will show up.

#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
# showPlot1("Steps to Clean for different numbers of robots", "Number Robots", "Steps to clean 80% of Room")

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#showPlot2("Steps to Clean for different room shapes (aspect ratio)",
 #      "Ratio of Width to Height", "Steps to clean 80% of Room")

