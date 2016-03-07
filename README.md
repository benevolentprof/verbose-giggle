# verbose-giggle
Mars Rover Demonstration Project

This project is my solution for a Mars Rover problem as given below. If I were solving this problem in practice,
my first step would be to Google for a similar problem and solution. But since this is a demonstration project,
I'll solve this from "scratch".

Usage: python mars_rover.py [count] [-h, --help]

Count is the number of rovers in the squad. Default is 1, if no count is given

Assumptions:

Coordinates refer to map grid squares and not point locations.

Mars is large and rovers are small, therefore, multiple rovers can be in the same grid square simultaneously.

Rovers move in sequence, not in parallel. I'm leaving the time dimension out for a few reasons. One, the instructions
are given in sequence. Two, it takes 4-24 minutes to transmit a message to Mars. Three, rovers normally move only
during the sidereal day and no data is provided on the Martian day cycle.

When rovers reach the edge of the plateau, they ignore instructions that would cause them to drive off.


================================
Problem Statement
=================================

A squad of robotic rovers are to be landed by NASA on a plateau on Mars.

This plateau, which is curiously rectangular, must be navigated by the rovers so that their on board cameras can
get a complete view of the surrounding terrain to send back to Earth.

A rover's position is represented by a combination of an x and y co-ordinates and a letter representing one of the
four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position
might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'.
'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot.

'M' means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

```
Input:
Configuration Input: The first line of input is the upper-right coordinates of the plateau,
the lower-left coordinates are assumed to be 0,0. Per Rover.
Test Input:8 4

Input 1: Landing co-ordinates for the Rover The position is made up of two integers and a
letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation.
Test Input:1 2 N

Input 2: Navigation instructions i.e a string containing ('L', 'R', 'M').
Test Input:LMLMLMLMM

Test Input:
Plateau:5 5
Rover1 Landing:1 2 N
Rover1 Instructions:LMLMLMLMM
Rover2 Landing:3 3 E
Rover2 Instructions:MMRMMRMRRM

Expected Output:
Rover1:1 3 N
Rover2:5 1 E
```

Task:
Develop a command line app that can take the various inputs from the command line and generate the desired outputs.

Expectations:

- App should be working
- Code should be modular and readable
- Unit tests

