#!/usr/bin/env python 
#coding=utf-8

import requests, json, time, os

last_id = 0

def getRecent():
	r = requests.get('http://thegeneralopinion.com/api/posts/recent')
	return r.json()

def setupPrinter(last_id):
	post_id = getRecent()['id']
	name = getRecent()['name']
	body = getRecent()['body']

	if post_id > last_id:
		print_(name,body)
	else:
		pass
	
	last_id = post_id

	return last_id

def print_(name, body):	
	p = printer.ThermalPrinter(serialport="/dev/ttyAMA0")
	name_text = textwrap.fill(name, 32)
	body_text = textwrap.fill(body, 32)
	spaces = "                                "
	cut = "- - - - - - - - - - - - - - - - "
	spaces_text = textwrap.fill(spaces, 32)
	cut_text = textwrap.fill(cut, 32)
	print name + spaces +body
	os.system('say "' + name + spaces +body + '"')

	p.bold_on()
	p.print_text(name_text)
	p.bold_off()
	p.linefeed()
	p.underline_on()
	p.print_text(spaces_text)
	p.underline_off()
	p.linefeed()
	p.print_text(body_text)
	p.linefeed()
	p.print_text(spaces_text)
	# p.print_text(wrapped_text)
	# p.linefeed()



while 1:	
	last_id = setupPrinter(last_id)
	time.sleep(2)