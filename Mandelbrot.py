from casioplot import *

top_left_pixel = -2 + 1j
bot_right_pixel = 1 - 1j
complex_range = bot_right_pixel - top_left_pixel
re_range = complex_range.real
im_range = complex_range.imag
re_offset = top_left_pixel.real
im_offset = top_left_pixel.imag


def is_mandel(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z ** 2 + c
        if abs(z) > 2:
            return i
    return max_iter


def colorize(iteration, max_iter):
    if iteration == max_iter:
        return (0, 0, 0)
    t = float(iteration) / max_iter
    r = int(9 * (1 - t) * t ** 3 * 255)
    g = int(15 * (1 - t) ** 2 * t ** 2 * 255)
    b = int(8.5 * (1 - t) ** 3 * t * 255)
    return (r, g, b)


def render(iterations):
    for x in range(384):
        real = x * re_range / 383 + re_offset
        for y in range(192):
            imag = y * im_range / 191 + im_offset
            cmplx = real + imag * 1j
            iteration = is_mandel(cmplx, iterations)
            color = colorize(iteration, iterations)
            set_pixel(x, y, color)
    show_screen()

print("Enter iterations:")
render(int(input("[>]")))
