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



    def __str__(self):
        return '({}, {}, {}, {})'.format(self.type,
                                         self.fr,
                                         self.value,
                                         self.round)



    def to_bytes(self):
        d = { 'type' : self.type,
              'fr' : self.fr,
              'value' : self.value,
              'round' : self.round }

        s = json.dumps(d)

        return s.encode()



if __name__ == '__main__':
    msg = from_bytes(Message(Type.ECHO, 'me', 4, 0).to_bytes())
    print(msg)
    print(Type.INITIAL == msg.type)
    print(Type.ECHO == msg.type)
