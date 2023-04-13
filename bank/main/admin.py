from django.contrib import admin
from .models import Banking

# Register your models here.
class BankingAdmin(admin.ModelAdmin):
    list = ('age','income','employment_length','loan_amount','loan_intent','loan_grade','loan_intrest','loan_status','loan_percent_income','cb_person_default_on_file','cb_credit_history_len')


admin.site.register(Banking, BankingAdmin)

