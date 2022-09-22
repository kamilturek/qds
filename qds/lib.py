from ctypes import CDLL
from ctypes.util import find_library


def load():
    LIBNAME = "ApplicationServices"

    if libpath := find_library(LIBNAME):
        lib = CDLL(libpath)
        lib.CGMainDisplayID()  # Precheck
        return lib

    raise OSError(f"Library {LIBNAME} not found.")
