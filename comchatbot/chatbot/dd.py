import json
import requests
import sqlite3
import re
from django.shortcuts import render

# Create your views here.

from django.template.defaultfilters import pprint
from django.utils.decorators import method_decorator
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt


message="hi"
con = sqlite3.connect('dbcheck.db')
c = con.cursor()
c.execute("SELECT A FROM fqa WHERE Q = '%s'" % message)
ms1=str(c.fetchone())
a = re.sub('\W+', "", ms1, 0)
print(a)