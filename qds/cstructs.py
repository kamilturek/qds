from ctypes import Structure, c_double, c_uint32


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


class CGConfigureOption(Structure):
    _fields_ = [
        ("rawValue", c_uint32),
    ]
