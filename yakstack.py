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


def add_yak_frame(stack, message):
    frame = {'text': message, 'timestamp': str(datetime.datetime.now())}
    stack['profiles'][stack['cur_profile']].append(frame)
    save_yak_stack(stack)
    return frame


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
    count = len(stack['profiles'][stack['cur_profile']])
    profile = ''
    if (stack['cur_profile'] != 'default'):
        profile = ' for profile "' + stack['cur_profile'] + '"'
    if (count):
        print 'You are currently %i yak %s deep%s' % (count, 'frame' if (count == 1) else 'frames', profile)
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


parser = argparse.ArgumentParser(description='Yak Stack!')
parser.add_argument('message', nargs='?', default='')
parser.add_argument('-l', '--list', action='store_true')
parser.add_argument('-p', '--pop', action='store_true')
parser.add_argument('-P', '--profile')
args = parser.parse_args()

stack = get_yak_stack()

if args.profile:
    switch_profile(stack, args.profile)

if args.message:
    add_yak_frame(stack, args.message)
elif args.pop:
    pop_yak_frame(stack)
# elif args.list:
#     print_yak_stack(stack)

print_yaks(stack)
