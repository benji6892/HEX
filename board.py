from tkinter import Canvas

sqrt3 = 1.7320508075688772


def draw_board(window, size: int, colour1: str, colour2: str):
    screen_height = window.winfo_screenheight() * 0.8
    screen_width = window.winfo_screenwidth() * 0.8
    radius, x0, y0, half_diagonal = compute_parameters(size, screen_width, screen_height)
    board = Canvas(window, height=screen_height, width=screen_width)
    draw_background_triangles(board, half_diagonal, x0, y0, colour1, colour2)
    draw_hexagons(board, size, radius, x0, y0)
    board.pack()
    return board


def compute_parameters(size, screen_width, screen_height):
    padding = 50
    const = (3 * (size - 1)/2 + 4)
    radius = min((screen_width - 2*padding)/sqrt3, screen_height - 2*padding)/const
    half_diagonal = const * radius
    x0 = (screen_width - sqrt3 * const * radius) / 2
    y0 = (screen_height - const * radius) / 2
    return radius, x0, y0, half_diagonal


def draw_background_triangles(board: Canvas, a, x0, y0, colour1, colour2):

    top_left = [x0, y0]
    bottom_left = [x0 + a / sqrt3, y0 + a]
    bottom_right = [x0 + a * sqrt3, y0 + a]
    top_right = [2 * a / sqrt3 + x0, y0]
    center = [x0 + a * sqrt3 / 2, y0 + a / 2]

    board.create_polygon(top_left + top_right + center, fill=colour1, width='1m', outline='#000000')
    board.create_polygon(top_left + bottom_left + center, fill=colour2, width='1m', outline='#000000')
    board.create_polygon(bottom_left + bottom_right + center, fill=colour1, width='1m', outline='#000000')
    board.create_polygon(bottom_right + top_right + center, fill=colour2, width='1m', outline='#000000')


def draw_hexagons(board: Canvas, size: int, radius, x0, y0):
    x1 = x0 + radius * 2 * sqrt3
    y1 = y0 + radius * 2
    for horizontal in range(0, size):
        for diagonal in range(0, size):
            x = x1 + radius * (sqrt3 * horizontal + (sqrt3 / 2) * diagonal)
            y = y1 + radius * ((3 / 2) * diagonal)
            draw_hexagon(x, y, board, radius, f'{horizontal + 1}.{diagonal + 1}')


def draw_hexagon(x: float, y: float, board: Canvas, radius, tag: str):
    base_points = [(0, 1), (-sqrt3/2, 1/2), (-sqrt3/2, -1/2),
                   (0, -1), (sqrt3/2, -1/2), (sqrt3/2, 1/2)]
    summits = []
    for point in base_points:
        summits.append(point[0] * radius + x)
        summits.append(point[1] * radius + y)
    board.create_polygon(summits, fill='#edb879', outline='#000000', width='1m', tags=tag)
