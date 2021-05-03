from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    '''
    Класс Создатель объявляет фабричный метод, который должен возвращать объект
    класса Продукт. Подклассы Создателя обычно предоставляют реализацию этого
    метода.
    '''