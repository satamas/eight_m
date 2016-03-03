import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Wins, Team


def get_statistic(request):
    dark_wins = Wins.objects.filter(team__side='dark')
    light_wins = Wins.objects.filter(team__side='light')

    response_body = {
        "dark": [win.name for win in dark_wins],
        "light": [win.name for win in light_wins]
    }

    return HttpResponse(
        json.dumps(response_body),
        content_type="application/json"
    )


def add_winner(request):
    event_name = request.GET['eventName']
    side = request.GET['side']
    if side != 'dark' and side != 'light':
        responce = HttpResponse("Wrong side")
        responce.status_code = 400
        return responce
    if Wins.objects.filter(name=event_name).count() > 0:
        responce = HttpResponse("Event winner had already been added", status_code=400)
        responce.status_code = 400
        return responce
    else:
        team, exists = Team.objects.get_or_create(side=side, defaults={"side": side})
        Wins.objects.create(name=event_name, team=team)
        responce = HttpResponse()
        responce.status_code = 200
        return responce
