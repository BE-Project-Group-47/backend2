from rest_framework import serializers
from .models import Banking

class BankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banking
        fields = '__all__'
        # fields = ('id','age','income','employment_length','loan_amount','loan_intent','loan_grade','loan_intrest','loan_status','loan_percent_income','cb_person_default_on_file','cb_credit_history_len')