import platform
from ctypes import CDLL
from ctypes.util import find_library

from .cdefs import define_api, precheck


def load_library() -> CDLL:
    if platform.system() != "Darwin":
        raise OSError("Library available only for MacOS.")

    LIBNAME = "ApplicationServices"

    if path := find_library(LIBNAME):
        return CDLL(path)

    raise ImportError(f"Library {LIBNAME} not found.")


lib = load_library()
define_api(lib)
precheck(lib)
