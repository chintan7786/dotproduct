from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Card
from .serializers import CardSerializer
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, "basic_app/index.html")

@csrf_exempt
def cardApi(request, id=0):
    if request.method == 'GET':
        cards = Card.objects.all()
        cards_serializer = CardSerializer(cards, many=True)
        return JsonResponse(cards_serializer.data, safe=False)
    elif request.method == 'POST':
        pass