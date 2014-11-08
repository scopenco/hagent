#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
This module with base func for HAgent
Author: Andrey Scopenco andrey@scopenco.net
'''

from errno import EACCES, EAGAIN
from fcntl import flock, LOCK_EX, LOCK_NB
from sys import exit, stderr
import os
import logging

try:
    import simplejson as json
except ImportError:
    import json


def read_config(config_path):
    '''
    Get info from config file
    '''

    data = {}
    try:
        execfile(config_path, {}, data)
    except (SyntaxError, OSError, IOError), e:
        stderr.write(repr(e))
        stderr.write('\n')
        exit(1)

    return data


class Output(Exception):
    ''' Exception for output '''
    pass


class FileLock:
    '''
    Ensures application is running only once, by using a lock file.

    Ensure call to lock works.  Then call unlock at program exit.

    You cannot read or write to the lock file, but for some reason you can
    remove it.  Once removed, it is still in a locked state somehow.  Another
    application attempting to lock against the file will fail, even though
    the directory listing does not show the file.  Mysterious, but we are glad
    the lock integrity is upheld in such a case.

    Instance variables:
        lockfile  -- Full path to lock file
        lockfd    -- File descriptor of lock file exclusively locked
    '''
    def __init__(self, lockfile):
        self.lockfile = lockfile
        self.lockfd = None

    def lock(self):
        '''
        Creates and holds on to the lock file with exclusive access.
        Returns True if lock successful, False if it is not, and raises
        an exception upon operating system errors encountered creating the
        lock file.
        '''
        try:
            #
            # Create or else open and trucate lock file, in read-write mode.
            #
            # A crashed app might not delete the lock file, so the
            # os.O_CREAT | os.O_EXCL combination that guarantees
            # atomic create isn't useful here.  That is, we don't want to
            # fail locking just because the file exists.
            #
            # Could use os.O_EXLOCK, but that doesn't exist yet in my Python
            #
            logging.debug('try lock %s' % self.lockfile)
            self.lockfd = os.open(self.lockfile,
                                  os.O_TRUNC | os.O_CREAT | os.O_RDWR)

            # Acquire exclusive lock on the file, but don't
            # block waiting for it
            flock(self.lockfd, LOCK_EX | LOCK_NB)

            # Writing to file is pointless, nobody can see it
            os.write(self.lockfd, '')

            return True

        except (OSError, IOError), e:
            # Lock cannot be acquired is okay,
            # everything else reraise exception
            if e.errno in (EACCES, EAGAIN):
                return False
            else:
                raise

    def unlock(self):
        try:
            logging.debug('try unlock %s' % self.lockfile)
            # FIRST unlink file, then close it.  This way, we avoid file
            # existence in an unlocked state
            os.unlink(self.lockfile)
            # Just in case, let's not leak file descriptors
            os.close(self.lockfd)
        except (OSError, IOError), e:
            # Ignore error destroying lock file.  See class doc about how
            # lockfile can be erased and everything still works normally.
            pass


def convert_status(output):
    ''' convert status from int to str '''

    if output['status'] == 0:
        output['status'] = 'ok'
    if output['status'] == 1:
        output['status'] = 'err'

    return output


if __name__ == "__main__":
    print __doc__
