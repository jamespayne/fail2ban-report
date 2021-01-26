#!/usr/bin/python3
# coding: utf-8
# Julien Pecqueur <julien@peclu.net>

from sys import argv
from os import path

if len(argv) != 2:
    print("Usage: fail2ban-getlog <file>")
    print("Extract fail2ban logs to CSV file.")
else:
    F_LOG = "/var/log/fail2ban.log"
    f_old = argv[1]
    old = []
    if not path.exists('./log.csv'):
        open(f_old, 'a').close()
    else:
        f_old = open(argv[1], "r")
        for l in f_old:
            old.append(l[0:-1])
        f_old.close()
        print(len(old), "existing line(s).")
    f_in = open(F_LOG, "r")
    f_out = open(argv[1], "a+")
    c = 0
    for l in f_in:
        l = l[0:-1].split(" ")
        if "Ban" in l:
            l = l[-1]+";"+l[0]+";"+l[1][0:-4]
            if not l in old:
                f_out.write(l+"\n")
                c += 1
    f_in.close()
    f_out.close() 
    print("Added", c, "new line(s).")
