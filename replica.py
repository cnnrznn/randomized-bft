#!/usr/bin/python3

import argparse
import random

import config
import channel
from message import Message, Type
from message_filter import Filter
import util

def do_round(conf, ch, r):
    v = random.randrange(2)
    message_count = [ 0, 0 ]
    echo_count = [ [ 0, 0 ] for i in range(conf.n) ]
    decision = False

    # put value into message channel (asynchronous sending/confirmation) as
    # (initial, me, v, r)
    ch.send(Message(Type.INITIAL, conf.id, v, r))

    # while we have less than 2f+1 votes:
    #  1. receive a message, filter only one message from every (type, from,
    #     round) tuple
    #  2. if initial, send an echo
    #  3. if echo and round == curr, increment echo_count and if at threshold,
    #     increment message_count (votes)
    #  3. if echo and round > curr, buffer the message to myself
    while sum(message_count) < ((2 * conf.f) + 1):
        msg = ch.recv()

        if Type.INITIAL == msg.type:
            pass
        elif Type.ECHO == msg.type and r == msg.round:
            pass
        elif Type.ECHO == msg.type and r < msg.round:
            pass

    # v = (message_count[0] > message_count[1]) ? 0 : 1
    # if message_count[i] has >= 2f+1, d = True else False

    # return (message_count[i], d)

    if message_count[0] > message_count[1]:
        v = 0
    else:
        v = 1

    for i in range(len(message_count)):
        if message_count[i] > (2 * conf.f):
            decision = True

    return (v, decision)



def main(args):
    conf = config.Config(util.load_json(args.config))
    conf.id = args.id
    mf = Filter()
    ch = channel.Channel(conf, mf)

    do_round(conf, ch, 0)

    return



if __name__ == '__main__':
    parser = argparse.ArgumentParser('An implementation of Bracha\'s randomized BFT consensus algorithm')
    parser.add_argument('config',
                        help='Path to config file')
    parser.add_argument('id', type=int
                        help='Integer identifying this process')

    main(parser.parse_args())

