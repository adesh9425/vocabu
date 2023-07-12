from django.shortcuts import render
import pandas as pd
import random
# Create your views here.
from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404
import requests

import json
from django.http import HttpResponse
from io import BytesIO
from django.contrib import auth
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from django.urls import reverse
import io

from google.oauth2.credentials import Credentials
from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.urls import reverse

from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


import pandas as pd
import random
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import random
import requests
import random
import requests
import pandas as pd
import random
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# CSV file path
CSV_FILE_PATH = r"C:\Users\adesh\vocabu\vocab\static\vocab (2).csv"

def get_random_vocab():
    df = pd.read_csv(CSV_FILE_PATH)
    r = df.iloc[:10].sample(1)
    options = []
    options.append({'value': r['meaning'].values[0], 'image': r['image '].values[0]})
    for i in range(3):
        kk = df.sample(1)
        options.append({'value': kk['meaning'].values[0], 'image': kk['image '].values[0]})
    random.shuffle(options)
    question = r['word'].values[0]
    answer = r['meaning'].values[0]
    image = r['image '].values[0]
    return question, options, answer, image

def update_image_url(answer, image_url):
    df = pd.read_csv(CSV_FILE_PATH)
    df.loc[df['meaning'] == answer, 'image '] = image_url
    df.to_csv(CSV_FILE_PATH, index=False)

@csrf_exempt
def vocab_mcq(request):
    if request.method == 'POST':
        selected_option = request.POST.get('selected_option', '')
        answer = request.POST.get('answer', '')

        if selected_option == answer:
            message = 'Correct!'
            is_correct = True
        else:
            message = 'Wrong!'
            is_correct = False

        custom_image = request.POST.get('custom_image', '')
        if custom_image:
            update_image_url(answer, custom_image)

    else:
        selected_option = None
        answer = None
        message = ''
        is_correct = False

    question, options, correct_answer, image_url = get_random_vocab()

    context = {
        'question': question,
        'options': options,
        'correct_answer': correct_answer,
        'image_url': image_url,
        'message': message,
        'is_correct': is_correct,
        'selected_option': selected_option,
    }

    return render(request, 'vocab_mcq.html', context)
