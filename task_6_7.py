"""Пыталась найти информацию, как сделать 7, но не выходит рабочий код. Пробовала через FileInput, но, видимо, не пойму до конца,
как он работает. Он перекидывает исходный фвйл в копию, но при этом исходный просто становится пустым..."""
from itertools import islice
import fileinput

with fileinput.FileInput('bakery.csv', inplace=True, backup='.bak') as f:
    u_str = islice(f, 2, 3)
    s = next(u_str)
    new_s = s.replace(s, '85000')