from django import forms
from candidates.models import CandidateProfile


class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model=CandidateProfile
        exclude=('user',)