import numpy as np

def basic():
    ### Elements
    elem = 15
    ### Row
    row = 3
    ### Column
    column = 5
    a = np.arange(elem).reshape(row, column)
    print(a)

    print(a.shape)
    print(a.ndim)
    print(a.dtype.name)
    print(a.itemsize)
    print(a.size)
    print(type(a))

    print('Array named b')
    b = np.array([6, 7, 8])
    print(b)
    print(type(b))

###
### DIMENSION OFF ARRAYS
def dimensional():
    ### One dimensional
    a = np.arange(6)
    ### Two dimensional
    b = np.arange(12).reshape(4, 3)
    ### Three dimensional
    c = np.arange(24).reshape(2, 3, 4)

    print('ONE DIMENSIONAL')
    print(a)
    print('TWO DIMENSIONAL')
    print(b)
    print('THREE DIMENSIONAL')
    print(c)

###
### SIMPLE ARRAYS
def arrays():
    a = np.array([1, 2, 3, 4, 5, 6])
    print(a)
    print(a[0])

    b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(b)
    print(b[0])
    print(b[1])
    print(b[2])

    print('An empty array')
    np.empty(3)

###
### BASIC ARRAYS OPERATIONS
def array_operation():
    arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
    print(arr)

    sorted_arr = np.sort(arr)
    print(sorted_arr)

    ### Concatenate
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])

    print('Before')
    print(a,b)
    print('After')
    print(np.concatenate((a, b)))

    ### Concatenate two dimension with one dimension
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6]])

    print(np.concatenate((x, y), axis=0))

    ### Number of dimensions
    array_example = np.array([[[0, 1, 2, 3],[4, 5, 6, 7]],
                              [[0, 1, 2, 3],[4, 5, 6, 7]],
                              [[0, 1, 2, 3],[4, 5, 6, 7]]])
    print(array_example)
    print(array_example.ndim)

    print(array_example.shape)
    print(array_example.size)

def reshaping():
    a = np.arange(6)
    print(a)

    b = a.reshape(3, 2)
    print(b)

    b = a.reshape(2, 3)
    print(b)

    b = a.reshape(1, 6)
    print(b)

    b = a.reshape(6, 1)
    print(b)