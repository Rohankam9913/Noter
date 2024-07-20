from django.shortcuts import render, redirect
from .forms import CreateForm
from .models import Note
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/")
def home(request):
    try:
        notes = Note.objects.filter(user=request.user).order_by("-createdAt")
        
        for note in notes:
            note.content = note.content[0:100]

        return render(request, 'home.html', {'notes': notes, 'user': request.user})
    except:
        return render(request, '404.html')

@login_required(login_url="/")
def create(request):
    try:
        if request.method == "POST":
            form = CreateForm(request.POST)
            if form.is_valid():
            
                note = form.save(commit=False)
                note.user = request.user
                note.save()
                return redirect('home')
        else:
            form = CreateForm()

        return render(request, 'create.html', {'form': form})
    except:
        return render(request, '404.html')

@login_required
def showParticularNote(request,id):
    try:
        note = Note.objects.filter(user=request.user).get(id=id)
        
        if note is not None:
            return render(request, 'particularNote.html', {'note': note})
    except:
        return render(request, '404.html')

@login_required
def edit(request, id):
    try:
        note = Note.objects.get(id=id)

        if request.method == "POST":
            form = CreateForm(request.POST, instance=note)
            if form.is_valid():
                note = form.save(commit=False)
                note.user = request.user
                note.save()
                return redirect('/notes')
        else:
            form = CreateForm(instance=note)

        return render(request, 'edit.html', {'form': form})
    except:
        return render(request, '404.html')

@login_required
def delete_note(request, id):
    try:
        note = Note.objects.filter(id=id).delete()
        return redirect("home")
    except:
        return render(request, '404.html')

    

    