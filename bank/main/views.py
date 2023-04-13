from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

# import models & serzs
from .models import Banking
from .serializers import BankingSerializer

@api_view(['GET'])
def main(request):
    return Response({"mssg":"hii"})

@api_view(['GET'])
def getData(request):

    # client = {'age':19,'income':25000,'employment length':5,'loan amount':50000,'loan intent':'edu','loan grade':'b'}
    # return Response(client)

    banking = Banking.objects.all()
    serializer = BankingSerializer(banking, many=True)
    return Response(serializer.data)


@api_view(['POST'])
# @api_view(['GET'])
def addData(request):
    # serializer = BankingSerializer(data=request.data)
    # print(f"serdata: {serializer.data}")
    # if serializer.is_valid():
        # serializer.save()
    # return Response(serializer.data)
    # if request.method == "POST":
    age = request.POST["age"]
    income = request.POST["income"]
    employment_length = request.POST["employment_length"]
    loan_amount = request.POST["loan_amount"]
    loan_intent = request.POST["loan_intent"]
    loan_grade = request.POST["loan_grade"]
    loan_intrest = request.POST["loan_intrest"]
    loan_status = request.POST["loan_status"]
    loan_percent_income = request.POST["loan_percent_income"]
    cb_person_default_on_file = request.POST["cb_person_default_on_file"]
    cb_credit_history_len = request.POST["cb_credit_history_len"]
    
    # try:
    # print("req:")
    # print(request.POST)
    obj = Banking.objects.create(age=age, income=income, employment_length=employment_length, loan_amount=loan_amount, loan_intent=loan_intent, loan_grade=loan_grade, loan_intrest=loan_intrest, loan_status=loan_status, loan_percent_income=loan_percent_income, cb_person_default_on_file=cb_person_default_on_file, cb_credit_history_len=cb_credit_history_len)
    print(obj)
    return Response(status=status.HTTP_200_OK)
        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)