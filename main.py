#!/usr/bin/env python3
from editor import Editor

def test1():
    editor = Editor()
    message = editor.open_editor(b"This is a test")
    print(message)

def test2():
    editor = Editor()
    args = editor.get_args(['test','test2'], b'# header', b'#footer')
    for arg in args:
        print(arg + ": " + args[arg])

def test3():
    editor = Editor()
    args = {'test':'defaultv'}
    args = editor.get_args(args, b'# header', b'#footer')
    for arg in args:
        print(arg + ": " + args[arg])

if __name__ == '__main__':
    test3()
