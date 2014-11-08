#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Set of fuctions for ip addr administration
Author: Andrey Scopenco andrey@scopenco.net
'''

import sys
sys.path.insert(0, '/usr/local/hagent/lib')
from modules.ip.IpAddr import IpAddr


__all__ = ['create',
           'delete',
           'assign']


def create(args, config):
    '''Add ip address.'''
    return IpAddr(config, args.get('ip')).create(args.get('account'),
        args.get('shared'))


def delete(args, config):
    '''Delete ip address.'''
    return IpAddr(config, args.get('ip')).delete()


def assign(args, config):
    '''Assign ip address to account.'''
    return IpAddr(config, args.get('ip')).update(
        args.get('account'), args.get('shared'),
        args.get('free'), restart=args.get('restart'))


if __name__ == "__main__":
    print __doc__
