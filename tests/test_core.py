from pygletengine.core import Engine, Vertex2D


def test_engine_singleness():
    engine1 = Engine()
    engine2 = Engine()
    assert id(engine1) == id(engine2)


def test_engine_startup():
    v = Vertex2D(400, 300)
    engine = Engine()
    engine.add_objects([v])
    engine.startup()
