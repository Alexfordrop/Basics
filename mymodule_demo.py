import mymodule

mymodule.sayhi()
print('Версия', mymodule.__version__)

# Второй вариант используя from...import
from mymodule import sayhi, __version__

sayhi()
print('Версия', __version__)