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
    resultsMap = {
        'create': { 'status': 'ok', 'status_msg': 'Account %s created' % testAccount },
        'delete': { 'status': 'ok', 'status_msg': 'Account %s removed' % testAccount },
        'update': { 'status': 'ok', 'status_msg': 'Account %s modified' % testAccount },
    }
    r = HAgent('http://localhost:8000/v1/')

    def doTest(self, data, result):
        data['account'] = self.testAccount
        data['module'] = 'account'
        response, content = self.r.rest_connect(data)
        self.assertEqual(json.dumps(self.resultsMap[result]),
                         json.dumps(json.loads(content)))

    def test1_account_create(self):
        ''' create account '''
        data = {'func': 'create', 'preset': 'tarif1'}
        self.doTest(data, 'create')

    def test2_account_lock(self):
        ''' lock account '''
        data = {'func': 'lock'}
        self.doTest(data, 'update')

    def test3_account_unlock(self):
        ''' unlock account '''
        data = {'func': 'unlock'}
        self.doTest(data, 'update')

    def test4_account_preset(self):
        ''' change preset for account '''
        data = {'func': 'preset', 'preset': 'tarif2'}
        self.doTest(data, 'update')

    def test5_account_delete(self):
        ''' delete account '''
        data = {'func': 'delete'}
        self.doTest(data, 'delete')

if __name__ == '__main__':
    unittest.main()
