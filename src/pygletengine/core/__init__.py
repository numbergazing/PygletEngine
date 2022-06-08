from abc import ABC, abstractmethod
from typing import List
from uuid import uuid4

import pyglet

from pygletengine.core.logging import engine_log


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


Objects = List[Object]


class EngineMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class Engine(metaclass=EngineMeta):

    def __init__(self):

        self.objects: Objects
        self._viewport: _Viewport

        engine_log.info("Engine is firing up.")

        self.objects = []
        self._viewport = None

    def startup(self):

        self._viewport = _Viewport()

        engine_log.info("Startup is finished.")

        pyglet.app.run()

    def shutdown(self):

        self._viewport.close()
        del self.objects

        engine_log.info("Engine is shutting down.")

    def add_objects(self, *objs: List[Object]):
        self.objects.extend(*objs)

    def remove_objects(self, *uids: List[str]):
        objs_to_delete = [obj for obj in self.objects if obj.uid in uids]
        for obj in objs_to_delete:
            del obj


class _Viewport(pyglet.window.Window):

    def __init__(self):
        super(_Viewport, self).__init__()
        self._engine = Engine()

    def on_draw(self):
        self.clear()
        for obj in self._engine.objects:
            if issubclass(type(obj), Drawable):
                obj.draw()
