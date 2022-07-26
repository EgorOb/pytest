import numpy as np
import re


# Функция удаления возможных побочных символов при чтения из файла. Выделение целых числел.
def cleaner(string):
    str_ = re.sub('[^-\d]', '', string)
    if str_ != '':
        return int(str_)
    return str_


# Генератор-функция для чтения даннных
def data_read(name_file, n=10):
#   Чтение из файла
    with open(name_file, 'r') as f:
        data = []
        for idx, line in enumerate(f):
#           Отчистка строки от ненужных символов и преобразование к типу int 
            line = cleaner(line)
#           Выделение строк файла на блоки необходимого размера
            if idx%n == 0 and idx != 0:
                yield data
                data = [line]
            else:  
                data.append(line)
        yield data

        
class Solver:
    """
    Класс для определения математического ожидания и дисперсии данных, разбитых на блоки
    """
    def __init__(self,):
        self.mean = 0
        self._mean2 = 0
        self.var = 0
        self.idx = 0
    
    def add_data(self, data):
        sum_chunc = 0
        sum2_chunc = 0
        len_d = len(data)
#       Определение суммы и суммы квадратов значений
        for val in data:
            sum_chunc += val
            sum2_chunc += val*val
            
        self.mean = (self.mean*self.idx + sum_chunc) / (self.idx + len_d)
        self._mean2 = (self._mean2*self.idx + sum2_chunc) / (self.idx + len_d)
        self.var = self._mean2 - self.mean*self.mean
        self.idx += len_d
    
    def get_parameters(self,):
        return (self.mean, self.var)