class Channel:

    def __init__(self, conf, mf):
        self.conf = conf
        self.filter = mf

        # TODO start a UDP socket
        self.sk = None

    def send(self):
        # 1. spin off new thread
        # 2. get my own socket for sending
        # 3. wait with timeouts for response and resend
        pass

    def recv(self):
        # 1. recv a message from the socket
        # 2. send an ack for the message
        # 3. if the message passes the filter, return it
        # 4. if the filter rejects the message, goto 1.
        pass
