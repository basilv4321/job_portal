from django.urls import path
from candidates import views


urlpatterns=[
    path('home/',views.CandidateHomeView.as_view(),name='cand-home'),
    path('profile/add',views.CandidateProfileCreateView.as_view(),name='cand-profileadd'),
    path('profile/view/',views.CandidateProfileView.as_view(),name='cand-profileview'),
    path('jobs/detail/<int:id>',views.CandidateJobDetailView.as_view(),name='cand-jobdetail'),
    path('application/add/<int:id>',views.applynow,name='apply-now'),
    path('application/all/',views.CandidateJobsAppliedListView.as_view(),name='cand-appli-list'),
    path('notifications/',views.AcceptedApplications.as_view(),name='cand-notifications'),
]