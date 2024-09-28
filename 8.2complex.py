class RegistryMeta(type):
    registry = {}

    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        cls.registry[name] = new_class
        return new_class

class BaseClass(metaclass=RegistryMeta):
    pass

class A(BaseClass):
    pass

class B(BaseClass):
    pass

# Accessing the registry
print(RegistryMeta.registry)  # {'BaseClass': <class '__main__.BaseClass'>, 'A': <class '__main__.A'>, 'B': <class '__main__.B'>}
