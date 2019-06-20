#!/usr/bin/python3

import json

def load_json(fn):
    data = {}
    with open(fn) as stream:
        data = json.load(stream)

    return data

