import pyglet

from pygletengine.core import Drawable, Object, Updatable


class Vertex2D(Object, Updatable, Drawable):

    def __init__(self, x: int = 0, y: int = 0):
        super(Object).__init__()
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ("v2i", (self.x, self.y)))
