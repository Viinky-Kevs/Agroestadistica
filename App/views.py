from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import CustomUser, FilesForm
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

def upload(request):
    context = {}
    
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            return redirect('listfiles')
    else:
        form = FilesForm()
    '''
        fs = FileSystemStorage()
        fs.save(upload_file.name, upload_file)
        name = upload_file.name
        size = upload_file.size
        context['name'] = name
        context['size'] = size
    '''
    form = FilesForm()
    context['form'] = form
    return render(request, 'AppWeb/upload.html', context)

def list_files(request):
    context = {}
    xlsx = Files_up.objects.all()
    #context['files'] = files
    return render(request, 'AppWeb/list_files.html', {'xlsx':xlsx})

def tstudent(request):
    return render(request, 'AppWeb/tstudent.html')