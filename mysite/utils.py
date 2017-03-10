# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http  import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.conf import settings
from .forms import *
import random, string
import csv
import numpy as np
import mygene
from mmap import mmap, ACCESS_READ
import itertools
from yattag import indent
import urllib
import fileinput
import ipdb
from compiler.ast import flatten
import zipfile
from StringIO import *
import os
import sys, time
from mysite.models import Hg38, Mm10, Dm3, Ce10, Rn6

# Flatten (flattens list)
def flatten(seq,container=None):
    if container is None:
        container = []
    for s in seq:
        if hasattr(s,'__iter__'):
            flatten(s,container)
        else:
            container.append(s)
    return container

# Example request function
def thanks(request):
	return render(request, 'thanks.html')
    

# Reads the created file and presents as a downloadable link on HTML     
def hg38IDresult(request):
    with open("hg38IDresult.csv", 'r') as f:
        response = HttpResponse(StringIO(f.read()).getvalue(), content_type='text/csv')
        response['Content-Disposition']='attachment; filename=hg38IDresult.csv'
        return response

def mm10IDresult(request):
    with open("mm10IDresult.csv", 'r') as f:
        response = HttpResponse(StringIO(f.read()).getvalue(), content_type='text/csv')
        response['Content-Disposition']='attachment; filename=mm10IDresult.csv'
        return response


def dm3IDresult(request):
    with open("dm3IDresult.csv", 'r') as f:
        response = HttpResponse(StringIO(f.read()).getvalue(), content_type='text/csv')
        response['Content-Disposition']='attachment; filename=dm3IDresult.csv'
        return response

def ce10IDresult(request):
    with open("ce10IDresult.csv", 'r') as f:
        response = HttpResponse(StringIO(f.read()).getvalue(), content_type='text/csv')
        response['Content-Disposition']='attachment; filename=ce10IDresult.csv'
        return response

def rn6IDresult(request):
    with open("rn6IDresult.csv", 'r') as f:
        response = HttpResponse(StringIO(f.read()).getvalue(), content_type='text/csv')
        response['Content-Disposition']='attachment; filename=rn6IDresult.csv'
        return response

#==================================================================================================================

def hg38LOCresult(request):
    with open("hg38LOCresult.csv", 'r') as f:
        response = HttpResponse(StringIO(f.read()).getvalue(), content_type='text/csv')
        response['Content-Disposition']='attachment; filename=hg38LOCresult.csv'
        return response

def mm10LOCresult(request):
    with open("mm10LOCresult.csv", 'r') as f:
        response = HttpResponse(StringIO(f.read()).getvalue(), content_type='text/csv')
        response['Content-Disposition']='attachment; filename=mm10LOCresult.csv'
        return response


def dm3LOCresult(request):
    with open("dm3LOCresult.csv", 'r') as f:
        response = HttpResponse(StringIO(f.read()).getvalue(), content_type='text/csv')
        response['Content-Disposition']='attachment; filename=dm3LOCresult.csv'
        return response

def ce10LOCresult(request):
    with open("ce10LOCresult.csv", 'r') as f:
        response = HttpResponse(StringIO(f.read()).getvalue(), content_type='text/csv')
        response['Content-Disposition']='attachment; filename=ce10LOCresult.csv'
        return response

def rn6LOCresult(request):
    with open("rn6LOCresult.csv", 'r') as f:
        response = HttpResponse(StringIO(f.read()).getvalue(), content_type='text/csv')
        response['Content-Disposition']='attachment; filename=rn6LOCresult.csv'
        return response
