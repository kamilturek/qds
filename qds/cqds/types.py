from ctypes import Structure, c_double, c_uint32

CGDirectDisplayID = c_uint32
CGError = int


class CGSize(Structure):
    _fields_ = [
        ("width", c_double),
        ("height", c_double),
    ]


class CGPoint(Structure):
    _fields_ = [
        ("x", c_double),
        ("y", c_double),
    ]


class CGRect(Structure):
    _fields_ = [
        ("origin", CGPoint),
        ("size", CGSize),
    ]
