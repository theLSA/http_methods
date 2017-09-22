# -*- coding:utf-8 -*-
#Author:LSA
#Description：http's get,post,put,delete,option,head methods
#Date:20170804
#Version:v1.0

import urllib2
import urllib
import json
import httplib
import requests
import sys
import re
from http import client

def http_get(url):
	rsp = urllib2.urlopen('http://'+url)
	return rsp.read()

def http_post(url):
	data = {'user':'lsa','pwd':'123456'}
	rsp = requests.post('http://'+url,data=data)
	return rsp.content

def http_put(url):
	opener = urllib2.build_opener(urllib2.HTTPHandler)  
	upfilepath = raw_input('upload file path: http://'+url+'/')
	localfilepath = raw_input('local file path: ')
	with open(localfilepath) as f:
		data = f.read()
	rqt = urllib2.Request('http://'+url+'/'+upfilepath,data=data)
	#rqt.add_header("Content-Type", "image/png")
	rqt.get_method = lambda:'PUT'
	#rsp = urllib2.urlopen(rqt)
	#return rsp.read()	
	rsp = opener.open(rqt)
	return rsp.read()

def http_put2(url):
	  
	upfilepath = raw_input('upload file path: http://'+url+'/')
	localfilepath = raw_input('local file path: ')
	with open(localfilepath) as f:
		data = f.read()
	rqt = urllib2.Request('http://'+url+'/'+upfilepath,data=data)
	#rqt.add_header("Content-Type", "image/png")
	rqt.get_method = lambda:'PUT'
	rsp = urllib2.urlopen(rqt)
	return rsp.read()
	#rsp = opener.open(rqt)
	


def http_delete(url):
	header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-cn,zh;q=0.8",
            "Connection": "keep-alive",
        }
	

	#port = url.split(':')[1].split('/')[0]
	delfilepath = raw_input('target delete file path: '+url)
        conn = client.HTTPConnection(url)
        conn.request(method="DELETE", url='http://'+url+delfilepath, headers=header)
        rsp = conn.getresponse().read().decode("utf-8")
	#opener = urllib2.build_opener(urllib2.HTTPHandler)
	#data = {'':''}
	#dataToJson = json.dumps(data)
	#rqt = urllib2.Request('http://'+url+delfilepath)
	#rqt.get_method = lambda:'DELETE'
	#rsp = opener.open(rqt)
	return rsp
	
		


def http_delete2(url):
	delfilepath = raw_input('target delete file path: '+url)
	opener = urllib2.build_opener(urllib2.HTTPHandler)
	#data = {'':''}
	#dataToJson = json.dumps(data)
	rqt = urllib2.Request('http://'+url+delfilepath)
	rqt.get_method = lambda:'DELETE'
	rsp = opener.open(rqt)
	return rsp.read()


	
def http_options(url):
	if ':' in url:
		port = url.split(':')[1].split('/')[0]
		conn = httplib.HTTPConnection(url)
		conn.request("OPTIONS","/")
		rsp = conn.getresponse()
		return rsp.msg.dict
	else:
		conn = httplib.HTTPConnection(url,80)
		conn.request("OPTIONS","/")
		rsp = conn.getresponse()
		return rsp.msg.dict

def http_head(url):
	if ':' in url:
		conn = httplib.HTTPConnection(url)
		conn.request("HEAD","/")
		rsp = conn.getresponse()
		return rsp.msg
	else:		
		conn = httplib.HTTPConnection(url,80)
		conn.request("HEAD","/")
		rsp = conn.getresponse()
		return rsp.msg

def http_copy(url):
	host = url.split(":")[0]
	uploaded_file_path = raw_input('uploaded_file_path: http://'+url+'/')
	dest0 = 'http://'+url+'/'
	dest1 = raw_input('input dest: http://'+url+'/')
	dest = dest0 + dest1
	headers = {'Host':host,'Destination':dest}
	conn = httplib.HTTPConnection(url)
	conn.request("COPY",'/'+uploaded_file_path,"",headers)
	rsp = conn.getresponse()
	return rsp.read()
	
switcher = {'get':http_get,
	    'post':http_post,
            'put':http_put,
	    'delete':http_delete,
	    'options':http_options,
	    'head':http_head,
	    'delete2':http_delete2,
	    'put2':http_put2,
	    'copy':http_copy,
	}

if __name__ == '__main__':
	url = raw_input('target url: ')
	httpMethod = raw_input('http method: ')
	method = switcher.get(httpMethod,lambda(argu):'Error method!')
	rsp = method(url)
	print rsp