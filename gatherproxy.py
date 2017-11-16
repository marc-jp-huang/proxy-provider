#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re, requests, sys

class GatherProxy(object):
	header={'headers':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
	'''To get proxy from http://gatherproxy.com/'''
	url='http://www.gatherproxy.com/'
	re1=re.compile(r'insertPrx\(\{.*?\}\)')
	ip=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	port=re.compile(r'"PROXY_PORT":"[a-fA-F0-9]+"')
	port_hex=re.compile(r'[a-fA-F0-9]+')
	def getlist(self):
		'''Get Elite Anomy proxy
		Pages define how many pages to get
		Uptime define the uptime(L/D)
		fast define only use fast proxy with short reponse time'''
		proxies=set()
		r=requests.get(self.url,headers=self.header,timeout=1)
		for row in self.re1.findall(r.text):
			proxy_ip = self.ip.findall(row)[0]
			proxy_port = self.port.findall(row)[0]
			proxy_port_hex = self.port_hex.findall(proxy_port)[0]
			proxy = proxy_ip+':'+str(int(proxy_port_hex, 16))
			proxies.add(proxy)
		return proxies