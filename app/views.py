#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, requests, random, re
from pprint import pprint

from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
from random import randint

import re # added for regular expression




PAGE_ACCESS_TOKEN = 'EAANaQeDieLUBAItYpMXGElEWDQGtZBiGVmVVqqO4lNky1Lh3hxD0gLImrv5VZCHmKMFt9FgsE3nX8VqAjjbe4qtm4dZBlI6HPERZA6in4NSZCg4rq7guhR3ZBeZC6yw5Rd9GaE6tWxnZBRsvMhmeSVRNNlFP8LDpTj4ZCZCOSCjl0sLgZDZD'
VERIFY_TOKEN = '8447789934m'

def logg(mess,meta='log',symbol='#'):
  print '%s\n%s\n%s'%(symbol*20,mess,symbol*20)

def index(request):
    #set_greeting_text()
    post_facebook_message('100006427286608','mango')
    output_response = 'Hi'
    return HttpResponse(output_response,content_type='application/json')


def set_greeting_text():
    post_message_url = "https://graph.facebook.com/v2.6/me/thread_settings?access_token=%s"%PAGE_ACCESS_TOKEN
    greeting_text = "Hello and welcome to HelloMeets Bot"
    greeting_object = json.dumps({"setting_type":"greeting", "greeting":{"text":greeting_text}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=greeting_object)
    pprint(status.json())

def get_coordinates(message):
	#x1 = randint(0,99)
    #x2 = randint(0,99)
    #y1 = randint(0,99)
    #y2 = randint(0,99)

    x1 = re.search( r'x1:([0-9]{1,3})', coordinates, re.M|re.I|re.U)
	x1 = x1.group(1)
	

	y1 = re.search( r'y1:([0-9]{1,3})', coordinates, re.M|re.I|re.U)
	y1 = y1.group(1)


	x2 = re.search( r'x2:([0-9]{1,3})', coordinates, re.M|re.I|re.U)
	x2 = x2.group(1)


	y2 = re.search( r'y2:([0-9]{1,3})', coordinates, re.M|re.I|re.U)
	y2 = y2.group(1)
    return x1,y1,x2,y2

def post_facebook_message(fbid, recevied_message):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    recevied_message = re.sub(r"[^a-zA-Z0-9\s]",' ',recevied_message).lower()

    x1,y1,x2,y2 = get_coordinates(recevied_message)

    response_msg  = {
                      "recipient":{
                        "id":fbid
                      },
                      "message":{
                        "attachment":{
                          "type":"image",
                          "payload":{
                            "url":"http://chestream.cloudapp.net:5000/?x1=%s&y1=%s&x2=%s&y2=%s"%(x1,y1,x2,y2)
                          }
                        }
                      }
                    }

    response_msg = json.dumps(response_msg)
    #response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":response_text}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)

class BotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        incoming_message= json.loads(self.request.body.decode('utf-8'))
        
        logg(incoming_message)

        for entry in incoming_message['entry']:
            for message in entry['messaging']:

                try:
                    sender_id = message['sender']['id']
                    message_text = message['message']['text']
                    post_facebook_message(sender_id,message_text) 
                except Exception as e:
                    logg(e,symbol='-332-')

        return HttpResponse()



