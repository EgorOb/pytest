import pytest
import numpy as np
import functions as f


class TestCleaner:
#   Тестирование функции cleaner
    def test1(self):
        print('test1')
        word = "1\n1"
        assert f.cleaner(word) == 11
    
    def test2(self):
        print('test2')
        word = "\n-1"
        assert f.cleaner(word) == -1
        
    def test3(self):
        print('test3')
        word = "1"
        assert f.cleaner(word) == 1
        
    def test4(self):
        print('test4')
        word = "\\\\"
        assert f.cleaner(word) == ''

        
class TestRead:
#   Тестирование функции data_read    
    def test1(self):
        print('test1')
        data = f.data_read('data_test.csv', n=3)
        i = 0
        while True:
            try:
                data_tmp = next(data)
                i += 1
            except:
                break
        assert i == 7
    
    def test2(self):
        print('test2')
        data = f.data_read('data_test.csv', n=3)
        i = 0
        while True:
            try:
                data_tmp = next(data)
                i += 1
            except:
                break
        assert data_tmp == [-3, 5]

        
def test_solver():
#   Тестирование класса Solver
    solver = f.Solver()
    data_gen = f.data_read('data_test.csv', n=3)
    data_gen_all = f.data_read('data_test.csv', n=20)
    data_all = next(data_gen_all)
    
    while True:
        try:
            data_tmp = next(data_gen)
            solver.add_data(data_tmp)
        except:
            break
    
    assert np.all(np.round(solver.get_parameters(), 6) \
                  == np.round((np.mean(data_all), np.var(data_all)), 6)) == True

    
if __name__ == '__main__':
    pytest.main()