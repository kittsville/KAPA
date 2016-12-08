# -*- coding: utf-8 -*-

"""
kapa.antigen

Represents parts of pathogens that can be recognised by antigens

"""

class Antibody:
    def __init__(self, shape):
        self.shape = shape
        self.affinity = float('inf')
        self.memfinity = float('inf')