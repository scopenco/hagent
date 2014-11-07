#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Set of fuctions for logical account administration
Author: Andrey Scopenco andrey@scopenco.net
'''

import sys
sys.path.insert(0, '/usr/local/hagent/lib')
from modules.account.Account import Account


__all__ = ['create',
           'delete',
           'lock',
           'unlock',
           'preset',
           ]


def create(args, config):
    '''Create account.'''
    return Account(config,
            args.get('account')).create(args.get('preset'))


def delete(args, config):
    '''Delete account.'''
    return Account(config, args.get('account')).delete(restart=args.get('restart'))


def lock(args, config):
    '''Lock account.'''
    return Account(config,
            args.get('account')).lock('off', restart=args.get('restart'))


def unlock(args, config):
    '''Unlock account.'''
    return Account(config,
            args.get('account')).lock('on', restart=args.get('restart'))


def preset(args, config):
    '''Change preset for account.'''
    return Account(config,
            args.get('account')).preset(args.get('preset'), restart=args.get('restart'))


if __name__ == "__main__":
    print __doc__
