def equilateral(sides):
    return sides[0] == sides[1] == sides[2] if 0 not in sides else False



def isosceles(sides):
    sides.sort()
    if sides[0] + sides[1] >= sides[2]:
        return sides[0] == sides[1] or sides[1] == sides[2]
    return False


def scalene(sides):
    sides.sort()
    if sides[0] + sides[1] >= sides[2]:
        return not (sides[0] == sides[1] or sides[1] == sides[2])
    return False
