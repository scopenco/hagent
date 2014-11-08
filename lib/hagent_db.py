#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Set of fuctions for txt database administration
Author: Andrey Skopenko <andrey@scopenco.net>
'''

from os import access, W_OK, R_OK
import logging
from time import sleep
import sys
sys.path.insert(0, '/usr/local/hagent/lib')
from cli import FileLock


def add_record(db, service_name, service_value, service_attr):
    '''Add record to db.'''

    logging.debug('func add_record (%s, %s, %s)' % (
                  service_name, service_value, service_attr))
    output = {}

    if not access(db, R_OK):
        content = []
    else:
        with open(db, 'r') as f:
            content = f.readlines()

    # return error if exist
    for line in content:
        args = line.strip().split()
        if args[0] == service_name and args[1] == service_value:
            output['status'] = 1
            output['status_msg'] = '%s %s exist' % (
                service_name, service_value)
            return output

    # wait lock file
    fl = FileLock('%s.lock' % db)
    while not fl.lock():
        logging.debug('waiting write access to %s for %s secs' % (db, 1))
        sleep(1)

    # write new data
    logging.debug('write %r', db)
    try:
        with open(db, 'a') as f:
            f.write('%s %s %s\n' % (service_name,
                    service_value,
                    ' '.join('%s=%s' % (
                        m, service_attr[m]) for m in service_attr.keys())))
    except IOError, e:
        fl.unlock()
        output['status'] = 1
        output['status_msg'] = str(e)
        return output

    # unlock
    fl.unlock()

    output['status'] = 0
    output['status_msg'] = '%s %s created' % (service_name, service_value)
    return output


def del_record(db, service_name, service_value):
    '''Delete service to data file.'''

    logging.debug('func del_record (%s, %s)' % (service_name, service_value))
    output = {}

    if not access(db, R_OK):
        content = []
    else:
        with open(db, 'r') as f:
            content = f.readlines()

    attr_exist = False
    content_modified = []
    for line in content:
        args = line.strip().split()
        if args[0] != service_name:
            content_modified.append(line)
        else:
            if args[1] != service_value:
                content_modified.append(line)
            else:
                attr_exist = True

    if not attr_exist:
        output['status'] = 0
        output['status_msg'] = '%s %s not found' % (
            service_name, service_value)
        return output

    # wait lock file
    fl = FileLock('%s.lock' % db)
    while not fl.lock():
        logging.debug('waiting write access to %s for %s secs' % (db, 1))
        sleep(1)

    logging.debug('write %r', db)
    try:
        with open(db, 'w') as f:
            f.writelines(content_modified)
    except IOError, e:
        fl.unlock()
        output['status'] = 1
        output['status_msg'] = str(e)
        return output

    # unlock
    fl.unlock()

    output['status'] = 0
    output['status_msg'] = '%s %s removed' % (service_name, service_value)
    return output


def update_record(db, service_name, service_value,
                  service_attr, remove_attr=False):
    '''Change attribute in data file.'''

    logging.debug('func update_record (%s, %s, %s)' % (
        service_name, service_value, service_attr))
    output = {}

    if not access(db, R_OK):
        content = []
    else:
        with open(db, 'r') as f:
            content = f.readlines()

    content_modified = []
    for line in content:
        args = line.strip().split()
        if args[0] != service_name:
            content_modified.append(line)
        else:
            if args[1] != service_value:
                content_modified.append(line)
            else:
                # update record
                cur_attrs = {}

                if not remove_attr:
                    # add new attr and change exist
                    for k in args[2:]:
                        attrs = k.strip().split('=')
                        if len(attrs) < 2:
                            cur_attrs[attrs[0]] = None
                        else:
                            cur_attrs[attrs[0]] = attrs[1]

                # update cur_attrs
                cur_attrs.update(service_attr)
                # append to content_modified
                content_modified.append('%s %s %s\n' % (
                    service_name, service_value,
                    ' '.join('%s=%s' % (
                        m, cur_attrs[m]) for m in cur_attrs.keys())))

    # wait lock file
    fl = FileLock('%s.lock' % db)
    while not fl.lock():
        logging.debug('waiting write access to %s for %s secs' % (db, 1))
        sleep(1)

    logging.debug('write %r', db)
    try:
        with open(db, 'w') as f:
            f.writelines(content_modified)
    except IOError, e:
        fl.unlock()
        output['status'] = 1
        output['status_msg'] = str(e)
        return output

    # unlock
    fl.unlock()

    output['status'] = 0
    output['status_msg'] = '%s %s modified' % (service_name, service_value)
    return output


def get_record_attr(db, service_name, service_value):
    '''Get service attr to data file.'''

    logging.debug('func get_record_attr (%s, %s)' % (
        service_name, service_value))
    output = {}

    if not access(db, R_OK):
        content = []
    else:
        with open(db, 'r') as f:
            content = f.readlines()

    cur_attrs = {}
    for line in content:
        args = line.strip().split()
        if args[0] == service_name and args[1] == service_value:
            for k in args[2:]:
                attrs = k.strip().split('=')
                if len(attrs) < 2:
                    cur_attrs[attrs[0]] = None
                else:
                    cur_attrs[attrs[0]] = attrs[1]
            cur_attrs['status'] = 0
            return cur_attrs

    output['status'] = 1
    output['status_msg'] = '%s %s not found' % (service_name, service_value)
    return output


def get_account_resources(db, account, locked=0):
    '''Get resources (-locked) for account.'''

    logging.debug('func get_account_resources (%s)' % account)
    output = {}

    if not access(db, W_OK):
        output['status'] = 1
        output['status_msg'] = 'Can not write to %s' % db
        return output

    with open(db, 'r') as f:
        content = f.readlines()

    resources = {'Domain': [], 'Ip': [], 'MySQLDb': [], 'MailDomain': []}

    args_d = {}
    for l in range(len(content)):
        args = content[l].strip().split()

        if args[0] == 'Domain':
            args_d.clear()
            for k in args[2:]:
                attrs = k.strip().split('=')
                if len(attrs) == 2:
                    args_d[attrs[0]] = attrs[1]
            if ('account', account) in args_d.items():
                if locked:
                    resources['Domain'].append(args[1])
                else:
                    if ('state', 'on') in args_d.items():
                        resources['Domain'].append(args[1])

        if args[0] == 'Ip':
            args_d.clear()
            for k in args[2:]:
                attrs = k.strip().split('=')
                if len(attrs) == 2:
                    args_d[attrs[0]] = attrs[1]
            if ('account', account) in args_d.items():
                resources['Ip'].append(args[1])

        if args[0] == 'MySQLDb':
            args_d.clear()
            for k in args[2:]:
                attrs = k.strip().split('=')
                if len(attrs) == 2:
                    args_d[attrs[0]] = attrs[1]
            if ('account', account) in args_d.items():
                if locked:
                    resources['MySQLDb'].append(args[1])
                else:
                    if ('state', 'on') in args_d.items():
                        resources['MySQLDb'].append(args[1])

        if args[0] == 'MailDomain':
            args_d.clear()
            for k in args[2:]:
                attrs = k.strip().split('=')
                if len(attrs) == 2:
                    args_d[attrs[0]] = attrs[1]
            if ('account', account) in args_d.items():
                if locked:
                    resources['MailDomain'].append(args[1])
                else:
                    if ('state', 'on') in args_d.items():
                        resources['MailDomain'].append(args[1])

    if locked:
        logging.debug('resources for account %s with locked = %s' % (
            account, resources))
    else:
        logging.debug('resources for account %s = %s' % (account, resources))
    output['status'] = 0
    output.update(resources)
    return output


def get_domain_resources(db, domain, locked=0):
    '''Get resources (-locked) for domain.'''

    logging.debug('func get_domain_resources (%s)' % domain)
    output = dict()

    if not access(db, W_OK):
        output['status'] = 1
        output['status_msg'] = 'Can not write to %s' % db
        return output

    with open(db, 'r') as f:
        content = f.readlines()

    resources = {'DomainAlias': [], 'SubDomain': [], 'Cron': []}

    args_d = {}
    for l in range(len(content)):
        args = content[l].strip().split()

        if args[0] == 'DomainAlias':
            args_d.clear()
            for k in args[2:]:
                attrs = k.strip().split('=')
                if len(attrs) == 2:
                    args_d[attrs[0]] = attrs[1]
            if ('domain', domain) in args_d.items():
                resources['DomainAlias'].append(args[1])

        if args[0] == 'SubDomain':
            args_d.clear()
            for k in args[2:]:
                attrs = k.strip().split('=')
                if len(attrs) == 2:
                    args_d[attrs[0]] = attrs[1]
            if ('domain', domain) in args_d.items():
                if locked:
                    resources['SubDomain'].append(args[1])
                else:
                    if ('state', 'on') in args_d.items():
                        resources['SubDomain'].append(args[1])

        if args[0] == 'Cron':
            args_d.clear()
            for k in args[2:]:
                attrs = k.strip().split('=')
                if len(attrs) == 2:
                    args_d[attrs[0]] = attrs[1]
            if ('domain', domain) in args_d.items():
                resources['Cron'].append(args[1])

    if locked:
        logging.debug('resources for domain %s with locked = %s' % (
            domain, resources))
    else:
        logging.debug('resources for domain %s = %s' % (domain, resources))
    output['status'] = 0
    output.update(resources)
    return output


def get_records(db, service_name):
    '''Get records from data file.'''

    logging.debug('func get_records (%s)' % service_name)
    output = {}

    if not access(db, W_OK):
        output['status'] = 1
        output['status_msg'] = 'Can not write to %s' % db
        return output

    with open(db, 'r') as f:
        content = f.readlines()

    output[service_name] = []

    for l in range(len(content)):
        args = content[l].strip().split()
        if args[0] == service_name:
            output[service_name].append(args[1])

    output['status'] = 0
    return output


def get_record_ip_shared(db, service_name='Ip'):
    '''Get recorts from data file.'''

    logging.debug('func get_record_ip_shared')
    output = {}

    if not access(db, W_OK):
        output['status'] = 1
        output['status_msg'] = 'Can not write to %s' % db
        return output

    with open(db, 'r') as f:
        content = f.readlines()

    output[service_name] = []
    for l in range(len(content)):
        args = content[l].strip().split()
        if args[0] == service_name:
            for k in args[2:]:
                attrs = k.strip().split('=')
                if len(attrs) == 2:
                    if attrs[0] == 'account' and attrs[1] == 'shared':
                        output[service_name].append(args[1])

    if len(output[service_name]) > 0:
        output['status'] = 0
    else:
        output['status'] = 1
        output['status_msg'] = 'no shared ip found'

    logging.debug('found ip %s' % output[service_name])
    return output


def get_maildomain_resources(db, domain, locked=0):
    '''Get resources (-locked) for mail domain.'''

    logging.debug('func get_maildomain_resources (%s)' % domain)
    output = {}

    if not access(db, W_OK):
        output['status'] = 1
        output['status_msg'] = 'Can not write to %s' % db
        return output

    with open(db, 'r') as f:
        content = f.readlines()

    resources = {'MailUser': [], 'MailUserAlias': [], 'MailDomainAlias': []}

    args_d = {}
    for l in range(len(content)):
        args = content[l].strip().split()

        if args[0] == 'MailUser':
            args_d.clear()
            for k in args[2:]:
                attrs = k.strip().split('=')
                if len(attrs) == 2:
                    args_d[attrs[0]] = attrs[1]
            if ('maildomain', domain) in args_d.items():
                if locked:
                    resources['MailUser'].append(args[1])
                else:
                    if ('state', 'on') in args_d.items():
                        resources['MailUser'].append(args[1])

        if args[0] == 'MailUserAlias':
            args_d.clear()
            for k in args[2:]:
                attrs = k.strip().split('=')
                if len(attrs) == 2:
                    args_d[attrs[0]] = attrs[1]
            if ('maildomain', domain) in args_d.items():
                if locked:
                    resources['MailUserAlias'].append(args[1])
                else:
                    if ('state', 'on') in args_d.items():
                        resources['MailUserAlias'].append(args[1])

        if args[0] == 'MailDomainAlias':
            args_d.clear()
            for k in args[2:]:
                attrs = k.strip().split('=')
                if len(attrs) == 2:
                    args_d[attrs[0]] = attrs[1]
            if ('maildomain', domain) in args_d.items():
                if locked:
                    resources['MailDomainAlias'].append(args[1])
                else:
                    if ('state', 'on') in args_d.items():
                        resources['MailDomainAlias'].append(args[1])

    if locked:
        logging.debug('resources for mail domain %s with locked = %s' % (
            domain, resources))
    else:
        logging.debug('resources for mail domain %s = %s' % (
            domain, resources))
    output['status'] = 0
    output.update(resources)
    return output


if __name__ == "__main__":
    print __doc__
