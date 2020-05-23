import datetime
from time import time
import time


class Open_file:

    def __init__(self, country_path, log_path):
        self.country_path = country_path
        self.log_path = log_path
        self.Country_dict()
        self.start = time.time()

    def Country_dict(self):
        with open(self.country_path) as file:
            dicts = {}
            for line in file:
                key, *value = line.split()
                dicts[key] = value
            rus = 'Россия'
            result_list = []
            for k, v in dicts.items():
                if rus in v:
                    result_list.append(k.split() + v)
            for m in result_list:
                print(f'{m}')

    def __enter__(self):
        self.log = open(self.log_path, 'w', encoding='UTF-8')
        return self

    def write_log(self):
        self.log.write(f'Запуск программы: {datetime.datetime.utcnow()}\n')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.write_log(f'Error {exc_val}')
        self.log.write(f'Закрытие программы: {datetime.datetime.utcnow()}\n')
        self.runtime = (time.time() - self.start)
        self.log.write(f'Потраченное время: {self.runtime}\n')
        self.log.close()


if __name__ in '__main__':
    with Open_file('City.txt', 'log_time.txt') as open_file:
        open_file.write_log()
        time.sleep(2)
