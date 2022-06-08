from typing import List

import pyglet

from pygletengine.core.logging import engine_log
from pygletengine.core.types import Objects, Object, Drawable


class EngineWindow(pyglet.window.Window):

    def __init__(self, engine):
        super(EngineWindow, self).__init__()
        self.engine = engine

    def on_draw(self):
        self.clear()
        for obj in self.engine.objects:
            if issubclass(type(obj), Drawable):
                obj.draw()


class Engine:

    def __init__(self):

        self.objects: Objects
        self.window: EngineWindow

        engine_log.info("Engine is firing up.")

        self.objects = []
        self.window = None

    def startup(self):

        self.window = EngineWindow(self)

        engine_log.info("Startup is finished.")

        pyglet.app.run()

    def shutdown(self):

        self.window.close()
        del self.objects

        engine_log.info("Engine is shutting down.")

    def add_objects(self, *objs: List[Object]):
        self.objects.extend(*objs)

    def remove_objects(self, *uids: List[str]):
        objs_to_delete = [obj for obj in self.objects if obj.uid in uids]
        for obj in objs_to_delete:
            del obj
