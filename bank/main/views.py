from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from . import classifiers
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
    #     serializer.save()
    # return Response(serializer.data)
    # if request.method == "POST":
    age = request.data["age"]
    income = request.data["income"]
    employment_length = request.data["employment_length"]
    loan_amount = request.data["loan_amount"]
    loan_intent = request.data["loan_intent"]
    loan_grade = request.data["loan_grade"]
    loan_intrest = request.data["loan_intrest"]
    loan_status = request.data["loan_status"]
    loan_percent_income = request.data["loan_percent_income"]
    cb_person_default_on_file = request.data["cb_person_default_on_file"]
    cb_credit_history_len = request.data["cb_credit_history_len"]

    inp = []

    inp.append(int(age))
    inp.append(int(income))
    inp.append(float(employment_length))

    # 'A', 'B','C', 'D', 'E', 'F', 'G'], [9.79,20.9,32.9,43.6,51.4,59.7,63.3]

    if loan_grade == "A":
        inp.append(9.79)
    elif loan_grade == "B":
        inp.append(20.9)
    elif loan_grade == "C":
        inp.append(32.9)
    elif loan_grade == "D":
        inp.append(43.6)
    elif loan_grade == "E":
        inp.append(51.4)
    elif loan_grade == "F":
        inp.append(59.7)
    else:
        inp.append(63.3)

    inp.append(int(loan_amount))
    inp.append(float(loan_intrest))
    loan_cent_income = float(int(loan_amount)/int(income))
    inp.append(loan_cent_income)

    if cb_person_default_on_file == "N":
        inp.append(0)
    else:
        inp.append(1)
    
    inp.append(int(cb_credit_history_len))

    result = classifiers.classifier(inp)

    print(result)
    
    # try:
    # print("req:")
    # print(request.POST)/
    obj = Banking.objects.create(age=age, income=income, employment_length=employment_length, loan_amount=loan_amount, loan_intent=loan_intent, loan_grade=loan_grade, loan_intrest=loan_intrest, loan_status=loan_status, loan_percent_income=loan_percent_income, cb_person_default_on_file=cb_person_default_on_file, cb_credit_history_len=cb_credit_history_len)
    # print(obj)
    return Response({"results" : result}, status=status.HTTP_200_OK)
        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)