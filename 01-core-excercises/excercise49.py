students = ['ines', 'salva', 'sergio', 'aaron', 'alexis', 'elias', 'elise',
            'hector', 'juanma', 'lauren', 'maryam', 'pablo', 'angela', 'raul',
            'francisco', 'david']


def shuffle_students():
    from random import shuffle
    shuffle(students)
    return students


shuffle_students = shuffle_students()
print(shuffle_students[0:0 + 2])
pairs = [shuffle_students[student:student + 2] for student in
         range(0, len(shuffle_students), 2)]

print(pairs)
