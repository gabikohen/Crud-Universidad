from django.shortcuts import render,redirect
from .models import Curso
from django.contrib import messages
# Create your views here.

""" Todos los cursos """

def home(request):
    cursosListados = Curso.objects.all()
    messages.success(request, '¡Cursos listados!')
    return render(request,"gestionCursos.html",{"cursos":cursosListados})


""" Metodo para crear un curso """

def registrarCurso(request):
 codigo = request.POST['txtCodigo']
 name = request.POST['txtNombre']
 creditos = request.POST['numCreditos']

 curso = Curso.objects.create(codigo=codigo,name=name,creditos=creditos)
 messages.success(request, '¡Curso registrado!')
 return redirect('/')


""" Metodo para editar curso  """
def editarCurso(request,codigo):
 curso = Curso.objects.get(codigo=codigo)
 return render(request,"editarCurso.html",{"curso":curso})

def editCurso(request):
 codigo = request.POST['txtCodigo']
 name = request.POST['txtNombre']
 creditos = request.POST['numCreditos']

 curso = Curso.objects.get(codigo=codigo)
 curso.name = name
 curso.creditos = creditos
 curso.save()
 messages.success(request, '¡Curso actualizado!')
 return redirect('/')


""" Metodo Para eliminar un curso  """

def deleteCurso(request,codigo):
 curso = Curso.objects.get(codigo=codigo)
 curso.delete()
 messages.success(request, '¡Curso eliminado!')
 return redirect('/')
