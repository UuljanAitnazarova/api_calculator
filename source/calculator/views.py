import json
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import ensure_csrf_cookie


def add_view(request, *args, **kwargs):
    if request.method == 'POST':
            numbers = json.loads(request.body)
            num1 = numbers['A']
            num2 = numbers['B']
            if num1 and num2:
                try:
                    answer = {'answer': int(num1) + int(num2)}
                    return JsonResponse(answer)
                except ValueError:
                    response = JsonResponse({'error': 'HTTP 400 Bad Request'})
                    response.status_code = 400
                    return response
            else:
                response = JsonResponse({'error': 'No data provided!'})
                response.status_code = 400
                return response


def subtract_view(request, *args, **kwargs):
    if request.method == 'POST':
        numbers = json.loads(request.body)
        num1 = numbers['A']
        num2 = numbers['B']
        if num1 and num2:
            try:
                answer = {'answer': int(num1) - int(num2)}
                return JsonResponse(answer)
            except ValueError:
                response = JsonResponse({'error': 'HTTP 400 Bad Request'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response

def multiply_view(request, *args, **kwargs):
    if request.method == 'POST':
        numbers = json.loads(request.body)
        num1 = numbers['A']
        num2 = numbers['B']
        if num1 and num2:
            try:
                answer = {'answer': int(num1) * int(num2)}
                return JsonResponse(answer)
            except ValueError:
                response = JsonResponse({'error': 'HTTP 400 Bad Request'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response


def divide_view(request, *args, **kwargs):
    if request.method == 'POST':
        numbers = json.loads(request.body)
        num1 = numbers['A']
        num2 = numbers['B']
        if num1 and num2:
            try:
                if int(num2) != 0:
                    answer = {'answer': int(num1) / int(num2)}
                    return JsonResponse(answer)
                else:
                    answer = {'error': 'Division by 0!'}
                    response = JsonResponse(answer)
                    response.status_code = 400
                    return response
            except ValueError:
                response = JsonResponse({'error': 'HTTP 400 Bad Request'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response




@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')