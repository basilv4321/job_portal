from django.shortcuts import render,redirect

from django.views.generic import TemplateView,CreateView,ListView,DetailView
from candidates.models import CandidateProfile
from candidates.forms import CandidateProfileForm
from django.urls import reverse_lazy
from employers.models import Jobs,Application
from candidates.filters import JobFilter

# Create your views here.

class CandidateHomeView(TemplateView):
    template_name = 'cand-home.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        qs=Jobs.objects.all()
        context['jobs']=qs
        return context

    def get(self,request,*args,**kwargs):
        filter=JobFilter(request.GET,queryset=Jobs.objects.all())
        return render(request,'cand-home.html',{'filter':filter})



class CandidateProfileCreateView(CreateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = 'cand-profileadd.html'
    success_url = reverse_lazy('cand-home')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class CandidateProfileView(TemplateView):
    template_name = 'cand-profileview.html'


# class CandidateJobsListView(ListView):
#     model = Jobs
#     template_name = 'cand-joblist.html'    #its not needed because the job list shown in the home page
#     context_object_name = 'jobs'


class CandidateJobDetailView(DetailView):
    model = Jobs
    context_object_name = 'jobdetail'
    template_name = 'cand-jobdetail.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        qs=Application.objects.filter(applicant=self.request.user,job=self.object)
        context['status']=qs
        return context


def applynow(request,*args,**kwargs):
    jobid=kwargs.get('id')
    job=Jobs.objects.get(id=jobid)
    applicant=request.user
    Application.objects.create(applicant=applicant,job=job)
    return redirect('cand-home')


class CandidateJobsAppliedListView(ListView):
    model = Application
    template_name = 'candidateappliedjobs.html'
    context_object_name = 'applied_jobs'

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user)


class AcceptedApplications(ListView):
    model = Application
    template_name = 'accepted.html'
    context_object_name = 'application'

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user,status='accepted')