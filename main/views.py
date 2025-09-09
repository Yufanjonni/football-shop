from django.shortcuts import render
def show_main(request):
    context = {
        'store_name' : 'Ryan Rapopo',
        'name' : 'Muhammad Yufan Jonni',
        'npm' : '2406408602',
        'class' : 'PBP A'
    }
    return render(request, "main.html", context)

# Create your views here.
