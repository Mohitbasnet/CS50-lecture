from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms

# Create your views here



def index(request):

    # Check if there already exists a "tasks" key in our session

    if "tasks" not in request.session:

        # If not, create a new list
        request.session["tasks"] = []

    return render(request, "task/index.html", {
        "tasks": request.session["tasks"]
    })


# Add a new task:
def add(request):

    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = NewTaskForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            task = form.cleaned_data["task"]

            # Add the new task to our list of tasks
            request.session["tasks"] += [task]

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("task:index"))

        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "task/add.html", {
                "form": form
            })
    return render(request,"task/add.html",{

        "form": NewTaskForm()
    })

    
    

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")
    
