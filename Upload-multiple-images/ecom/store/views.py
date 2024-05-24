from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from .models import UploadedFile
from .forms import UploadFileForm

def product(request):
    files = UploadedFile.objects.all()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for uploaded_file in request.FILES.getlist('files'):
                UploadedFile.objects.create(file=uploaded_file)
            return redirect('product')
    else:
        form = UploadFileForm()

    return render(request, 'upload_and_display.html', {'form': form, 'files': files})