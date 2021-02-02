def begin_rendering(group_id: str='default'):
    pass

def end_rendering():
    pass

def clear_screen(group_id: str='default'):
    pass

def clear_all_touched_render_groups():
    """
    Clears all render groups which have been drawn to using `begin_rendering(group_id)`.
    Note: This does not clear render groups created by e.g. other bots.
    """
    pass

def is_rendering():
    pass

def draw_line_2d(x1, y1, x2, y2, color):
    pass

def draw_polyline_2d(vectors, color):
    pass

def draw_line_3d(vec1, vec2, color):
    pass

def draw_polyline_3d(vectors, color):
    pass

def draw_line_2d_3d(x, y, vec, color):
    pass

def draw_rect_2d(x, y, width, height, filled, color):
    pass

def draw_rect_3d(vec, width, height, filled, color, centered=False):
    pass

def draw_string_2d(x, y, scale_x, scale_y, text, color):
    pass

def draw_string_3d(vec, scale_x, scale_y, text, color):
    pass

def create_color(alpha, red, green, blue):
    pass

def black():
    pass

def white():
    pass

def gray():
    pass

def grey():
    pass

def blue():
    pass

def red():
    pass

def green():
    pass

def lime():
    pass

def yellow():
    pass

def orange():
    pass

def cyan():
    pass

def pink():
    pass

def purple():
    pass

def teal():
    pass

def team_color(team=None, alt_color=False):
    """
    Returns the team color of the bot. Team 0: blue, team 1: orange, other: white
    :param team: Specify which team's color. If None, the associated bot's team color will be returned.
    :param alt_color: If True, returns the alternate team colors instead. Team 0: cyan, team 1: red, other: gray
    :return: a team color
    """
    pass

def get_rendering_manager(bot_index=0, bot_team=0):
    pass
