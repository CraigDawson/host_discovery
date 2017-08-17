#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os.path


class openWithHeader(object):
    """
    Open file fpath and if it doesn't exist then header hdr is added
    otherwise the file handle is returned without the header added
    """
    def __init__(self, fpath, hdr):
        self.f = fpath
        self.h = hdr

    def __enter__(self):
        if os.path.exists(self.f):
            self.file = open(self.f, 'a')
        else:
            self.file = open(self.f, 'w')
            self.file.write('{}\n'.format(self.h))
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def __str__(self):
        return self.f


def main():
    """
    Test/Example code
    """
    fn = 'openWithHeader.tst'

    with openWithHeader(fn, 'Count,Name') as f:
        f.write('1, foo\n')

    with openWithHeader(fn, 'Count,Name') as f:
        f.write('2, bar\n')

if __name__ == '__main__':
    main()
