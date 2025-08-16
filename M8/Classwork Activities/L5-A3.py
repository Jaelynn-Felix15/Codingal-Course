#It refers to the process of hiding complex implemetation details and exposing only the essential features of an object or system.
#import necessary packages
from abc import ABC, abstractmethod
# create a base class 
class Animal(ABC):

    # abstract method
    # should be implemeneted by all sub-classes