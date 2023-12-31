# import os
# from datetime import datetime
#
# def logger(old_function):
#
#     info_dict = {}
#
#     def new_function(*args, **kwargs):
#         result = old_function(*args, **kwargs)
#         time_of_call = datetime.now()
#         info_dict[f'{args}_{kwargs}'] = (result, time_of_call, old_function.__name__)
#         with open('main.log', 'a', encoding='utf-8') as file:
#             file.write(str(info_dict))
#         return result
#     return new_function
#
#
# def test_1():
#     path = 'main.log'
#     if os.path.exists(path):
#         os.remove(path)
#
#     @logger
#     def hello_world():
#         return 'Hello World'
#
#     @logger
#     def summator(a, b=0):
#         return a + b
#
#     @logger
#     def div(a, b):
#         return a / b
#
#     assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
#     result = summator(2, 2)
#     assert isinstance(result, int), 'Должно вернуться целое число'
#     assert result == 4, '2 + 2 = 4'
#     result = div(6, 2)
#     assert result == 3, '6 / 2 = 3'
#
#     assert os.path.exists(path), 'файл main.log должен существовать'
#
#     summator(4.3, b=2.2)
#     summator(a=0, b=0)
#
#     with open(path) as log_file:
#         log_file_content = log_file.read()
#
#     assert 'summator' in log_file_content, 'должно записаться имя функции'
#     for item in (4.3, 2.2, 6.5):
#         assert str(item) in log_file_content, f'{item} должен быть записан в файл'
#
#
# if __name__ == '__main__':
#     test_1()
import os
from datetime import datetime


def logger(path):
    ...

    def __logger(old_function):
        info_dict = {}

        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            time_of_call = datetime.now()
            info_dict[f'{args}_{kwargs}'] = (result, time_of_call, old_function.__name__)
            with open(f'{path}', 'a', encoding='utf-8') as file:
                file.write(str(info_dict))
            return result

        return new_function

    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


@logger('log_4.log')
def sqr(a):
    b = a ** 2
    return b




if __name__ == '__main__':
   sqr(2)
