from django.shortcuts import render, redirect
from notes.models import Note
from django.views.generic import ListView, DetailView
from notes.forms import NoteForm

class NoteListView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/list.html'
    ordering = '-date'


class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/note.html'


def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note-list')
    else:
        form = NoteForm()
        return render(request, 'notes/add_note.html', {'form': form})
