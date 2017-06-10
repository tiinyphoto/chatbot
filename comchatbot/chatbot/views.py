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
        post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAMCsghqLRABABcpCDZB5iZBdRpfftcK2xFfPvo5SUTTotQRX9G2X8ycDT9OB55A5zH5Vl4xo340D9wZCMnW7JPj41k8xcIRZB8IDTca5ezfBTndPvkVVBzdfwjICjqiw32ySx2Qqb9YAvkN39kztbEykuNZCpJCqZBNyi36jYfwZDZD'
        response_msg = json.dumps({"recipient": {"id": fbid}, "message": {"text": message_sender}})
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
        pprint(status.json())

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)
        # Post function to handle Facebook messages

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
