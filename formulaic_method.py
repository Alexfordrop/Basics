from abc import abstractmethod

class AbstractClass(ABC):
    '''
    Абстрактный Класс определяет шаблонный метод, содержащий скелет некоторого
    алгоритма, состоящего из вызовов (обычно) абстрактных примитивных операций.

    Конкретные подклассы должны реализовать эти операции, но оставить сам
    шаблонный метод без изменений.
    '''

    def template_method(self) -> None:
        '''
        Шаблонный метод определяет скелет алгоритма.
        '''

        self.base_operation()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()