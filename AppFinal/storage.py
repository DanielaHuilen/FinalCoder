from django.core.files.storage import FileSystemStorage

class MiAlmacenamiento(FileSystemStorage):
   def __init__(self, location=None, base_url=None):
       super().__init__(location='archivos', base_url=base_url)
