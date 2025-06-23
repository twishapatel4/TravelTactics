from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def RegPage(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save user to the database
            messages.success(request, "Account created successfully!")
            return redirect('login')  # Redirect to login page after successful signup
        else:
            print(form.errors)
            messages.error(request, "Error in form submission!")  # Form validation failed

    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})
