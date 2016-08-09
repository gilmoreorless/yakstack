#!/usr/bin/env python

import os
import json
import argparse
import datetime

dirname = os.path.expanduser('~/.yakstack')
path_yak = dirname + '/yakstack.json'


def ensure_files():
    # Mkdir if it doesn't exist
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    if not os.path.isfile(path_yak):
        f = open(path_yak, 'w')
        f.write('[]')
        f.close()


def get_yak_stack():
    ensure_files()
    f = open(path_yak, 'r')
    raw_json = f.read()
    f.close()
    stack = json.loads(raw_json)
    if (isinstance(stack, list)):
        stack = convert_to_profile_format(stack)
    return stack


def convert_to_profile_format(stack):
    return {'cur_profile': 'default', 'profiles': {'default': stack}}


def save_yak_stack(stack):
    f = open(path_yak, 'w')
    json_str = json.dumps(stack, indent=4)
    f.write(json_str)
    f.close()


def add_yak_frame(stack, item):
    frame = {'text': item, 'timestamp': str(datetime.datetime.now())}
    stack['profiles'][stack['cur_profile']].append(frame)
    save_yak_stack(stack)
    return frame


def add_yak_frames(stack, items):
    return [add_yak_frame(stack, item) for item in items]


def switch_profile(stack, profile):
    if (profile not in stack['profiles']):
        stack['profiles'][profile] = []
    stack['cur_profile'] = profile
    save_yak_stack(stack)


def pop_yak_frame(stack):
    substack = stack['profiles'][stack['cur_profile']]
    if (len(substack)):
        substack.pop()
        save_yak_stack(stack)


def print_yak_frame_count(stack):
    profile_count = len(stack['profiles'])
    frame_count = len(stack['profiles'][stack['cur_profile']])
    profile = ''
    if (profile_count > 1):
        profile = ' for profile "' + stack['cur_profile'] + '"'
    if (frame_count):
        print 'You are currently %i yak %s deep%s' % (frame_count, 'frame' if (frame_count == 1) else 'frames', profile)
    else:
        print 'No yaks to shave right now%s!' % profile


def print_yak_stack(stack):
    spaces = -2
    frames = stack['profiles'][stack['cur_profile']]
    for frame in frames:
        print '%s%s%s' % (' ' * spaces if (spaces > 0) else '', u'\u2937 ' if (spaces >= 0) else '', frame['text'])
        spaces += 3


def print_yaks(stack):
    print_yak_frame_count(stack)
    print
    print_yak_stack(stack)


parser = argparse.ArgumentParser(description='Yak Stack! Stack your yaks.')
parser.add_argument('item', nargs='*', default=[],
                    help='one or more items to add to the yak stack')
parser.add_argument('-s', '--shave', action='store_true',
                    help='shave a yak; remove the most recent item from the stack')
parser.add_argument('-p', '--profile',
                    help='switch to a different profile to use a different stack')
args = parser.parse_args()

stack = get_yak_stack()

if args.profile:
    switch_profile(stack, args.profile)

if args.shave:
    pop_yak_frame(stack)

if args.item:
    add_yak_frames(stack, args.item)

print_yaks(stack)
