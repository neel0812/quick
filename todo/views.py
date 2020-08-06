from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo


def home_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            form = TodoForm()
            todos = Todo.objects.filter(user=request.user)
            return render(
                request,
                "todo/home.html",
                {"form": form, "todos": todos},
            )
        else:
            return redirect("/login/")

    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        return redirect("/")
