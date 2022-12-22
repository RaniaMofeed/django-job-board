from django.shortcuts import render
from.models import Job

# Create your views here.
def job_list(request):
    job_list=Job.objects.all()
    print (job_list)
    context ={'jobs':job_list}#template name
    return render(request,'job/job_list.html',context)

def job_detail(request , id):
    job_detail=Job.objects.get(id=id)
    context ={'job_d':job_detail}#template name
    return render(request,'job/job_detail.html',context)