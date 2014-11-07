#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Python wrapper for the HAgent RESTful API V1.0.
'''

from optparse import OptionParser
from httplib2 import Http
from urllib import urlencode
from time import strftime, gmtime
from sys import stdout, exit
import logging


# A good practice
try:
    import simplejson as json
except ImportError:
    import json


CONFIG = None
__version__ = '$Id$'


class HAgent:
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
        logging.debug(data)
        h = Http()
        return h.request(self.baseurl + '?' + urlencode(data),
                         'GET', headers=self._headers())


def main():

    global CONFIG

    p = OptionParser(description=__doc__,
                     prog="hagent.py",
                     version=__version__,
                     usage="%prog -h")
    p.add_option("--url", action="store",
                 help="API URI", default=None)
    p.add_option("-d", "--debug", action="store_true",
                 help="enable debug", default=None)
    options, arguments = p.parse_args()

    defaults = {
        'url': 'http://localhost:8000/v1/',
        'debug': False,
    }

    CONFIG = {}
    CONFIG.update(defaults)
    # options override config
    CONFIG.update(dict([(k, v) for k, v in vars(options).items()
                  if v is not None]))
    # base logging to file
    level = logging.INFO
    if CONFIG['debug']:
        level = logging.DEBUG
    logging.basicConfig(format='%(message)s', level=level)

    logging.debug('config: %s' % CONFIG)

    args = {}
    for i, v in enumerate(arguments):
        vs = v.split('=')
        if len(vs) > 1:
            args[vs[0]] = vs[1]

    logging.debug('arguments: %s' % args)

    # get data from HAgent
    r = HAgent(CONFIG['url'])
    response, content = r.rest_connect(args)
    logging.info('header:')
    logging.info(json.dumps(response, sort_keys=True, indent=4))
    logging.info('data:')
    try:
       content_ =  json.loads(content)
    except:
        if content:
            logging.info(content)
        else:
            logging.info('no data')
        exit(1)
    logging.info(json.dumps(content_, sort_keys=True, indent=4))


if __name__ == "__main__":
    main()
