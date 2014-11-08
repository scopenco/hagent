#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Unit tests for module account.
'''

import unittest
from httplib2 import Http
from urllib import urlencode
from time import strftime, gmtime

try:
    import simplejson as json
except ImportError:
    import json


class HAgent(object):
    def __init__(self, baseurl):
        self.baseurl = baseurl

    def _headers(self):
        currTime = self.__get_date()
        headers = {'x-hagent-requestDate': currTime,
                   'content-type': 'application/json'}

        return headers

    def __get_date(self):
        return strftime('%a, %d %b %Y %H:%M:%S GMT', gmtime())

    def rest_connect(self, data={}):
        h = Http()
        return h.request(self.baseurl + '?' + urlencode(data),
                         'GET', headers=self._headers())


class HAgentTest(unittest.TestCase):
    ''' Test module account '''

    testAccount = 'a100500'
    r = HAgent('http://localhost:8000/v1/')

    def doTest(self, data, result):
        data['account'] = self.testAccount
        data['module'] = 'account'
        response, content = self.r.rest_connect(data)
        self.assertEqual(json.dumps(result), json.dumps(json.loads(content)))

    def test1_create(self):
        ''' create account '''
        data = {'func': 'create', 'preset': 'tarif1'}
        result = {'status': 'ok', 'record': 'Account %s state=on preset=tarif1' % self.testAccount, 'status_msg': 'Account %s created' % self.testAccount}
        self.doTest(data, result)

    def test2_lock(self):
        ''' lock account '''
        data = {'func': 'lock'}
        result = {'status': 'ok', 'record': 'Account %s state=off preset=tarif1' % self.testAccount, 'status_msg': 'Account %s modified' % self.testAccount}
        self.doTest(data, result)

    def test3_unlock(self):
        ''' unlock account '''
        data = {'func': 'unlock'}
        result = {'status': 'ok', 'record': 'Account %s state=on preset=tarif1' % self.testAccount, 'status_msg': 'Account %s modified' % self.testAccount}
        self.doTest(data, result)

    def test4_preset(self):
        ''' change preset for account '''
        data = {'func': 'preset', 'preset': 'tarif2'}
        result = {'status': 'ok', 'record': 'Account %s state=on preset=tarif2' % self.testAccount, 'status_msg': 'Account %s modified' % self.testAccount}
        self.doTest(data, result)

    def test5_delete(self):
        ''' delete account '''
        data = {'func': 'delete'}
        result = {'status': 'ok', 'status_msg': 'Account %s removed' % self.testAccount}
        self.doTest(data, result)

if __name__ == '__main__':
    unittest.main()
