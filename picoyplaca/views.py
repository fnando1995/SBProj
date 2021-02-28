from django.shortcuts import render
from .forms import CarForm

def index(request):
    """
    Rendering function for the License Plate Form.
    """
    if request.method=='POST':
        POST_DATA = request.POST
        placa = POST_DATA['placa']
        date  = POST_DATA['DateTimeField']
        result=0

    else:
        message=None
        result=0

    form = CarForm()
    context = {'message':message,'form':form,'result':result}
    return render(request,'car/LicensePlate.html',context)