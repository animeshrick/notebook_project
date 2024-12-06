from django.urls import path
from .views import NoteListCreateAPIView

urlpatterns = [
    # Consolidated all operations into this endpoint
    path('notes/', NoteListCreateAPIView.as_view(), name='note-list-create'),
]
