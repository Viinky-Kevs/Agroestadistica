from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.

def home(request):
	return render(request, 'AppWeb/index.html')

def register_user(request):
    data = { 'form': CustomUser()}
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
        upload_file = request.FILES['Archivo']
        fs = FileSystemStorage()
        fs.save(upload_file.name, upload_file)
        name = upload_file.name
        size = upload_file.size
        context['name'] = name
        context['size'] = size
    return render(request, 'AppWeb/upload.html', context)