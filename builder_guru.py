from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any

class Builder(ABC):
    '''
    Интерфейс Строителя объявляет создающие методы для различных частей объектов
    Продуктов.
    '''

    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass

class ConcreteBuilder1(Builder):
    '''
    Классы Конкретного Строителя следуют интерфейсу Строителя и предоставляют
    конкретные реализации шагов построения. Ваша программа может иметь несколько
    вариантов Строителей, реализованных по-разному.
    '''