#!/usr/bin/env python 
#coding=utf-8

import requests, json, time, os

last_id = 0

def getRecent():
	r = requests.get('http://thegeneralopinion.com/api/posts/recent')
	return r.json()

def setupPrinter(last_id):
	post_id = getRecent()['id']

	if post_id > last_id:
		printer()
	else:
		pass
	
	last_id = post_id

	return last_id

def printer():
	name = getRecent()['name']
	body = getRecent()['body']
	os.system('say "' + body + '"')

while 1:	
	last_id = setupPrinter(last_id)
	time.sleep(2)
