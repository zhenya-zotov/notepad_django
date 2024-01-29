from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Note

# Create your views here.
def index(request):
    latest_note_list = Note.objects.all()
    context = {
        "latest_note_list": latest_note_list,
    }
    return render(request, "notes/index.html", context)

def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, "notes/detail.html", {"note": note})
