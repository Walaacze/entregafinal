from django.views.generic import ListView, DetailView
from pages.models import Blog

class ListaBlogs(ListView):
    model = Blog
    template_name = 'pages/lista_blogs.html'
    
class DetalleBlogs(DetailView):
    model = Blog
    template_name = 'pages/detalle_blogs.html'
    
class CrearBlog(ListView):
    model = Blog
    success_url = '/pages/'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']
    
class BorrarBlog(ListView):
    model = Blog
    success_url = '/pages/'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']
class ActualizarBlog(ListView):
    model = Blog
    success_url = '/pages/'
