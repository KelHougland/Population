import random
import rep_vars
import helpers
import village
import individual
import player

class building:  # buildings must have their special attributes, levels, dependencies, and available classes

    def __init__(self,init_buildtype):
        self.building=init_buildtype
        self.level=1
        self.lessons=[rep_vars.btypes[self.building]]

    def add_lesson(self,new_lesson):
        self.lessons.append(new_lesson)

    def get_test(self):
        return self.lessons

