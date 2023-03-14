from django.shortcuts import render

# Create your views here.
def connections(request):
    d={'a':400,'b':250,'c':100}
    return render(request,'connections.html',d)
def loop(request):
    d={'name':'NARE'}
    return render(request,'loop.html',d)