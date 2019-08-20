#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class NutritionInfo:
    '''Class plased info about proteins, carbs, fats in Instance'''
    def __init__(self, proteins, carbs, fats):
        '''initiate new instance'''
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats
    
    def __mul__(self, other):
        '''multiply the instance and repeat it other times
        other is str, int or __class__'''
        _new = self.__class__(self.proteins, self.carbs, self.fats)
        if type(other) == str or type(other) == int:
            _new.proteins = self.proteins * int(other)
            _new.carbs = self.carbs * int(other)
            _new.fats = self.fats * int(other)
        elif other.proteins or other.carbs or other.fats:
            _new.proteins = self.proteins * other.proteins
            _new.carbs = self.carbs * other.carbs
            _new.fats = self.fats * other.fats
        else:
            raise ValueError
#        print(type(self))
#        print(type(other)) 
#        print(self.proteins)
#        print(new.proteins)
#        print(id(self))
#        print(id(new))
        return _new
    
    def __add__(self, other):
        '''add (sum) other to the (with) instance
        other is str, int or __class__'''
        _new = self.__class__(self.proteins, self.carbs, self.fats)
#        print(type(other) == '__main__.NutritionInfo')
##        print(dir(inspect))
#        print(type(other))
#        print(dir(other))
#        print(other.__class__)
        if type(other) == str or type(other) == int:
            _new.proteins = self.proteins + int(other)
            _new.carbs = self.carbs + int(other)
            _new.fats = self.fats + int(other)
        elif other.proteins or other.carbs or other.fats:
            _new.proteins = self.proteins + other.proteins
            _new.carbs = self.carbs + other.carbs
            _new.fats = self.fats + other.fats
        else:
            raise ValueError
        
        return _new
    
    def __str__(self):
        return f"It has {self.proteins} proteins, {self.carbs} carbs and {self.fats} fats"
        
    def energy(self):
        return int(self.fats * 9 + (self.carbs + self.proteins) * 4.2)
    
    
    
if __name__ == "__main__":
    tvorog_9 = NutritionInfo(18, 3, 9)
    apple = NutritionInfo(0, 25, 0)
    print(tvorog_9)
    print(tvorog_9.energy())
    print(apple)
    print(apple.energy())
    breakfast = apple * 2 + tvorog_9
    print(breakfast)
    print(breakfast.energy())
    