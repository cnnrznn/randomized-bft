class Channel:

    # Notes: The send processes must be killable. If they get stuck trying to
    # deliver messages to byzantine processes they may hang indefinitely. Create
    # a function to clean them up or destroy them, possible selectively (for
    # generality), or in one big KILLALL syle function.

    def __init__(self, conf, mf):
        self.conf = conf
        self.filter = mf

        # TODO start a UDP socket
        self.sk = None

    def send(self):
        # 1. spin off new thread
        # 2. get my own socket for sending
        # 3. wait with timeouts for response and resend

        # NOTE: I need to wait for EVERY of the 3f + 1 processes to respond. If
        # not, it is possible less than 2f+1 correct processes received the
        # initial, which means there won't be enought ECHO's "in the system" in
        # order to accept the echo.
        pass

    def recv(self):
        # 1. recv a message from the socket
        # 2. send an ack for the message
        # 3. if the message passes the filter, return it
        # 4. if the filter rejects the message, goto 1.
        pass
