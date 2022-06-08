from logging import Formatter, StreamHandler, getLogger, INFO

engine_log = getLogger("engine")
engine_log.setLevel(INFO)

engine_handler = StreamHandler()
engine_formatter = Formatter("%(asctime)s [%(name)s] %(message)s", "%Y-%m-%d %H:%M:%S")
engine_handler.setFormatter(engine_formatter)
engine_log.addHandler(engine_handler)
