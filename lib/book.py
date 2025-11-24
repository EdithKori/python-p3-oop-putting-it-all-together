#!/usr/bin/env python3

class Book:
    def __init__(self, title='', page_count=0):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 100:
            self._title = value.title()
        else:
            raise ValueError("Title must be a string between 1 and 100 characters.")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int) and value > 0:
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        
        