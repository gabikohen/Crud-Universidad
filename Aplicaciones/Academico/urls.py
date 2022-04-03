
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('registrarCurso/',views.registrarCurso),
    path('editarCurso/<codigo>',views.editarCurso),
    path('editCurso/',views.editCurso),
    path('deleteCurso/<codigo>',views.deleteCurso)
    
 
]
