class Pupil():
    def __init__(self, surname, name, mark):
        self.surname = surname
        self.name = name
        self.mark = mark

best_pupils = []
sum_mark = 0
amount = 0

with open("pupils_txt.txt", 'r', encoding='utf-8') as file:
    for line in file:
        data = line.split(' ')
        pupil = Pupil(data[0], data[1], int(data[2]))
        sum_mark += pupil.mark
        amount += 1
        if pupil.mark == 5:
            best_pupils.append(pupil.surname)


print('Отличники')
for pupil in best_pupils:
    print(pupil)
print(sum_mark/amount)

