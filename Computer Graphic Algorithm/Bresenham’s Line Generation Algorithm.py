# Python 3 program for Bresenham’s Line Generation
# Assumptions :
# 1) Line is drawn from left to right.
# 2) x1 < x2 and y1 < y2
# 3) Slope of the line is between 0 and 1.
# We draw a line from lower left to upper
# right.


# function for line generation
def bresenham(x1, y1, x2, y2):
    m_new = 2 * (y2 - y1)
    slope_error_new = m_new - (x2 - x1)

    y = y1
    for x in range(x1, x2 + 1):

        print("(", x, ",", y, ")\n")

        # Add slope to increment angle formed
        slope_error_new = slope_error_new + m_new

        # Slope error reached limit, time to
        # increment y and update slope error.
        if (slope_error_new >= 0):
            y = y + 1
            slope_error_new = slope_error_new - 2 * (x2 - x1)


# driver function
if __name__ == '__main__':
    x1 = 10
    y1 = 18
    x2 = 15
    y2 = 20
    bresenham(x1, y1, x2, y2)