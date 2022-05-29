from abc import ABC, abstractmethod
from typing import List
from uuid import uuid4


class Object(ABC):

    def __init__(self):
        self.uid = uuid4().hex  # generating an id using a random number


class Updatable(ABC):

    @abstractmethod
    def update(self):
        pass


class Drawable(ABC):

    @abstractmethod
    def draw(self):
        pass


Objects = List[Object]
