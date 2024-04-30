from django.contrib import admin
from django.db.models import Avg
from .models import Job
from decimal import Decimal
from django.db.models import Q
import numpy as np


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'company', 'location', 'salary', 'average_salary_for_python']
    search_fields = ['title', 'company', 'location']

    def average_salary_for_python(self, obj):
        
        if obj.location in ['Bangalore', 'Bengaluru']:
            # Convert Decimal128 salary to Decimal
            salaries = Job.objects.filter(Q(location__icontains='bangalore') | Q(location__icontains='bengaluru'))
            if salaries:
                salary_values = [salary.salary for salary in salaries]
                val = [float(Decimal(str(sal))) for sal in salary_values]
                average_salary = np.mean(val)
                return average_salary

        return '-'

    average_salary_for_python.short_description = 'Avg. Salary'
