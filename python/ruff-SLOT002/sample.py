from collections import namedtuple


class Foo(namedtuple("foo", ["str", "int"])):
    pass

