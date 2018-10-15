from django.shortcuts import render
from forms_app import forms



from .models import FormModel


def index(request):
    form_list = FormModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'forms_app/index.html', context)

def form_name_view(request):
    form = forms.Formmodel()
    if request.method == 'POST':
        form = forms.Formmodel(request.POST)
        if form.is_valid():
            # Do something
            print("VALIDATION SUCCESSFUL")

    return render(request, 'forms_app/index.html', {'form': form})
