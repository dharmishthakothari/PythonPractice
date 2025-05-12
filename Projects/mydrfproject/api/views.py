from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from base.models import Item

@api_view(['GET'])
def getData(request):
    #person = {'name':'dharmishtha', 'city' : 'Ahmedabad'} 
    #return Response(person)
    items = Item.objects.all()
    serializer = ItemSerializer(items,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteItem(request,pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return Response("Item successfully deleted ")
