#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Set of fuctions/classes for ip administration
Author: Andrey Scopenco andrey@scopenco.net
'''

import sys
sys.path.insert(0, '/usr/local/hagent/lib')
import logging
from cli import Output
from hagent_db import add_record, del_record, update_record, \
    get_record_attr, get_account_resources


class IpAddr(object):
    '''Base class for ip administration '''

    def __init__(self, options, ip):
        self.options = options
        self.ip = ip
        self.db = self.options.get('db_file')
        self.output = {'status': 0}
        self.service_attr = {}

        if not self.ip:
            self.output['status'] = 1
            self.output['status_msg'] = 'argument <ip> not specified'

    def create(self, account, shared):
        '''Create ip and assign to user.'''

        try:
            if self.output['status']:
                raise Output

            # check if some ip exist
            check_attr = get_record_attr(self.db, 'Ip', self.ip)
            if not check_attr['status']:
                self.output['status'] = 1
                self.output['status_msg'] = 'Ip %s exist' % self.ip
                raise Output

            if shared == 'on':
                self.service_attr['shared'] = shared
            else:
                if account:
                    self.service_attr['account'] = account
            self.output.update(add_record(self.db, 'Ip',
                                          self.ip, self.service_attr))
            raise Output

        except Output:
            return self.output

    def delete(self):
        '''Delete virtual domain.'''

        try:
            if self.output['status']:
                raise Output

            #TODO
            # add check if ip assigned to one of users
            # if so show error

            self.output.update(del_record(self.db, 'Ip', self.ip))
            raise Output

        except Output:
            return self.output

    def update(self, account, shared='off', free='off', restart=1):
        '''Change account for ip'''

        restart = str(restart)
        if restart != str(0):
            restart = 1

        try:
            if not account and shared == 'off' and free == 'off':
                self.output['status'] = 1
                self.output['status_msg'] = 'argument <account> not specified'

            if self.output['status']:
                raise Output

            # check if ip exist
            check_attr = get_record_attr(self.db, 'Ip', self.ip)
            if check_attr['status']:
                self.output.update(check_attr)
                raise Output
            self.service_attr.update(check_attr)
            del(self.service_attr['status'])

            if free == 'on':
                # TODO 
                # remove ip from all domains 
                if 'account' in self.service_attr:
                    del(self.service_attr['account'])
                if 'shared' in self.service_attr:
                    del(self.service_attr['shared'])
            else:
                if shared == 'on':
                    # TODO
                    # remove ip from account and assign to shared
                    self.service_attr['shared'] = shared
                    if 'account' in self.service_attr:
                        del(self.service_attr['account'])
                else:
                    # TODO
                    # remove from shared and assign to account
                    # if shared add is only one, show error
                    self.service_attr['account'] = account
                    if 'shared' in self.service_attr:
                        del(self.service_attr['shared'])

            self.output.update(update_record(
                self.db, 'Ip', self.ip, self.service_attr, remove_attr=True))
            raise Output

        except Output:
            return self.output


if __name__ == "__main__":
    print __doc__
