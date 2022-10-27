from operator import add
from functools import partial


class Color:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'
    MIN_LEVEL = 0
    MAX_LEVEL = 255

    def __init__(self, red_level: int, green_level: int, blue_level: int):
        self._validate_level(red_level)
        self._validate_level(green_level)
        self._validate_level(blue_level)
        self.rgb = (red_level, green_level, blue_level)

    def _validate_level(self, level):
        if level > self.MAX_LEVEL or level < self.MIN_LEVEL:
            raise ValueError(f'levels should be in range [{self.MIN_LEVEL},{self.MAX_LEVEL}]')

    def __repr__(self):
        return f'{self.START};{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}{self.MOD}●{self.END}{self.MOD}'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.rgb == other.rgb
        return False

    def __add__(self, other):
        new_rgb = self.__class__(*map(add, self.rgb, other.rgb))
        return new_rgb

    def __hash__(self):
        return hash(self.rgb)

    def __rmul__(self, contrast):
        return self.__class__(*map(partial(self._change_contrast, contrast), self.rgb))

    def __mul__(self, contrast):
        return self.__class__(*map(partial(self._change_contrast, contrast), self.rgb))

    def _change_contrast(self, contrast, level):
        cl = -256 * (1 - contrast)
        f = 259 * (cl + 255) / (255 * (259 - cl))
        return int(f * (level - 128) + 128)


if __name__ == '__main__':
    dot = Color(255, 0, 0)
    print(dot)
    a = Color(255, 0, 0)
    b = Color(0, 122, 0)
    print(a + b)
    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(color_list)
    print(set(color_list))
    print(a * 0.5)
