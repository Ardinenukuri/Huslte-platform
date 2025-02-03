from django import forms
from .models import User, ParticipantProfile, MentorProfile, Feedback, Resource, Rating, ChatMessage,  MentorshipRequest, Session, JobListing, JobApplication

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES)

class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    terms_and_conditions = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'phone_number', 'user_type', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        username = cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("Username cannot be empty")
        return cleaned_data
        
class ParticipantProfileForm(forms.ModelForm):
    class Meta:
        model = ParticipantProfile
        fields = ['bio', 'skills', 'interests', 'certifications']

class MentorProfileForm(forms.ModelForm):
    class Meta:
        model = MentorProfile
        fields = ['bio', 'expertise_areas']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'feedback']

class ResourceSearchForm(forms.Form):
    keyword = forms.CharField(required=False)
    topic = forms.CharField(required=False)
    format = forms.ChoiceField(choices=Resource.FORMAT_CHOICES, required=False)
    difficulty = forms.ChoiceField(choices=Resource.DIFFICULTY_CHOICES, required=False)

class ResourceUploadForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'topic', 'format', 'difficulty', 'url']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'review']

class MentorshipRequestForm(forms.ModelForm):
    class Meta:
        model = MentorshipRequest
        fields = ['mentor', 'message']

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['scheduled_time', 'notes']

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['message']

class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['title', 'description', 'location', 'industry', 'job_type']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job_listing']