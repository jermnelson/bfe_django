import json
import os
import bfe_django.settings
import time

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'bfe/index.html', {})


def save(request):
    bibframe_entity = json.loads(request.POST.get('linked_data'))
    filepath = os.path.join(
                bfe_django.settings.BASE_DIR,
                "bfe",
                "ld",
                "{}.json".format(int(time.time())))
    json.dump(
        bibframe_entity,
        open(filepath, "w+"),
        indent=2,
        sort_keys=True)
    return HttpResponse("Saved JSON to {}".format(filepath))