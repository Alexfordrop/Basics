import pyscreenshot

# Делаем скриншот
image = pyscreenshot.grab()

# Открываем его
image.show()

# Сохраняем результат
image.save('screenshot.png')