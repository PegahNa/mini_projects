# Using the Decorator Class file as a reference, 
# try and write a class decorator that remembers the 
# arguments passed to the following function. If that
# value has been given before, output an additional line
# that states how many times it's been previously called.

# EXPAND THIS CLASS
class MonitorDecorator:
    def __init__(self, function):
        self.function = function
        self._memory = []
    
    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)
        self._memory.append(result)
        if result in self._memory:
           if self._memory.count(result) == 1:
               return result
           else:
               return f"This number has been called {self._memory.count(result)} times"
       




@MonitorDecorator
def what_is_this_number(num):
    return f'The number entered is {num}!'

print(what_is_this_number(4))
print(what_is_this_number(3))

