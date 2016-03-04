import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Wins, Team, Event


def get_statistic(request):
    dark_wins = Wins.objects.filter(team__side='dark')
    light_wins = Wins.objects.filter(team__side='light')

    response_body = {
        "dark": [{"event": win.event.name, "rate": win.rate} for win in dark_wins],
        "light": [{"event": win.event.name, "rate": win.rate} for win in light_wins]
    }

    return HttpResponse(
        json.dumps(response_body),
        content_type="application/json"
    )


def add_winner(request):
    event_name = request.GET['eventName']
    side = request.GET['side']
    rate = request.GET["rate"] if "rate" in request.GET else None
    if side != 'dark' and side != 'light':
        responce = HttpResponse("Wrong side")
        responce.status_code = 400
        return responce
    else:
        event, exists = Event.objects.get_or_create(name=event_name, defaults={"name": event_name})
        team, exists = Team.objects.get_or_create(side=side, defaults={"side": side})
        Wins.objects.create(event=event, team=team, rate=rate)
        responce = HttpResponse()
        responce.status_code = 200
        return responce
