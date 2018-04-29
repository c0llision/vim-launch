#!/usr/bin/env python3 import sys
import tempfile
import os
from subprocess import call


class Editor():
    def __init__(self):
        self.EDITOR = os.environ.get('EDITOR', 'vim')
        pass

    def open_editor(self, initial_message=b"", ignore_comments=True):
        with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
            tf.write(initial_message)
            tf.flush()
            call([self.EDITOR, tf.name])
            with open(tf.name, 'r') as f:
                msg = f.read()

        return msg

    def __parse_args(self, edited_message):
        return_args = {}

        for line in edited_message.split('\n'):
            if ':' not in line:
                continue
            if line.startswith(b"#"):
                continue

            key, value = line.split(':', 1)
            key, value = key.strip(), value.strip()
            return_args[key] = value

        return return_args

    def get_args(self, args, header=b'', footer=b''):
        initial_message = b""

        if header:
            initial_message += header + b'\n'

        if type(args) is dict:
            for k,v in args.items():
                initial_message += ('%s: %s\n' % (k, v)).encode('utf-8')
        else:
            initial_message += str(':\n'.join([arg for arg in args]) + ':\n').encode('utf-8')

        if footer:
            initial_message += footer + b'\n'

        edited_message = self.open_editor(initial_message=initial_message)
        return_args = self.__parse_args(edited_message)

        for key in return_args:
            if key not in args:
                raise Exception('Key not in args: %s' % key)
        for arg in args:
            if arg not in return_args:
                raise Exception('key missing: %s' % arg)

        return return_args
