import pickle

greetings = {'russian': 'привет', 'english' : 'hello'}

# сохраняем данные
with open('data.p', 'wb') as file:
    pickle.dump(greetings, file)

# читаем данные
with open('data.p', 'rb') as file:
    data = pickle.load(file)

print(data)