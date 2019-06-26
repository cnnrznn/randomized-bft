class Filter:

    def __init__(self):
        self.seen = set()

    def filter(self, sender, msg):
        if (sender, msg.type, msg.fr, msg.round) in self.seen:
            return False

        self.seen.add((sender, msg.type, msg.fr, msg.round))

        return True
