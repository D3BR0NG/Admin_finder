#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
        i = 0
        while i<=j:
                print " ",
                i+=1
			  
def cariadmin():
        f = open("goblok.txt","r");
        link = raw_input("Masukan Nama Website \n(ex : example.com or www.example.com ): ")
        print "\n\nAvilable links : \n"
        while True:
                sub_link = f.readline()
                if not sub_link:
                        break
                req_link = "http://"+link+"/"+sub_link
                req = Request(req_link)
                try:
                        response = urlopen(req)
                except HTTPError as e:
                        continue
                except URLError as e:
                        continue
                else:
                        print "OK => ",req_link

def Credit():
        Space(9); print "[][][][][][][][][][][][][][][][][][][][]"
        Space(9); print "[]      A D M I N F I N D E R         []"
        Space(9); print "[]     K A L I A N - N O L E P        []"
        Space(9); print "[]   S C R I P T : Mr.D 3 B R 0 N G   []"
        Space(9); print "[][][][][][][][][][][][][][][][][][][][]"
Credit()
cariadmin()
									
