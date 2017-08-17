#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Created : Tue 25 Jul 2017 02:19:40 PM EDT
# Modified: Tue 15 Aug 2017 11:50:44 AM EDT

from __future__ import print_function

import better_exceptions
import nmap
import os
import time
import pickle
from pathlib import Path
from printColor import printColor
from openwithheader import openWithHeader


class NotSudo(Exception):
    pass


def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]


def main():
    try:
        if os.getuid() != 0:
            raise NotSudo("This program is not run as sudo")

        nm = nmap.PortScanner()

        hosts_seen = {}
        f = Path('host_discovery.p')
        if f.is_file():
            with open('host_discovery.p', 'rb') as pfile:
                hosts_seen = pickle.load(pfile)

        with openWithHeader('host_discovery.csv', '\"Date\",\"IP Address\",\"Host name\"') as hd_log:
            while(True):
                nm.scan(hosts='192.168.1.1/24', arguments='-T4 -F')

                i = 0
                for host in nm.all_hosts():
                    if host not in hosts_seen:
                        t = time.asctime()
                        printColor('green', '{}  {}\t{}'.format(t, host, nm[host].hostname()))
                        print('\"{}\",\"{}\",\"{}\"'.format(t, host, nm[host].hostname()), file=hd_log)
                        hosts_seen[host] = nm[host].hostname()
                    i += 1

                printColor('cyan', 'Previous seen hosts now not active:')
                for host in diff(hosts_seen.keys(), nm.all_hosts()):
                    printColor('cyan', '\t{}\t{}'.format(host, hosts_seen[host]))

                t = time.asctime()
                printColor('yellow', '{}  {} hosts scanned'.format(t, i))

                time.sleep(30)
    except KeyboardInterrupt:
        with open('host_discovery.p', 'wb') as pfile:
            pickle.dump(hosts_seen, pfile)


if __name__ == '__main__':
    main()
