from django.views.generic import View
from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.hashers import check_password

from .models import *
from .forms import *

from my_functions import valid_acount # valida si un usuario esta loguiado y tiene cuenta, retorna true/false

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
# Create your views here.

class Register(View): # vistas del registro de usuario
    #registra un usuario
    def get(self, request):
        if valid_acount(request):
            return redirect(reverse_lazy("login"))
        form = UserCreationForm()
        return render(request, "login/register.html", {"form": form, "title": "Registrarse", "button_text": "Aceptar"})
    

    def post(self, request):
        
        if valid_acount(request):
            return redirect(reverse_lazy("login"))
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            user = authenticate(request=request, username=usuario.username, password=form.cleaned_data['password1'])
            if user is not None:
                # Establecer la sesión de usuario
                login(request, user)
                return redirect(reverse_lazy("acount"))
        
        content = {
            "form": UserCreationForm(request.POST),
            "title": "Registro",
            "button_text": "Aceptar"
            }

        return render(request, "login/register.html", content)

def user_logout(request):
    logout(request)
    return redirect(reverse_lazy("login"))

def register_acount(request): # registra una ceunta vinculada a un usuario de auth_user
    if request.user.is_authenticated: # si esta autenticado
        context={'imgAvatar': "/media/avatares/avatar.png",
                 "title": "Registro",
                "button_text": "Acptar"}
        try:
            user = request.user
            account = Acount.objects.get(user_id=user)
            return redirect(reverse_lazy('turns'))
        except:
            
        

            if request.method == "POST":
                form = AcountForm(request.POST)
                if form.is_valid():
                    new_acount = form.save(commit=False)
                    # Guardar la imagen en una carpeta
                    if 'imgAvatar' in request.FILES:
                        image = request.FILES['imgAvatar']
                        image_name = image.name
                        path = default_storage.save(f'avatares/{image_name}', ContentFile(image.read()))
                        new_acount.imgAvatar = path

                    new_acount.user = request.user  # Asigna el usuario actualmente autenticado

                    new_acount.save()  # Ahora guarda la instancia con el usuario asignado

                    # Actualiza el correo electrónico en la tabla auth_user con el valor de Acount
                    request.user.email = new_acount.email
                    request.user.save()

                    return redirect(reverse_lazy('turns'))  
                else:
                    form = AcountForm(request.POST)
            else:
                sessions = TypeSession.objects.all()
                session_choices = []
                for session in sessions:
                    session_choices.append((session, session.name))
                form = AcountForm() 
                form.fields['typeSession'].choices = session_choices

            context["form"] = form

            return render(request, "login/registerAccount.html", context)

    return redirect(reverse_lazy("register"))


def view_login(request): # la vista del login
    #autenticacion de usuario
    
    context = {"title": "Iniciar sesion", "button_text": "Login"}
    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']  
            password = form.cleaned_data['password']
            
            # Busca el usuario por correo electrónico
            try:
                user = User.objects.get(email=email)
            except:
                context["msj"] = "Usuario o contraseña inexistenses"
                context["form"] = form
                return render(request, "login/login.html", context)
            
            if user is not None and check_password(password, user.password):
                authenticated_user = authenticate(request, username=user.username, password=password)
                login(request, authenticated_user)
                return redirect(reverse_lazy('turns'))
            else:
                context = {"msj": "Usuario o contraseña incorrecta"}

    form = LoginForm()
    context["form"] = form
    return render(request, "login/login.html", context)



