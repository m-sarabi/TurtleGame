def quad_bezier(p0, p1, p2, points):
    """
    quadratic bézier curve for three given control points

    :param p0: first control point
    :param p1: middle control point
    :param p2: last control point
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
