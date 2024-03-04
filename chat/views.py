from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def room(request, room_name):
    return render(request, 'room.html')