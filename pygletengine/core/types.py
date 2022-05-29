from abc import ABC, abstractmethod
from typing import List
from uuid import uuid4


class Object(ABC):

    def __init__(self):
        self.uid = uuid4().hex  # generating an id using a random number


class Updatable(ABC):

    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class Drawable(ABC):

    @abstractmethod
    def draw(self, *args, **kwargs):
        pass


class Vertex2D(Object, Updatable, Drawable):

    def __init__(self, x: int = 0, y: int = 0):
        super(Object).__init__()
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pass


Objects = List[Object]
