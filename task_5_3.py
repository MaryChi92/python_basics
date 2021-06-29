# Женя, ниже вопрос по этому дз

from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Светлана', 'Инесса']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

pair = ((tutor, group) for tutor, group in zip_longest(tutors, classes[:len(tutors)]))

for i in pair:
    print(i)

print('-'*30)
print(type(pair))


### скорее всего глупый вопрос, я упускаю какие-то основы, но почему не работает такой код?
# def tutor_class():
#     if len(tutors) > len(classes):
#         pair = ((tutor, group) for tutor, group in zip_longest(tutors, classes))
#     else:
#         pair = ((tutor, group) for tutor, group in zip(tutors, classes))
#     yield pair
#
# print(next(tutor_class()))
