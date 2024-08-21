

def test_function(y):
    x = y**3
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
    return x



x = test_function(9)
print(x)
