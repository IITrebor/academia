from django.urls import path
from .views import (
    RegistroUsuarioView,CustomLoginView,ListaCursosViews,DetalleCursoView,CrearCursoView,
    MisCursosView,InscribirseCursoView,CustomLogoutView
)

urlpatterns=[
   path('',ListaCursosViews.as_view(),name='lista_cursos'),
    path('registro/',RegistroUsuarioView.as_view(),name='registro'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',CustomLogoutView.as_view(),name='logout'),
    path('curso/<int:pk>/', DetalleCursoView.as_view(), name='detalle_curso'),
    path('curso/<int:pk>/inscribir/', InscribirseCursoView.as_view, name='inscribir_curso'),
    path('curso/crear/', CrearCursoView.as_view(), name='crear_curso'),
    path('mis-cursos/', MisCursosView.as_view(), name='mis_cursos'),



]