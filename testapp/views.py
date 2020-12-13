from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def emp_data_view(request):
    emp_data = {'eno': 101, 'ename': "yusuf", 'esal': 1000, 'eaddr': 'Mathura'}
    resp = "<h1>Employee Number : {} ,Employee Name : {} ,Employee Salary : {}" \
           " ,Employee Address : {}</h1>".format(emp_data['eno'], emp_data['ename'],
                                           emp_data['esal'], emp_data['eaddr'],)
    return HttpResponse(resp)


import json


def emp_data_json_view(request):
    emp_data = {'eno': 101, 'ename': "yusuf", 'esal': 1000, 'eaddr': 'Mathura'}
    json_date = json.dumps(emp_data)
    return HttpResponse(json_date, content_type='application/json')


# pip install httpie
# pip install requests

from django.http import JsonResponse


def emp_data_json_view1(request):
    emp_data = {'eno': 101, 'ename': "yusuf", 'esal': 1000, 'eaddr': 'Mathura'}

    return JsonResponse(emp_data, content_type='application/json')


from django.views.generic import View
from testapp.mixins import HttpResponseMixin   # Mixins.py
# class Based


class JsonCBV(HttpResponseMixin, View):
    def get(self, request, *args, **kwargs):

        # emp_data = {'eno': 101, 'ename': "yusuf", 'esal': 1000, 'eaddr': 'Mathura'}
        # return JsonResponse(emp_data, content_type='application/json')
        json_data = json.dumps({'msg': 'This Is From Get Method'})
        # return HttpResponse(json_data, content_type='application/json')
        return self.render_to_http_response(json_data)  # Must Use Self Without Self Occur Error

    def post(self, request, *args, **kwargs):      # goto settings and comment middleware csrf line
        json_data = json.dumps({'msg': 'This Is From Post Method'})
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This Is From Put Method'})
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This Is From Delete Method'})
        return HttpResponse(json_data, content_type='application/json')

