from django.shortcuts import render
from .forms import CarForm
from datetime import datetime as dt, time as tm , date as dm

def checkLicensePlate(plate,date_time):
    """
    this function return True or false depending of the
    Peak Hours mobilization laws mentioned in the README.md

    plate:          (str) License plate with the format "XXX-0000" (number could be 3/4)
    date_time:      (str) Date and time selected to predict. format: "2021-02-06T16:43"

    return:         (int) 1 if the car can drive, 0 if not.
    """
    peak = {
        0 : [1,2],
        1 : [3,4],
        2 : [5,6],
        3 : [7,8],
        4 : [9,0],
    }

    message1 = "{}, License Plate {} can {} drive on {}."
    message3 = message1[:-1] + " at time: {}."
    message2 = "Plate can only be alphanumeric."
    if not plate.isalnum():
        return 0,message2

    lDigit      = plate[-1]   # Last Digit
    day,time_    = date_time.split("T")
    day = dt.strptime(day, '%Y-%m-%d')
    weekday     = day.weekday()
    weekdaystr  = day.strftime('%A')

    # if the selected date is not in the peak days then it can drive.
    if weekday not in peak.keys():
        return 1 , message1.format('YES',plate,'',weekdaystr)
    # if lDigit not in the blacklist of the day then it can drive.
    if int(lDigit) not in peak[weekday]:
        return 1 , message1.format('YES',plate,'',weekdaystr)

    time_        = dt.strptime(time_, '%H:%M').time()
    # if the time_ selected is between the peak hours then it can't drive.
    if (time_>= tm(7,0) and time_ <= tm(9,30)) or (time_>= tm(16,0) and time_ <= tm(19,30)):
        return 0 , message3.format('NO',plate,'not',weekdaystr,str(time_))
    else:
        # else, it can drive.
        return 1 , message3.format('YES',plate,'',weekdaystr,str(time_))


def index(request):
    """
    Rendering function for the License Plate Form.
    """
    if request.method=='POST':
        placa = request.POST['placa']
        date  = request.POST['DateTimeField']
        result , message  = checkLicensePlate(placa,date)
    else:
        result=0 ; message=None

    form = CarForm()
    context = {'form':form,
               'result':result,
               'message':message}
    return render(request,'car/LicensePlate.html',context)