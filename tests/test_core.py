from pygletengine.core import Engine
from pygletengine.core.types import Vertex2D


def test_engine_startup():
    v = Vertex2D(400, 300)
    engine = Engine()
    engine.add_objects([v])
    engine.startup()
