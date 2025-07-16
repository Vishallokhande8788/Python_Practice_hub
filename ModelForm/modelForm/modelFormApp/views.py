from django.http import HttpResponseRedirect
from django.shortcuts import render
from modelFormApp.form import modelFormForm
from modelFormApp.models import modelForm 

# Create your views here.
def modelFormView(request):
    form = modelFormForm()
    print("get request")
    if request.method == 'POST':
        form = modelFormForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # add form data inside database
            return HttpResponseRedirect('/modelForm/')
    return render(request, 'modelForm.html', {'form': form})

def modelListView(request):
    modelList = modelForm.objects.all()
    return render(request, 'modelList.html', {'modelList': modelList})  