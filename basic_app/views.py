from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Card
from .serializers import CardSerializer
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, "basic_app/base.html")

@csrf_exempt
def cardApi(request, id=0):
    if request.method == 'GET':
        cards = Card.objects.all()
        cards_serializer = CardSerializer(cards, many=True)
        return JsonResponse(cards_serializer.data, safe=False)

    elif request.method == 'POST':
        card_data = JSONParser().parse(request)
        card_serializer = CardSerializer(data=card_data)
        print(card_serializer)
        if card_serializer.is_valid():
            card_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed', safe=False)

    elif request.method == 'PUT':
        card_data = JSONParser().parse(request)
        card = Card.objects.get(card_id = card_data['card_id'])
        card_serializer = CardSerializer(card, data = card_data)
        if card_serializer.is_valid():
            card_serializer.save()
            return JsonResponse('Updated successfully', safe=False)
        return JsonResponse('failed to update', safe=False)

    elif request.method == 'DELETE':
        card = Card.objects.get(card_id = id)
        card.delete()
        return JsonResponse('deleted!', safe=False)