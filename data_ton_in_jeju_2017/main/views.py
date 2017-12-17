from django.shortcuts import render
from django.http import HttpResponse
from subprocess import check_output
from item import getItemPrice
from django.views.decorators.csrf import csrf_exempt
import base64 as b64
import random
import json


# Create your views here.
@csrf_exempt
def classify(requests):
    fname = "images/%s.jpeg"%(random.randint(1, 10000000))
    with open(fname, "wb") as f:
        f.write(b64.b64decode(requests.POST["data"]))
    product = check_output(["python", "/home/sprout/tmp/tensorflow_object/research/object_detection/go.py", fname])
    print("saved", label)
    return HttpResponse(str(getItemPrice(product.strip().decode())))