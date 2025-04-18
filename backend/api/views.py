from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from pymongo import MongoClient

client = MongoClient("mongodb+srv://placement_tracker:placement_tracker@cluster0.hrxkgqx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["FormDatabase"]
collection = db["FormCollection"]


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
#     data={
#   "date": "2025-04-18T08:43:16.108Z",
#   "reportedBy": "dsfsdfs",
#   "snsceOffersReceived": "dsf",
#   "snsctOffersReceived": "dfsdf",
#   "unplacedSNSCE": "sdfs",
#   "unplacedSNSCT": "dfsdf",
#   "awaitedResults": "sdfsdfs",
#   "offersTodayInternships": "dfsdf",
#   "totalSinceAprilInternships": "dsfsd",
#   "internshipRemarks": "fsdfsd",
#   "offersTodayHighSalary": "fd",
#   "totalSinceAprilHighSalary": "sfdsf",
#   "highSalaryRemarks": "sdfsdfs",
#   "internshipUpdates": [
#     {
#       "company": "dfsdf",
#       "department": "sdf",
#       "numberOfStudents": "sdf",
#       "status": "sdf"
#     }
#   ]
# }
    collection.insert_one(data)
    return Response({"status": "Data added"}, status=status.HTTP_201_CREATED)





