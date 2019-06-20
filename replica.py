#!/usr/bin/python3

import argparse
import random

import config
import util

def do_round(conf, r):
    v = random.randrange(2)
    message_count = [ 0, 0 ]
    echo_count = [ [ 0, 0] for i in range(conf.n) ]

    # put value into message channel (asynchronous sending/confirmation) as
    # (initial, me, v, r)

    # while we have less than 2f+1 votes:
    #  1. receive a message, filter only one message from every (type, from,
    #     round) tuple
    #  2. if initial, send an echo
    #  3. if echo and round == curr, increment echo_count and if at threshold,
    #     increment message_count (votes)
    #  3. if echo and round > curr, buffer the message to myself

    # v = (message_count[0] > message_count[1]) ? 0 : 1
    # if message_count[i] has >= 2f+1, d = True else False

    # return (message_count[i], d)

    return 



def main(args):
    conf = config.Config(util.load_json(args.config))

    do_round(conf, 0)

    return



if __name__ == '__main__':
    parser = argparse.ArgumentParser('An implementation of Bracha\'s randomized BFT consensus algorithm')
    parser.add_argument('config',
                        help='Path to config file')

    main(parser.parse_args())

