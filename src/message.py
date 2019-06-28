import enum
import json

class Type(enum.IntEnum):
    INITIAL = 1
    ECHO    = 2


def from_bytes(b):
    s = b.decode()
    d = json.loads(s)

    return Message(d['type'],
                   d['fr'],
                   d['value'],
                   d['round'])

class Message:

    def __init__(self, ty, fr, v, r):
        self.type = ty
        self.fr = fr
        self.value = v
        self.round = r

    def to_bytes(self):
        d = { 'type' : self.type,
              'fr' : self.fr,
              'value' : self.value,
              'round' : self.round }

        s = json.dumps(d)

        return s.encode()

if __name__ == '__main__':
    Message(Type.INITIAL, 'me', 4, 0)
