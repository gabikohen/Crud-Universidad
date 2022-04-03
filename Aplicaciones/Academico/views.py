from django.shortcuts import render,redirect
from .models import Curso
# Create your views here.

def home(request):
    cursosListados = Curso.objects.all()
    return render(request,"gestionCursos.html",{"cursos":cursosListados})

def registrarCurso(request):
 codigo = request.POST['txtCodigo']
 name = request.POST['txtNombre']
 creditos = request.POST['numCreditos']

 curso = Curso.objects.create(codigo=codigo, name=name,creditos=creditos)
 return redirect('/')


def editCurso(request,codigo):
 codigo = request.POST['txtCodigo']
 name = request.POST['txtNombre']
 creditos = request.POST['numCreditos']

 curso = Curso.objects.get(codigo=codigo)
 curso.nombre = nombre
 curso.creditos = creditos
 curso.save()
 return redirect('/')


def editarCurso(request,codigo):
 curso = Curso.objects.get(codigo=codigo)
 return render(request,"editarCurso.html",{"curso":curso})

def deleteCurso(request,codigo):
 curso = Curso.objects.get(codigo=codigo)
 curso.delete()
 return redirect('/')
