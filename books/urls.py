from django.urls import re_path
from books.views import ImportBooks

app_name = "import"

urlpatterns = [
    re_path('import/', ImportBooks.as_view(), name='import')
]
