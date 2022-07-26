from django.urls import path
from employers import views



urlpatterns=[
    path('home/',views.EmpHomeView.as_view(),name='emp-home'),
    path('profile/',views.EmployerProfileCreateView.as_view(),name='emp-profile-add'),
    path('profile/details/',views.EmployerProfileDetails.as_view(),name='empprofiledetails'),
    path('jobs/post/',views.JobCreateView.as_view(),name='emp-postjob'),
    path('jobs/',views.EmployerJobsListView.as_view(),name='emp-listjobs'),
    path('jobs/details/<int:id>',views.JobDetailView.as_view(),name='emp-jobdetails'),
    path('jobs/update/<int:id>',views.JobUpdateView.as_view(),name='emp-jobupdate'),
    path('jobs/applicants/<int:id>',views.JobApplicationsView.as_view(),name='emp-jobapplications'),
    path('applicant/profile/<int:id>',views.ApplicantProfileDetailView.as_view(),name='emp-appli-profile-detail'),
    path('application/rejected/<int:id>',views.empapplicationstatus,name='application-rejected'),
    path('application/accepted/<int:id>',views.empapplicationacceptedstatus,name='application-accepted'),
]