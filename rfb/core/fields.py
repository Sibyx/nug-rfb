class Field:
    def __init__(self, struct_format: str, constant: bool = False):
        pass

    def __str__(self) -> str:
        pass


class String(Field):
    def __init__(self, value):
        super().__init__("hihi")


class UnsignedInt8(Field):
    pass
