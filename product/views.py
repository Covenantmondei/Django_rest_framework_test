from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Product, Student, School
from .serializers import SchoolSerializer, StudentSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView

class Hello(APIView):

    def get(self, request):
        return Response({"message": "Hello, world!"})

    def post(self, request):
        data = request.data
        name = data.get("name")
        print(data)

        return Response({"message": f"Hello, {name}!"})



class Logistic(APIView):

    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def post(self, request):
        try:
            data = request.data
            name = data.get("name")
            email = data.get("email")

            send_mail(
                subject="Covenant Monday From PY50",
                message=f"Hello {name}, your logistics request has been received.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
            # print(name, email)
            # print(request.data)


        except Exception as e:
            print(f"Error sending email: {e}")
            return Response({"error": "Failed to send email"}, status=500)
        return Response({"message": f"Logistics request received for {name}!"}, status=200)
        

@api_view(['POST'])
def create_school(request):
    """This function is to create a School"""
    serializer = SchoolSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": serializer.data}, status=201)
    
    return Response({"error": serializer.errors})

def list_school(request):
    """This function lists all the schools available"""
    serializer = StudentSerializer(data=request.data)


@api_view(['POST'])
def create_student(request):
    school_id = request.data.get('school')
    serializer = StudentSerializer(data=request.data , context={"school": school_id})

    if serializer.is_valid():
        serializer.save()
        return Response({"message": serializer.data}, status=201)
    
    return Response({"error": serializer.errors})


class HelloWorld(APIView):
    def get(self, request):
        return Response({"Message": "Hello World!"})
    

class MarketList(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class CreateMarket(CreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer