from django.shortcuts import render, redirect
from .forms import JobRegister
from .models import Job
import numpy as np
from decimal import Decimal
from django.db.models import Q
from django.urls import reverse


# Create your views here.
def add_show(request):

    fm = JobRegister()
    jobs = Job.objects.all()

    # Calculate average salary using NumPy
    salaries = Job.objects.filter(Q(location__icontains='bangalore') | Q(location__icontains='bengaluru'))  
    if salaries:
        salary_values = [salary.salary for salary in salaries]
        val = [float(Decimal(str(sal))) for sal in salary_values]
        average_salary = np.mean(val)
    
    else:
        average_salary = None

    return render(request, 'enroll/addandshow.html', {'form': fm, 'job':jobs, 'average_salary': average_salary})


def del_data(request, id):
    if request.method == "POST":
        pi = Job.objects.get(pk = id)
        pi.delete()
        return redirect(add_show)

def update_data(request, id):
    if request.method == 'POST':
        pi = Job.objects.get(pk = id)
        fm = JobRegister(request.POST, instance = pi)
        if fm.is_valid():
            fm.save()
        return redirect(add_show)
    else:
        pi = Job.objects.get(pk = id )
        fm = JobRegister(instance = pi)
    return render(request, 'enroll/updatejobs.html', {'form':fm})


def job_list(request):
    query = request.GET.get('q')
    if query:
        jobs = Job.objects.filter(Q(title__icontains=query) | Q(company__icontains=query) | \
        Q(location__icontains=query))
    else:
        jobs = Job.objects.all()
    context = {'job': jobs}
    return render(request, 'enroll/addandshow.html', context)

# Calculate average salary using NumPy
def average_salary(request):
    salaries = Salary.objects.filter(location='Bangalore')
    if salaries:
        salary_values = [salary.salary for salary in salaries]
        average_salary = np.mean(salary_values)
    else:
        average_salary = None
    
    return render(request, 'enroll/addandshow.html', {'form':fm, 'average_salary': average_salary})


def admin_redirect(request):
    return redirect(reverse('admin:index'))