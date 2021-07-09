""" Женя, крутила-вертела я эту задачу, но не получается у меня правильная структура. Неправильно вкладываются папки,
не успеваю доработать :( """

import yaml
from yaml.loader import SafeLoader
import os
from pathlib import Path

starter_dict = dict(my_project=[{'settings': ['__init__.py', 'dev.py', 'prod.py']},
                                {'mainapp': ['__init__.py', 'models.py', 'views.py',
                                             {'templates': [{'mainapp': ['base.html', 'index.html']}]}]},
                                {'authapp': ['__init__.py', 'models.py', 'views.py',
                                             {'templates': [{'mainapp': ['base.html', 'index.html']}]}]}])


with open('config.yaml', 'w', encoding='utf-8') as f:
    yml_doc = yaml.dump(starter_dict, f, sort_keys=False, default_flow_style=False)

with open('config.yaml', 'r', encoding='utf-8') as f:
    a = yaml.load(f, SafeLoader)
    print(a)


    def create_starter(dict_a):
        for key, value in dict_a.items():
            if not os.path.exists(key):
                os.mkdir(key)
                # os.chdir(key)
            if isinstance(value, list):
                for i in value:
                    if isinstance(i, dict):
                        create_starter(i)
                    elif '.' in i:
                        Path(i).touch()
            elif '.' in value:
                Path(value).touch()

    if __name__ == '__main__':
        create_starter(a)
