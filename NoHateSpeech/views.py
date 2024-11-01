# NoHateSpeech/views.py
from django.http import JsonResponse
from django.shortcuts import render
import json
from .main import pipe, changeimti  # main.py에 있는 함수와 변수를 가져오기
from django.shortcuts import render

def home_view(request):
    return render(request, 'NoHateSpeech.html')

def check_value_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('user_input', '')
        predictions = pipe(user_input)
        result = predictions[0]
        keytype = max(result, key=lambda x: x['score'])['label']

        if max(result, key=lambda x: x['score'])['score'] >= 0.5:
            response_value = changeimti.get(keytype, user_input)
        else:
            response_value = user_input

        return JsonResponse({'response': response_value}, safe=False)

    return render(request, 'NoHateSpeech.html')
