# version_2

import hashlib
import re


def get_hash_string(text):
    salt = 'sergshrb@mail.ru'

    hash_str = hashlib.sha256(text.encode('UTF-8') + salt.encode('UTF-8'))
    hex_dig = hash_str.hexdigest()  # хэш в шестнадцатеричном формате
    return print(f'Хэш-значение введенного пароля: {hex_dig}')


def valid_pass():
    pass_regex = re.compile(r'''(^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()\-_+.])(?=.*[0-9]).{8,}$)''', re.VERBOSE)

    while True:
        password = input('введите пароль: ')
        if re.search(pass_regex, password):
            get_hash_string(password)
            break
        else:
            print('Пароль должен содержать:'
                  '\n- хотя бы одну прописную букву'
                  '\n- хотя бы одну строчную букву'
                  '\n- хотя бы одну цифру'
                  '\n- хотя бы один из следующих спецсимволов:!@#$%^&*()-_+.'
                  '\n- не менее 8 символов')
            continue


valid_pass()
