# Metaclass to enforce method presence
class EnforceMethodMeta(type):
    def __new__(cls, name, bases, attrs):
        if 'required_method' not in attrs:
            raise TypeError(f"{name} is missing a required method: 'required_method'")
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=EnforceMethodMeta):
    def required_method(self):
        print("This method is required!")

obj = MyClass()
obj.required_method()
