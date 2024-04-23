from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee
# Create your views here.

def employee_list(request):
    context = {'list':Employee.objects.all()}
    return render(request, 'registration/employee_list.html', context)

def employee_form(request, id=0):
    if request.method == 'GET':
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'registration/employee_form.html', {'form': form})
    else:
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            # Redirect to the employee list view (assuming it's named 'employee_list')
            return redirect('list')
        # Handle invalid form data (optional, e.g., return to form with errors)
        return render(request, 'registration/employee_form.html', {'form': form})

def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('list')

