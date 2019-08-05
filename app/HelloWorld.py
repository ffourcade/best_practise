# coding: utf-8
# @author : Jean Dupont
# @email : jean.dupont@email.com

############################################################
############################################################
##################    IMPORTS    ###########################
############################################################
############################################################

# First import built-in packages and "simple" packages
import os
import sys

# Then import packages to be renamed with alias
import numpy as np
import pandas as pd

# Then import particular classes, methods...
from sklearn.Ensemble import RandomTreeClassifier


############################################################
############################################################
###############    CLASSES/FUNCTIONS    ####################
############################################################
############################################################

# Classes name must be uppercase
class MyClass:
    def __init__(self, arg1, arg2):
        self.attribute_1 = arg1
        self.attribute_2 = arg2
    
    # Each method has to be documented
    # Methods name must be lowercase
    def first_method(self):
        """
        Get the instance's attributes
        :param self: the instance of type MyClass
        :return: the dictionnary of the instance's attributes
        """
        return {
            "A1" : self.attribute_1,
            "A2" : self.attribute_2,
        }
    
    @staticmethod
    def static_method(arg3, arg4):
        """
        Join two string separated by a single space
        :param arg3: first part of string to be joined
        :param arg4: second part of string to be joined
        :return: Concatenation of arg3 and arg4
        """
        assert isinstance(arg3, str), "First argument must be a string. Input value is type {}".format(type(arg3))
        assert isinstance(arg4, str), "First argument must be a string. Input value is type {}".format(type(arg4))
        var = " ".join([arg3, arg4])
        return var
    
    

def hello_world():
    """
    Prints the classic "Hello World !"
    """
    print("Hello World")
    
    
############################################################
############################################################
######################    SCRIPTS    #######################
############################################################
############################################################

if __name__ == "__main__":
    my_class = MyClass("Hello", "World")
    attributes = my_class.first_method()
    hello_world()
    print(my_class.static_method("Bonjour", "Monde"))
    