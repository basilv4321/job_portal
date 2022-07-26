from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView
from employers.models import EmployerProfile,Jobs,Application
from employers.forms import EmployerProfileForm,JobForm
from candidates.models import CandidateProfile
from users.models import User
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

class EmpHomeView(TemplateView):
    template_name = 'emp-home.html'

class EmployerProfileCreateView(CreateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = 'emp-profile.html'
    success_url = reverse_lazy('emp-home')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


    # def post(self, request, *args, **kwargs):
    #     form=EmployerProfileForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         profile=form.save(commit=False)
    #         profile.user=request.user
    #         profile.save()
    #         return redirect('emp-home')
    #     else:
    #         return render(request,self.template_name,{'form':form})



class EmployerProfileDetails(TemplateView):
    template_name = 'emp-profile-detail.html'


class JobCreateView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = 'emp-postjob.html'
    success_url = reverse_lazy('emp-home')

    def form_valid(self, form):
        form.instance.posted_by=self.request.user
        messages.success(self.request,'Job has been Posted Successfully')
        return super().form_valid(form)


class EmployerJobsListView(ListView):
    model = Jobs
    context_object_name = 'jobs'
    template_name = 'emp-joblist.html'

    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user).order_by('-created_date')


class JobDetailView(DetailView):
    model = Jobs
    template_name = 'emp-jobdetailsaa.html'
    context_object_name = 'details'
    pk_url_kwarg = 'id'


class JobUpdateView(UpdateView):
    model = Jobs
    form_class = JobForm
    template_name = 'emp-postjob.html'
    success_url = reverse_lazy('emp-home')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,'Job Edited Successfully')
        return super().form_valid(form)


class JobApplicationsView(ListView):
    model = Application
    template_name = 'emp-jobapplicants.html'
    context_object_name = 'jobapplications'

    def get_queryset(self):
        return Application.objects.filter(job=self.kwargs.get('id'),status='applied')


class ApplicantProfileDetailView(DetailView):
    model = Application
    template_name = 'empcandidateprofile.html'
    context_object_name = 'canddetails'
    pk_url_kwarg = 'id'


def empapplicationstatus(request,*args,**kwargs):
    id=kwargs.get('id')
    qs=Application.objects.get(id=id)
    qs.status='rejected'
    qs.save()
    return redirect('emp-home')


def empapplicationacceptedstatus(request,*args,**kwargs):
    id=kwargs.get('id')
    qs=Application.objects.get(id=id)
    qs.status='accepted'
    qs.save()
    send_mail(
        'Job Notification',
        'Hi, your application accepted',
        'basilv4321@gmail.com',
        ['basilv54321@gmail.com'],
        fail_silently=False,
    )
    return redirect('emp-home')

