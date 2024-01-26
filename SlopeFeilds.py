import casioplot
from CasioGraph import *
from math import *

Screen_X = 384
Screen_Y = 192
YSTEPS = 16
XSTEPS = 16
LINE_LEN = 1


# Function to render the slope field
def RenderSlope(equ):
    x_jump = (Screen_X / (XSTEPS * 16))
    y_jump = (Screen_Y / (YSTEPS * 16))
    y = (Screen_Y / 32) - y_jump / 2
    for y_cord in range(YSTEPS):
        # O(n^2) sad
        x = -(Screen_X / 32) + x_jump / 2
        for x_cord in range(XSTEPS):
            delta = equ(x, y)
            # trig to calculate the angle of the slope so all the lines are the same length
            angle = atan(delta)
            dx = cos(angle) * LINE_LEN / 2
            dy = sin(angle) * LINE_LEN / 2

            x1 = x - dx
            y1 = y - dy
            x2 = x + dx
            y2 = y + dy

            # draw the line
            graph_line(x1, y1, x2, y2, color=(255, 0, 0))
            x += x_jump
        y -= y_jump


def render_line(equ, point):
    xf, yf = point
    xb, yb = point
    x_min, x_max = -12, 12
    y_lower_bound, y_upper_bound = -6, 6
    max_delta_y = 4
    min_sample_rate = 0.01
    max_sample_rate = 0.1

    while xf <= x_max:
        slope_f = equ(xf, yf)
        adaptive_sample_rate = max(min_sample_rate,
                                   min(max_sample_rate, 1 / abs(slope_f) if slope_f != 0 else max_sample_rate))
        dxf, dyf = xf + adaptive_sample_rate, yf + slope_f * adaptive_sample_rate
        if abs(dyf - yf) > max_delta_y:
            dyf = yf + max_delta_y * (-1 if slope_f < 0 else 1)
        dyf = max(min(dyf, y_upper_bound), y_lower_bound)
        graph_line(xf, yf, dxf, dyf)
        xf, yf = dxf, dyf

    while xb >= x_min:
        slope_b = equ(xb, yb)
        adaptive_sample_rate = max(min_sample_rate,
                                   min(max_sample_rate, 1 / abs(slope_b) if slope_b != 0 else max_sample_rate))
        dxb, dyb = xb - adaptive_sample_rate, yb - slope_b * adaptive_sample_rate
        # stability and boundary checks
        if abs(dyb - yb) > max_delta_y:
            dyb = yb + max_delta_y * (-1 if slope_b < 0 else 1)
        dyb = max(min(dyb, y_upper_bound), y_lower_bound)
        graph_line(xb, yb, dxb, dyb)
        xb, yb = dxb, dyb


# Main function to display the graph
def main():
    InitGraph(sublines=False)
    print("""1). Slope Fields
2). Point Slope Filed
3). Settings""")
    action = input("[>]")

    if action == "1":
        equation = input("Enter dy/dx:").replace("^", "**")
        dydx = eval("lambda x,y: " + equation)
        RenderSlope(dydx)
        casioplot.show_screen()

    if action == "2":
        equation = input("Enter dy/dx:").replace("^", "**")
        point = eval(input("Enter (x,y):"))
        dydx = eval("lambda x,y: " + equation)
        RenderSlope(dydx)
        render_line(dydx, point)
        casioplot.show_screen()

main()
