import casioplot

Screen_X = 384
Screen_Y = 192


def draw_line(x1, y1, x2, y2, color=(0, 0, 0)):
    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    steep = abs(y2 - y1) > abs(x2 - x1)
    if steep:
        x1, y1, x2, y2 = y1, x1, y2, x2
    if x1 > x2:
        x1, x2, y1, y2 = x2, x1, y2, y1

    dx, dy = x2 - x1, y2 - y1
    error = dx / 2.0
    ystep = 1 if y1 < y2 else -1
    y = int(y1)
    points = []
    for x in range(int(x1), int(x2) + 1):
        coord = (y, x) if steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    # Draw the points
    for point in points:
        casioplot.set_pixel(point[0], point[1], color)


def graph_line(x1, y1, x2, y2, color=(0, 0, 0)):
    x1 = (Screen_X / 2) + (x1 * 16)
    x2 = (Screen_X / 2) + (x2 * 16)
    y1 = (Screen_Y / 2) - (y1 * 16)
    y2 = (Screen_Y / 2) - (y2 * 16)
    draw_line(x1, y1, x2, y2, color)


def plot_circle(x, y, color, radius):
    outline_radius = radius + 1

    for dx in range(-outline_radius, outline_radius + 1):
        for dy in range(-outline_radius, outline_radius + 1):
            if dx * dx + dy * dy <= outline_radius * outline_radius:
                casioplot.set_pixel(x + dx, y + dy, (255, 255, 255))

    for dx in range(-radius, radius + 1):
        for dy in range(-radius, radius + 1):
            if dx * dx + dy * dy <= radius * radius:
                casioplot.set_pixel(x + dx, y + dy, color)


def plot_point(x, y, color, radius):
    x = (Screen_X / 2) + (x * 16)
    y = (Screen_Y / 2) + (y * 16)
    plot_circle(x, y, color, radius)


def graph_function(equation, samplerate=100):
    jump = 24 / samplerate
    x = -12
    y = equation(-12)
    for _ in range(int(24 / jump)):
        dx = x + jump
        dy = equation(dx)
        graph_line(dx, dy, x, y)
        x, y = dx, dy


def InitGraph(sublines=True):
    Initstep = 16
    if sublines:
        for i in range(0, Screen_Y, Initstep):
            draw_line(0, i, Screen_X, i, color=(170, 170, 170))
        for i in range(0, Screen_X, Initstep):
            draw_line(i, 0, i, Screen_Y, color=(170, 170, 170))
    draw_line(0, Screen_Y // 2, Screen_X, Screen_Y // 2, color=(0, 0, 0))
    draw_line(Screen_X // 2, 0, Screen_X // 2, Screen_Y, color=(0, 0, 0))
