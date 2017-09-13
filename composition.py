import forbiddenfruit


UseIt = type("UseIt!", (Exception,), {})
__init_subclass__ = object.__init_subclass__


@classmethod
def dikembe_mutombo(cls, **kwargs):
    if cls.__bases__ == (object,):
        return
    elif "unittest.case.TestCase" in {
        each.__module__ + "." + each.__qualname__ for each in cls.__bases__
    }:
        print("We're sorry, but we'll allow it, it's not your fault.")
        return
    raise UseIt("COMPOSITION!")


def demon_worship():
    forbiddenfruit.curse(object, "__init_subclass__", __init_subclass__)


forbiddenfruit.curse(object, "__init_subclass__", dikembe_mutombo)
