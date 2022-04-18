from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.ListaBlogs.as_view(), name='lista_blogs'),
    # path('detalle/', views.DetalleBlogs.as_view(), name='detalle_blog'),
    # path('crear/', views.CrearBlog.as_view(), name='crear_blog'),
    # path('borrar/', views.BorrarBlog.as_view(), name='borrar_blog'),
    # path('actualizar/', views.ActualizarBlog.as_view(), name='actualizar_blog'),


]
