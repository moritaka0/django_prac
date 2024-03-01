# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:01:36 2019

@author: takahiromori
"""

from django import forms
from .models import GoodJobMsg

class HelloForm(forms.Form):
    id = forms.IntegerField(label='ID')    
    #name = forms.CharField(label='name')
    #mail = forms.EmailField(label='mail')

class GoodJobForm(forms.Form):
    date = forms.DateField()
    frName = forms.CharField()
    toName = forms.CharField()
    message = forms.CharField()
    cardpath = forms.CharField()
 