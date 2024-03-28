from django.shortcuts import render
from notes.models import Note
from django.views.generic import ListView, DetailView

class NoteListView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/list.html'


class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/note.html'
