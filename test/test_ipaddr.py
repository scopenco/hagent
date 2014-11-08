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

    testIp = '192.168.0.100'
    testAccount = 'a100500'
    r = HAgent('http://localhost:8000/v1/')

    def test0Up(self):
        data = {'module': 'account', 'func': 'create', 'account': self.testAccount, 'preset': 'tarif1'}
        response, content = self.r.rest_connect(data)
        result = {'status': 'ok', 'record': 'Account %s state=on preset=tarif1' % self.testAccount, 'status_msg': 'Account %s created' % self.testAccount}
        self.assertEqual(json.dumps(result), json.dumps(json.loads(content)))

    def doTest(self, data, result):
        data['ip'] = self.testIp
        data['module'] = 'ip'
        response, content = self.r.rest_connect(data)
        self.assertEqual(json.dumps(result), json.dumps(json.loads(content)))

    def test1_create1(self):
        ''' create ip '''
        data = {'func': 'create'}
        result = {'status': 'ok', 'record': 'Ip %s' % self.testIp, 'status_msg': 'Ip %s created' % self.testIp}
        self.doTest(data, result)
        self.test5_delete()

    def test1_create2(self):
        ''' create ip and assign to account '''
        data = {'func': 'create', 'account': self.testAccount}
        result = {'status': 'ok', 'record': 'Ip %s account=%s' % (self.testIp, self.testAccount), 'status_msg': 'Ip %s created' % self.testIp}
        self.doTest(data, result)
        self.test5_delete()

    def test1_create3(self):
        ''' create ip and assign to shared '''
        data = {'func': 'create', 'shared': 'on'}
        result = {'status': 'ok', 'record': 'Ip %s shared=on' % self.testIp, 'status_msg': 'Ip %s created' % self.testIp}
        self.doTest(data, result)

    def test2_assign1(self):
        ''' assign ip to account '''
        data = {'func': 'assign', 'account': self.testAccount}
        result = {'status': 'ok', 'record': 'Ip %s account=%s' % (self.testIp, self.testAccount), 'status_msg': 'Ip %s modified' % self.testIp}
        self.doTest(data, result)

    def test2_assign2(self):
        ''' assign ip to shared pool '''
        data = {'func': 'assign', 'shared': 'on'}
        result = {'status': 'ok', 'record': 'Ip %s shared=on' % self.testIp, 'status_msg': 'Ip %s modified' % self.testIp}
        self.doTest(data, result)

    def test2_assign3(self):
        ''' assign ip to free pool '''
        data = {'func': 'assign', 'free': 'on'}
        result = {'status': 'ok', 'record': 'Ip %s' % self.testIp, 'status_msg': 'Ip %s modified' % self.testIp}
        self.doTest(data, result)

    def test5_delete(self):
        ''' delete ip '''
        data = {'func': 'delete'}
        result = {'status': 'ok', 'status_msg': 'Ip %s removed' % self.testIp}
        self.doTest(data, result)

    def testDown(self):
        data = {'module': 'account', 'func': 'delete', 'account': self.testAccount}
        response, content = self.r.rest_connect(data)
        result = {'status': 'ok', 'status_msg': 'Account %s removed' % self.testAccount}
        self.assertEqual(json.dumps(result), json.dumps(json.loads(content)))

if __name__ == '__main__':
    unittest.main()
