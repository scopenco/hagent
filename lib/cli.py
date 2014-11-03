#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
This module with base func for HAgent
# Author: Andrey Scopenco andrey@scopenco.net
'''


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

if __name__ == "__main__":
    print __doc__
