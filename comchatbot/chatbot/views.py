import json
import requests
import sqlite3
from django.shortcuts import render

# Create your views here.

from django.template.defaultfilters import pprint
from django.utils.decorators import method_decorator
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt




class Chat(generic.View):

    wifidic = {"เข้าไม่ได้": "ปิดเปิดใหม่", "เชื่อมไม่ได้้": "ปิดเปิดใหม่", "ต่อไม่ติด": "ปิดเปิดใหม่"}
    landic = {"เข้าไม่ได้": "ถอดเสียบใหม่", "เชื่อมไม่ได้้": "ถอดเสียบใหม่", "ต่อไม่ติด": "ถอดเสียบใหม่"}
    internetdic = {"wifi": wifidic, 'lan': landic}
    dict_target = {"internet": internetdic, "wifi": wifidic, 'lan': landic}

    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == 'Chat@botcatflukenior':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')
    def post_facebook_message(self,fbid,message_sender):
        post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAD9lyOabHsBAEVOBXjKG21U4LK9VTThodyXEmZCEZBvH9ZBS2kFJKd8OPumbVhrnJKvLK9PZBlgB2uHkFHfNZArWxQZAb42XQXrwIqTLXpzLoZCFZApw0MF37cz5B2oAgsYLpH2dOG8s7nAVUmxnqGgaogArh7n6qvWZBBkdabLM6wZDZD'
        response_msg = json.dumps({"recipient": {"id": fbid}, "message": {"text": message_sender}})
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
        pprint(status.json())

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)
        # Post function to handle Facebook messages
    def dbcheck(self,q):
        con = sqlite3.connect('dbcheck.db')
        c = con.cursor()
        c.execute("SELECT A FROM fqa WHERE Q = '%s'" % q)
        con.close()
        c.close()
        #return c.fetchone()
    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        entry = incoming_message['entry']
        for en in entry:
            for messaging in en["messaging"]:
                if "message" in messaging :
                    sender = messaging["sender"]["id"]
                    message = messaging["message"]["text"]
                    #

                    #message = self.dbcheck(message)

                self.post_facebook_message(sender,message)

        return HttpResponse()




