from abc import abstractclassmethod
from typing import Protocol, Iterable

class SupportsRoar(Protocol):
    @abstractclassmethod
    def roar(self) -> None:
        raise NotImplementedError

class Lion(SupportsRoar):
    def roar(self) -> None:
        print('roar')

class Tiger:
    def roar(self) -> None:
        print('roar')

class Cat:
    def meow(self) -> None:
        print('meow')

def roar_all(bigcats: Iterable[SupportsRoar]) -> None:
    for t in bigcats:
        t.roar()

roar_all([Lion(), Tiger()]) # ok
roar_all([Cat()]) # error