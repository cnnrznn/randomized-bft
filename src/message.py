import enum

class Type(enum.Enum):
    INITIAL = 1
    ECHO    = 2

class Message:

    def __init__(self, ty, fr, v, r):
        self.type = ty
        self.fr = fr
        self.value = v
        self.round = r

if __name__ == '__main__':
    Message(Type.INITIAL, 'me', 4, 0)
