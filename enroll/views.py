from django.shortcuts import render
from  .forms import StudentRegi

# Create your views here.
def ShowData(request):
    fm=StudentRegi()
    fm.order_fields(field_order=['name','email','first_name'])
    #return render(request, 'enroll/user_registration1.html', {'form': fm})
    #return render(request, 'enroll/form_field_argument.html', {'form': fm})
    return render(request, 'enroll/widget.html', {'form': fm})
    #return render(request,'enroll/user_registration.html', {'form': fm})


'''
{{form.as_p}}
{{form}}


'''