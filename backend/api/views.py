from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]


# Create your views here.
@api_view(['GET'])
def health_check(request):
    return Response({"status": "Working"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_data(request):
    data = list(collection.find({}, {"_id": 0}))
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_data(request):
    data = request.data
    collection.insert_one(data)
    return Response({"status": "Data added"}, status=status.HTTP_201_CREATED)





