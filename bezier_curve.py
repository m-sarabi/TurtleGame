def quad_bezier(p0, p1, p2, points):
    """
    quadratic bézier curve for three given control points
    source: https://en.wikipedia.org/wiki/B%C3%A9zier_curve#Quadratic_B%C3%A9zier_curves

    :param p0: Start point
    :param p1: Control point
    :param p2: End point
    :param points: how many points to return (including start and end points) + 1
    :return: a list of points on the curve
    """

    # calculate for a single axis
    def b_calc(a, b, c, t):
        return int(round(b + (1 - t) ** 2 * (a - b) + t ** 2 * (c - b), 0))

    curve_list = []

    for i in range(points + 1):
        ti = i / points
        curve_list.append([b_calc(p0[0], p1[0], p2[0], ti), b_calc(p0[1], p1[1], p2[1], ti)])
    return curve_list


def cubic_bezier(p0, p1, p2, p3, points):
    """
    Cubic bézier curve for four given control points
    source: https://en.wikipedia.org/wiki/B%C3%A9zier_curve#Cubic_B%C3%A9zier_curves

    :param p0: Start point
    :param p1: First control point
    :param p2: Second control point
    :param p3: End point
    :param points: how many points to return (including start and end points) + 1
    :return: a list of points on the curve
    """

    # calculate for a single axis
    def b_calc(a, b, c, d, t):
        return int(round((1 - t) ** 3 * a + 3 * (1 - t) ** 2 * t * b + 3 * (1 - t) * t ** 2 * c + t ** 3 * d, 0))

    curve_list = []

    for i in range(points + 1):
        ti = i / points
        curve_list.append([b_calc(p0[0], p1[0], p2[0], p3[0], ti), b_calc(p0[1], p1[1], p2[1], p3[1], ti)])
    return curve_list
