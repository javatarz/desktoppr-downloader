__author__ = 'karunab'


class Resolution:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.aspect_ratio = width * 1.0 / height

    @staticmethod
    def from_tuple((width, height)):
        return Resolution(width, height)

    def __str__(self):
        return "%d x %d (%f)" % (self.width, self.height, self.aspect_ratio)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __gt__(self, other):
        return self.aspect_ratio == other.aspect_ratio and self.width >= other.width

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return not self.__gt__(other)

    def __lt__(self, other):
        return not self.__ge__(other)