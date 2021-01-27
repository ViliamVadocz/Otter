from sys import modules

from rlbot.utils.rendering.rendering_manager import RenderingManager


def bind_renderer(renderer: RenderingManager):
    # Bind module methods to global renderer.
    module = modules[__name__]
    for method_name in dir(renderer):
        if not callable(getattr(renderer, method_name)):
            continue
        if method_name.startswith("_"):
            continue
        setattr(module, method_name, renderer.__getattribute__(method_name))
