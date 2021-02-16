class Singleton(object):
    obj = None

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = object.__new__(cls, *args, **kwargs)
        return cls.obj

single = Singleton()
single.attr = 42
newSingle = Singleton()
newSingle.attr
newSingle is single

print(newSingle.attr)