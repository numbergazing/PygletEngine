import pyglet

from core.logging import engine_log
from core.types import Objects


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
