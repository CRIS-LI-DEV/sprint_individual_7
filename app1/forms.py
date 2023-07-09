from django import forms
from app1.models import *
from django.contrib.auth.models import User
class LoginUsuario(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese su username','class':'form-control'}),max_length=50,required=True,label='Nombre de usuario')
    clave = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña','class':'form-control'}), max_length=20,label='Password',required=True,error_messages={'required':'La contraseña es obligatoria'})


class RegistroTareasForm(forms.Form):

    opciones_estado = Estado.objects.all().values_list('nombre', flat=True)
    opciones_categoria = Categoria.objects.all().values_list('nombre', flat=True)
    opciones_prioridad = Prioridad.objects.all().values_list('nombre', flat=True)
    opciones_usuario = User.objects.all().values_list('username', flat=True)


    OPCIONES_ESTADO = tuple((opcion, opcion) for opcion in opciones_estado)
    OPCIONES_CATEGORIA = tuple((opcion, opcion) for opcion in opciones_categoria)
    
    OPCIONES_PRIORIDAD = tuple((opcion, opcion) for opcion in opciones_prioridad)
    OPCIONES_USUARIO = tuple((opcion, opcion) for opcion in opciones_usuario)



    # OPCIONES_ESTADO = (("a","a"))
    # OPCIONES_CATEGORIA = (("a","a"))

    nombre = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'text'}))
    descripcion = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'text'}))
    vencimiento = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}))
    
    estado = forms.ChoiceField(
        choices=OPCIONES_ESTADO, 
        widget=forms.Select(attrs={'class': 'form-control'}))

    categoria = forms.ChoiceField(
        choices=OPCIONES_CATEGORIA,
        widget=forms.Select( attrs={'class': 'form-control'}))
    
    
    prioridad = forms.ChoiceField(
        choices=OPCIONES_PRIORIDAD,
        widget=forms.Select( attrs={'class': 'form-control'}))

    usuario = forms.ChoiceField(
        choices=OPCIONES_USUARIO,
        widget=forms.Select( attrs={'class': 'form-control'}))

class Filtro(forms.Form):
    opciones_estado = Estado.objects.all().values_list('nombre', flat=True)
    opciones_categoria = Categoria.objects.all().values_list('nombre', flat=True)
 
    OPCION_TODAS =[["TODAS","TODAS"]]
    OPCIONES_ESTADO = tuple([(opcion, opcion) for opcion in opciones_estado] + OPCION_TODAS)
    OPCIONES_CATEGORIA = tuple([(opcion, opcion) for opcion in opciones_categoria] + OPCION_TODAS)
   
    
  


    estado = forms.ChoiceField(
        choices=OPCIONES_ESTADO,
        widget=forms.Select(attrs={'class': 'form-control'}))

    categoria = forms.ChoiceField(
        choices=OPCIONES_CATEGORIA,
        widget=forms.Select( attrs={'class': 'form-control'}))




class ObservacionForm(forms.Form):
    observacion = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'text'}))






