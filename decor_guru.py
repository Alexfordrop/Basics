class Component():
    '''
    Базовый интерфейс Компонента определяет поведение, которое изменяется
    декораторами.
    '''

    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    '''
    Конкретные Компоненты предоставляют реализации поведения по умолчанию. Может
    быть несколько вариаций этих классов.
    '''

    def operation(self) -> str:
        return 'ConcreteComponent'

class Decorator(Component):
    '''
    Базовый класс Декоратора следует тому же интерфейсу, что и другие
    компоненты. Основная цель этого класса - определить интерфейс обёртки для
    всех конкретных декораторов. Реализация кода обёртки по умолчанию может
    включать в себя поле для хранения завёрнутого компонента и средства его
    инициализации.
    '''

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> str:
        '''
        Декоратор делегирует всю работу обёрнутому компоненту.
        '''

        return self._component