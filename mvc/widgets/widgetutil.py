from math import pi as PI
from mvc.widgets import widgetset

def css_to_color(css_string):
    parts = (css_string[1:3], css_string[3:5], css_string[5:7])
    return tuple((int(value, 16) / 255.0) for value in parts)

def align(widget, xalign=0, yalign=0, xscale=0, yscale=0,
        top_pad=0, bottom_pad=0, left_pad=0, right_pad=0):
    """Create an alignment, then add widget to it and return the alignment.
    """
    alignment = widgetset.Alignment(xalign, yalign, xscale, yscale,
                          top_pad, bottom_pad, left_pad, right_pad)
    alignment.add(widget)
    return alignment

def align_center(widget, top_pad=0, bottom_pad=0, left_pad=0, right_pad=0):
    """Wrap a widget in an Alignment that will center it horizontally.
    """
    return align(widget, 0.5, 0, 0, 1,
            top_pad, bottom_pad, left_pad, right_pad)

def align_right(widget, top_pad=0, bottom_pad=0, left_pad=0, right_pad=0):
    """Wrap a widget in an Alignment that will align it left.
    """
    return align(widget, 1, 0, 0, 1, top_pad, bottom_pad, left_pad, right_pad)

def align_left(widget, top_pad=0, bottom_pad=0, left_pad=0, right_pad=0):
    """Wrap a widget in an Alignment that will align it right.
    """
    return align(widget, 0, 0, 0, 1, top_pad, bottom_pad, left_pad, right_pad)

def align_middle(widget, top_pad=0, bottom_pad=0, left_pad=0, right_pad=0):
    """Wrap a widget in an Alignment that will center it vertically.
    """
    return align(widget, 0, 0.5, 1, 0,
            top_pad, bottom_pad, left_pad, right_pad)

def align_top(widget, top_pad=0, bottom_pad=0, left_pad=0, right_pad=0):
    """Wrap a widget in an Alignment that will align to the top.
    """
    return align(widget, 0, 0, 1, 0, top_pad, bottom_pad, left_pad, right_pad)

def align_bottom(widget, top_pad=0, bottom_pad=0, left_pad=0, right_pad=0):
    """Wrap a widget in an Alignment that will align to the bottom.
    """
    return align(widget, 0, 1, 1, 0, top_pad, bottom_pad, left_pad, right_pad)

def pad(widget, top=0, bottom=0, left=0, right=0):
    """Wrap a widget in an Alignment that will pad it.
    """
    alignment = widgetset.Alignment(0, 0, 1, 1,
                          top, bottom, left, right)
    alignment.add(widget)
    return alignment

def circular_rect(context, x, y, width, height):
    """Make a path for a rectangle with the left/right side being circles.
    """
    radius = height / 2.0
    inner_width = width - height
    inner_y = y + radius
    inner_x1 = x + radius
    inner_x2 = inner_x1 + inner_width

    context.move_to(inner_x1, y)
    context.rel_line_to(inner_width, 0)
    context.arc(inner_x2, inner_y, radius, -PI/2, PI/2)
    context.rel_line_to(-inner_width, 0)
    context.arc(inner_x1, inner_y, radius, PI/2, -PI/2)

def circular_rect_negative(context, x, y, width, height):
    """The same path as ``circular_rect()``, but going counter clockwise.
    """
    radius = height / 2.0
    inner_width = width - height
    inner_y = y + radius
    inner_x1 = x + radius
    inner_x2 = inner_x1 + inner_width

    context.move_to(inner_x1, y)
    context.arc_negative(inner_x1, inner_y, radius, -PI/2, PI/2)
    context.rel_line_to(inner_width, 0)
    context.arc_negative(inner_x2, inner_y, radius, PI/2, -PI/2)
    context.rel_line_to(-inner_width, 0)

class Shadow(object):
    """Encapsulates all parameters required to draw shadows.
    """
    def __init__(self, color, opacity, offset, blur_radius):
        self.color = color
        self.opacity = opacity
        self.offset = offset
        self.blur_radius = blur_radius
