from django.shortcuts import render
from django.http import HttpResponse
from subprocess import check_output


# Create your views here.

def classfiy(requests):
    return HttpResponse(check_output(["python", "/home/sprout/tmp/tensorflow_object/research/object_detection/go.py",
                                      "/var/www/html/data-ton-in-jeju/pic1.jpeg"]))