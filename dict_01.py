man = {
    'name': 'John',
    'age': 19,
    'birthday': '2023-01-01',
    'address': {
        'street': 'Mira',
        'number': '22',
    },
}

print(
    man['age']
)


def add(a):
    a['age'] = 10


add(man)

print(man)

man['eye_color'] = 'blue'

print(man)

del man['age']

print(man)


