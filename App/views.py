from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .forms import CustomUser, FilesForm, SelectFile
from .formulas import T_student
from .models import Files_up

# Create your views here.

def home(request):
	return render(request, 'AppWeb/index.html')

def register_user(request):
    data = {'form': CustomUser()}
    if request.method == 'POST':
        formulario = CustomUser(data = request.POST)
        if formulario.is_valid():
            formulario.save()

            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "El usuario a sido creado satisfactoriamente")

            return redirect(to = "home")

        data["form"] = formulario    
    return render(request, 'registration/register.html',data)

@login_required(login_url = '/accounts/login/')
def upload(request):
    context = {}
    
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listfiles')
    else:
        form = FilesForm()
    form = FilesForm()
    context['form'] = form
    return render(request, 'AppWeb/upload.html', context)

@login_required(login_url = '/accounts/login/')
def list_files(request):
    context = {}
    xlsx = Files_up.objects.all()
    #context['files'] = files
    return render(request, 'AppWeb/list_files.html', {'xlsx':xlsx})

@login_required(login_url = '/accounts/login/')
def tstudent(request):
    context = {}
    #form = SelectFile()
    if request.method == "POST":
        file = SelectFile(request.POST)
        results = request.Get(request.POST)
        if file.is_valid():
            context['dir_file'] = file.Descarga_archivo.url
            
    else:
       file = SelectFile(request.POST) 
    
    context['form'] = file
    return render(request, 'AppWeb/tstudent.html', context)