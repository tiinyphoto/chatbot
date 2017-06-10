import json
import requests
from django.shortcuts import render

# Create your views here.

from django.template.defaultfilters import pprint
from django.utils.decorators import method_decorator
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class Chat(generic.View):

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

    def check2(self,check, target):
        if target is None:
            return False
        if isinstance(target, dict):
            if check in target:
                return target[check]
        elif isinstance(target, str):
            return target

    def check(self,word, target):
        d = self.check2(word, target)
        temp = d

        while True:

            if d is False:
                return "กรุณาติดต่อเจ้าหน้าที่"
            if d is None:
                arg2 = input("ขอรายละเอียดเพิ่มเติ่ม: ")
                d = self.check2(arg2, temp)
            if isinstance(d, str):
                return d
            else:
                if isinstance(d, dict):
                    temp = d
                    d = self.check2(word, d)
    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        entry = incoming_message['entry']
        for en in entry:
            for messaging in en["messaging"]:
                if "message" in messaging :
                    sender = messaging["sender"]["id"]
                    message = messaging["message"]["text"]
                    #

                    #
                self.post_facebook_message(sender,message)

        return HttpResponse()



