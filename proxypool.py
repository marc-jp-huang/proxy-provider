#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests, sys
from proxylist import ProxyList

class proxypool(object):
	def __init__(self,file_path):
		self.pl = ProxyList()
		self.proxy_file = file_path
	def loadProxy(self):
		self.pl.load_file(self.proxy_file)
		self.pl.random()
	def getProxy(self):
		if(len(self.pl)==0):
			self.loadProxy()
		return self.pl.random().address()

class fetchweb(object):
	def __init__(self,target_url,proxy):
		#set proxy
		self.proxies={'http':'http://'+proxy,'https':'https://'+proxy}
		self.target_url = target_url
	def fetch(self):
		try:
			#request url through proxy
			r = requests.get(self.target_url,proxies=self.proxies,timeout=1)
			if(r.status_code == 200):
				return r.text
			else:
				return str({'response':self.r.status_code})
		except Exception as e:
			return str({'error':str(e)})

if __name__ == '__main__':
	#encoding handling
	reload(sys)
	sys.setdefaultencoding('utf-8')
	#the page you want to fetch
	target_url = 'https://twitter.com/'
	#local proxy list
	proxy_file = 'proxy.txt'
	pp = proxypool(proxy_file)
	#get proxy
	proxy = pp.getProxy()
	fw = fetchweb(target_url,proxy)
	f = open('result', 'w')
	#fetch and write result
	f.write(fw.fetch())
	f.close()

