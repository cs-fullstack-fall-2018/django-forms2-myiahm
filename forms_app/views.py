from django.shortcuts import render
from forms_app import forms



from .models import FormModel
from django.shortcuts import render, get_object_or_404, redirect
from .forms import Form

def index(request):
    form_list = FormModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'forms_app/index.html', context)

def form_name_view(request):
    form = Form()
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            # Do something
            print("VALIDATION SUCCESSFUL")
            post = form.save(commit=False)
            post.save()
            return redirect('index')


    return render(request, 'forms_app/index.html', {'form': form})

