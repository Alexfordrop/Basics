from pathlib import Path

home = Path.home()
print(home)

script = home

print(script.name)

print(script.exists())
print(script.is_dir())