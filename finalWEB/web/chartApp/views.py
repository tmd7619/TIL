from django.shortcuts import render

# Create your views here.

def intro(request):
    return render(request , 'chartIndex.html')

def line(request):
    seoul = [13.0, 6.9,9.5,14.5,18.4,21.5,25.2,26.5,23.3,18.3,13.9,9.6]
    london = [7,4,5,8,11,15,17,16,14,10,6,4]
    context = {'seoul': seoul, 'london' : london}
    return  render(request, 'line.html', context)


listv=["A", "b", "c", "D", "e", "F", "G", "h"];
result=[x for x in listv if x.islower() ];
print(result);