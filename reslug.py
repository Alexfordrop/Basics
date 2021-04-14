a = { 'max': 200 }
b = { 'min': 100, 'max': 250 }
c = { 'min': 50 }

# a['min'] + b['min'] + c['min'] - так не надо
print(a.get('min', 0) + b.get('min', 0) + c.get('min', 0))