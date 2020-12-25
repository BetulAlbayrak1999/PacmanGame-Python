from OpenGL import GL as gl

COIN_COLOR = 0.9, 0.9, 0        # color of coin
SUPER_COIN_COLOR = 0.9, 0.3, 0  # color of super coin

FLOOR_COLOR = 0.15, 0.15, 0.15  # color of floor
CELING_COLOR = 0.1, 0.4, 0.9        # color of celing

CELLING_LEVEL = 0    # height of celling
FLOOR_LEVEL = -1.0  # height of floor

MOVES = "NSWE"
OPPOSITE_MOVES = {
    "N": "S",
    "S": "N",
    "W": "E",
    "E": "W"
}


def set_color(color):
    """Function sets the color."""
    r, g, b = color
    gl.glColor3f(r, g, b)