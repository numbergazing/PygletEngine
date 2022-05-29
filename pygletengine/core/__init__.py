from abc import ABC, abstractmethod
from typing import List
from uuid import uuid4

import pyglet

from core.logging import engine_log


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


class Engine:

    def _startup(self):

        engine_log.info("Engine is firing up.")

        self.objects = []
        self.window = pyglet.window.Window()

        engine_log.info("Startup is finished.")

        pyglet.app.run()

    def __init__(self):

        self.objects: Objects
        self.window: pyglet.window.Window

        self._startup()

    def shutdown(self):

        self.window.close()
        del self.objects

        engine_log.info("Engine is shutting down.")
