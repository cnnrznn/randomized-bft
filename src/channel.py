import multiprocessing as mp
import socket
import time

import message



class Channel:

    # Notes: The send processes must be killable. If they get stuck trying to
    # deliver messages to byzantine processes they may hang indefinitely. Create
    # a function to clean them up or destroy them, possible selectively (for
    # generality), or in one big KILLALL syle function.

    __port = 3333

    def __init__(self, conf, mf):
        self.conf = conf
        self.filter = mf
        self.procs = []

        self.sk = socket.socket(socket.AF_INET,
                                socket.SOCK_DGRAM)
        self.sk.bind((self.conf.ips[self.conf.id], self.__port))

        return



    def async_send(self, msg, i):
        timeout = 2
        end = False

        sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sk.setblocking(False)

        while not end:
            sk.sendto(msg.to_bytes(), (self.conf.ips[i], self.__port))

            time.sleep(timeout)

            try:
                ok, addr = sk.recvfrom(1024)

                if 'ok' == ok.decode():
                    end = True
            except:
                pass

        return



    def broadcast(self, msg):
        # 1. spin off new thread
        # 2. get my own socket for sending
        # 3. wait with timeouts for response and resend

        # NOTE: I need to wait for EVERY of the 3f + 1 processes to respond. If
        # not, it is possible less than 2f+1 correct processes received the
        # initial, which means there won't be enought ECHO's "in the system" in
        # order to accept the echo.

        for i in range(self.conf.n):
            self.send(i, msg)

        return



    def send(self, i, msg):
        proc = mp.Process(target=self.async_send,
                          args=(msg, i),
                          daemon=True)
        proc.start()
        self.procs.append(proc)

        return



    def recv(self):
        # 1. recv a message from the socket
        # 2. send an ack for the message
        # 3. if the message passes the filter, return it
        # 4. if the filter rejects the message, goto 1.

        while True:
            data, addr = self.sk.recvfrom(1024)
            try:
                msg = message.from_bytes(data)
                self.sk.sendto('ok'.encode(), addr)

                if self.filter.filter(addr[0], msg):
                    return msg
            except:
                pass
