"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Jason Ims.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    length = abs(rectangle.corner_1.x - rectangle.corner_2.x)
    height = abs(rectangle.corner_1.y - rectangle.corner_2.y)
    for k in range(n):
        for i in range(k+1):
            pt1 = (rectangle.corner_1.x + (i * length))
            pt2 = (rectangle.corner_2.x + (i * length))
            row = rg.Rectangle(rg.Point(pt1,rectangle.corner_1.y),rg.Point(pt2,rectangle.corner_2.y))
            row.attach_to(window)
            window.render()
        rectangle.corner_1.x = rectangle.corner_1.x - length/2
        rectangle.corner_2.x = rectangle.corner_2.x - length/2
        rectangle.corner_2.y = rectangle.corner_2.y - height
        rectangle.corner_1.y = rectangle.corner_1.y - height

    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # -------------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # -------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
