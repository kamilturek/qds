from ctypes import Structure, c_double


class CGPoint(Structure):
    _fields = [
        ("x", c_double),
        ("y", c_double),
    ]


class CGSize(Structure):
    _fields_ = [
        ("width", c_double),
        ("height", c_double),
    ]


class CGRect(Structure):
    _fields_ = [
        ("x", c_double),
        ("y", c_double),
        ("width", c_double),
        ("height", c_double),
    ]
