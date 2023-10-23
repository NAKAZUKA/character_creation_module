import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_files = [filename.lower() for filename in os.listdir(BASE_DIR)]

files_list = ['main.py', 'readme.md']
mess = ''


def test_program():
    for filename in files_list:
        mess = (f'Файл `{filename}` не найден в корне репозитория')
        assert filename in dir_files, mess
