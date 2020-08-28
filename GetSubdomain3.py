# -*- coding: utf-8 -*-

import urllib.request
import json
import sys
import os

'''
description:基于百度云观测接口获取子域名(Python3)
Src:http://ce.baidu.com/index/getRelatedSites?site_address=xxx.xxx
'''


def GetSubdomain(domain):
    url = 'http://ce.baidu.com/index/getRelatedSites?site_address=%s' % domain
    res = urllib.request.urlopen(url).read()
    return res


def DownSubdomain(domain_json, outfile):
    with open(outfile, 'w') as f:
        obj_json = json.loads(domain_json)
        domain_list = obj_json.get("data")
        print ('[+] Number of subdomains: {}'.format(len(domain_list)))
        for domain in domain_list:
            f.write(domain.get('domain'))
            f.write('\n')
        print ("[+] Successfully exported to {}".format(outfile))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ('Usag: python GetSubdomain.py xxx.com')
        exit()

    target_domain = sys.argv[1]
    outfile = "{}.txt".format(sys.argv[1])
    if os.path.exists(outfile):
        os.remove(outfile)
    domain_json = GetSubdomain(target_domain)
    DownSubdomain(domain_json, outfile)
