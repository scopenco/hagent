#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Set of fuctions for logical account administration
Author: Andrey Scopenco andrey@scopenco.net
'''

import sys
sys.path.insert(0, '/usr/local/hagent/lib')
import logging
from cli import Output
from hagent_db import add_record, del_record, update_record, \
    get_record_attr, get_account_resources


class Account(object):
    ''' class for accounts '''

    def __init__(self, options, account):
        self.options = options
        self.account = account
        self.db = self.options.get('db_file')
        self.output = {'status': 0}
        self.service_attr = {}

        if not self.account:
            self.output['status'] = 1
            self.output['status_msg'] = 'argument <account> not specified'

    def create(self, preset):
        ''' create account '''

        try:
            if not preset:
                self.output['status'] = 1
                self.output['status_msg'] = 'argument <preset> not specified'

            if self.output['status']:
                raise Output

            # check if some account exist
            check_attr = get_record_attr(self.db, 'Account', self.account)
            if not check_attr['status']:
                self.output['status'] = 1
                self.output['status_msg'] = 'Account %s exist' % self.account
                raise Output

            self.service_attr['state'] = 'on'
            self.service_attr['preset'] = preset
            self.output.update(add_record(self.db, 'Account',
                                          self.account, self.service_attr))
            raise Output

        except Output:
            return self.output

    def delete(self,  restart=1):
        ''' delete account '''

        restart = str(restart)
        if restart != str(0):
            restart = 1

        try:
            if self.output['status']:
                raise Output

            self.output.update(del_record(self.db, 'Account', self.account))
            raise Output

        except Output:
            return self.output

    def lock(self, state, restart=1):
        ''' lock account '''

        restart = str(restart)
        if restart != str(0):
            restart = 1

        try:
            if self.output['status']:
                raise Output

            # check if account exist for lock
            check_attr = get_record_attr(self.db, 'Account', self.account)
            if check_attr['status']:
                self.output.update(check_attr)
                raise Output

            '''
            if state == 'on':
                account_resources = get_account_resources(self.db, self.account, locked=1)
            elif state == 'off':
                account_resources = get_account_resources(self.db, self.account)
            else:
                self.output['status'] = 1
                self.output['status_msg'] = 'error set state for %s' % self.account
                raise Output

            if account_resources['status']:
                self.output['status'] = 1
                self.output['status_msg'] = account_resources['status_msg']
                raise Output
            '''

            self.service_attr['state'] = state
            self.output.update(update_record(self.db, 'Account', self.account, self.service_attr))
            raise Output

        except Output:
            return self.output

    def preset(self, preset,  restart=1):
        ''' change account preset '''

        restart = str(restart)
        if restart != str(0):
            restart = 1

        try:
            if not preset:
                self.output['status'] = 1
                self.output['status_msg'] = 'argument <preset> not specified'

            if self.output['status']:
                raise Output

            check_attr = get_record_attr(self.db, 'Account', self.account)
            if check_attr['status']:
                self.output.update(check_attr)
                raise Output

            self.service_attr['preset'] = preset
            self.output.update(update_record(self.db, 'Account', self.account, self.service_attr))
            raise Output

        except Output:
            return self.output


if __name__ == "__main__":
    print __doc__
