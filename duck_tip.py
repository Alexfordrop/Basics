class English:
    def greeting(self):
        print('Hello')

class French:
    def greeting(self):
        print('Bonjour')

def intro(language):
    language.greeting()

john = English()
gerard = French()
intro(john)
intro(gerard)