from ast import literal_eval
import os
from ctypes import *
import pathlib
import time


def array_sum():
    script_dir = pathlib.Path(__file__).parent

    lib_path = pathlib.Path.joinpath(script_dir, "sum_array.dll")

    lib_sum_array = cdll.LoadLibrary(lib_path.as_posix())

    lib_sum_array.sum_array.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

    arr = [i for i in range(999999)]

    t0 = time.perf_counter()
    arr2 = [i * 2 for i in arr]
    result = sum(arr2)
    t1 = time.perf_counter()
    delta = t1 - t0
    print(delta)
    print(result)
    print()

    t0 = time.perf_counter()
    arr_c = (c_double * len(arr))(*arr)
    result = c_double()
    lib_sum_array.sum_array(arr_c, byref(result), c_int(len(arr)))
    t1 = time.perf_counter()
    delta = t1 - t0
    print(delta)
    print(result.value)