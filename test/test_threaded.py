#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
test_threaded.py - Unit tests for Python-LLFUSE.

Copyright © 2015 Nikolaus Rath <Nikolaus.org>

This file is part of Python-LLFUSE. This work may be distributed under
the terms of the GNU LGPL.
'''

from __future__ import division, print_function, absolute_import

if __name__ == '__main__':
    import pytest
    import sys
    sys.exit(pytest.main([__file__] + sys.argv[1:]))

import os
import sys
import pytest
import time
from threading import Thread
import stat
import errno
import llfuse


class FSTest(llfuse.Operations):
    def __init__(self):
        super(FSTest, self).__init__()
        self.hello_name = b"message"
        self.hello_inode = llfuse.ROOT_INODE+1
        self.hello_data = b"hello world\n"

    def getattr(self, inode, ctx=None):
        entry = llfuse.EntryAttributes()
        if inode == llfuse.ROOT_INODE:
            entry.st_mode = (stat.S_IFDIR | 0o755)
            entry.st_size = 0
        elif inode == self.hello_inode:
            entry.st_mode = (stat.S_IFREG | 0o644)
            entry.st_size = len(self.hello_data)
        else:
            raise llfuse.FUSEError(errno.ENOENT)

        stamp = int(1438467123.985654 * 1e9)
        entry.st_atime_ns = stamp
        entry.st_ctime_ns = stamp
        entry.st_mtime_ns = stamp
        entry.st_gid = os.getgid()
        entry.st_uid = os.getuid()
        entry.st_ino = inode

        return entry

    def lookup(self, parent_inode, name, ctx=None):
        if parent_inode != llfuse.ROOT_INODE or name != self.hello_name:
            raise llfuse.FUSEError(errno.ENOENT)
        return self.getattr(self.hello_inode)

    def opendir(self, inode, ctx):
        if inode != llfuse.ROOT_INODE:
            raise llfuse.FUSEError(errno.ENOENT)
        return inode

    def readdir(self, fh, off):
        assert fh == llfuse.ROOT_INODE

        # only one entry
        if off == 0:
            yield (self.hello_name, self.getattr(self.hello_inode), 1)

    def open(self, inode, flags, ctx):
        if inode != self.hello_inode:
            raise llfuse.FUSEError(errno.ENOENT)
        if flags & os.O_RDWR or flags & os.O_WRONLY:
            raise llfuse.FUSEError(errno.EPERM)
        return inode

    def read(self, fh, off, size):
        assert fh == self.hello_inode
        return self.hello_data[off:off+size]


def wait_for_mount(mnt_dir):
    elapsed = 0
    while elapsed < 30:
        if os.path.ismount(mnt_dir):
            return True
        time.sleep(0.1)
        elapsed += 0.1
    pytest.fail("mountpoint failed to come up")


def test_close_from_another_thread(tmpdir):
    mountpoint = str(tmpdir)

    def start_fuse():
        testfs = FSTest()
        fuse_options = set(llfuse.default_options)
        fuse_options.add('fsname=lltest')
        llfuse.init(testfs, mountpoint, fuse_options)
        try:
            llfuse.main(workers=1)
        finally:
            llfuse.close()

    thread = Thread(target=start_fuse)
    thread.start()
    wait_for_mount(mountpoint)

    llfuse.schedule_close()
    tmpdir.listdir()
    thread.join()
