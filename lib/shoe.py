#!/usr/bin/env python3

APPROVED_BRANDS = ["Nike", "Adidas", "Puma", "Reebok"]

class Shoe:
    def __init__(self, brand='', size=0, color=''):
        self.brand = brand
        self.size = size
        self.color = color

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if value in APPROVED_BRANDS:
            self._brand = value
        else:
            print("brand must be in the list of approved brands")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int) and 1 <= value <= 20:
            self._size = value
        else:
            print("size must be an integer")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 30:
            self._color = value.title()
        else:
            print("color must be a string")

    def put_on(self):
        print(f"Putting on your {self.color} {self.brand} shoes. Ready to go!")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
