from django import forms
from .models import User, ParticipantProfile, MentorProfile,Certificate, MentorAvailability, ScheduledSession, Quiz,  Chapter, Feedback, Resource, Rating, ChatMessage,  MentorshipRequest, Session, JobListing, JobApplication, Thread
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import inlineformset_factory

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'description', 'tags']  # Include fields you want in the form
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter thread title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter thread description'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tags (optional)'}),
        }
        labels = {
            'title': 'Thread Title',
            'description': 'Description',
            'tags': 'Tags (comma-separated)',
        }
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
        fields = ['mentor','notes', 'scheduled_time']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['mentor'].queryset = User.objects.filter(user_type='mentor')

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

class MentorshipResponseForm(forms.ModelForm):
    class Meta:
        model = MentorshipRequest
        fields = ['status', 'mentor_response']

class ChangeEmailForm(forms.Form):
    new_email = forms.EmailField(label="New Email", required=True)
    confirm_email = forms.EmailField(label="Confirm New Email", required=True)

    def clean(self):
        cleaned_data = super().clean()
        new_email = cleaned_data.get('new_email')
        confirm_email = cleaned_data.get('confirm_email')

        if new_email and confirm_email and new_email != confirm_email:
            raise forms.ValidationError("Emails do not match.")
        return cleaned_data
    
class DeleteAccountForm(forms.Form):
    confirm_delete = forms.BooleanField(
        label="I understand that this action cannot be undone.",
        required=True,
    )

class JobUploadForm(forms.ModelForm):
    """Form for mentors to upload job listings."""
    class Meta:
        model = JobListing
        fields = ['title', 'description', 'location', 'industry', 'job_type']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter job title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter job description', 'rows': 4}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter job location'}),
            'industry': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter industry'}),
            'job_type': forms.Select(attrs={'class': 'form-select'}),
        }

class MentorRatingForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=[(str(i), str(i)) for i in range(1, 6)], 
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Rating (1-5)"
    )
    feedback = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        label="Feedback"
    )

    class Meta:
        model = Feedback
        fields = ['rating', 'feedback']

class JobSubmitForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['resume', 'cover_letter']

    resume = forms.FileField(
        required=True,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': '.pdf'}),
        label="Upload Resume (PDF)"
    )

    cover_letter = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        required=True
    )

    
    cover_letter = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your cover letter...'}),
        label="Cover Letter"
    )


class ResourceUploadForm(forms.ModelForm):
    resource_file = forms.FileField(
        required=False,  # Optional file upload
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        label="Upload Resource File (PDF, DOCX)"
    )

    class Meta:
        model = Resource
        fields = ['title', 'description', 'cover_image', 'resource_file']  # Added `resource_file`
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cover_image'].widget.attrs.update({'class': 'form-control'})


class ChapterForm(forms.ModelForm):
    """
    Form for uploading individual chapters of a course.
    """
    class Meta:
        model = Chapter
        fields = ['title', 'content']


# ✅ Formset for ensuring at least 10 chapters are uploaded
ChapterFormSet = inlineformset_factory(Resource, Chapter, form=ChapterForm, extra=10, min_num=10, validate_min=True)

class ChapterQuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['resource', 'chapter', 'questions']

    def __init__(self, *args, **kwargs):
        super(ChapterQuizForm, self).__init__(*args, **kwargs)
        self.fields['resource'].queryset = Resource.objects.all()
        self.fields['chapter'].queryset = Chapter.objects.all()

    questions = forms.JSONField(widget=forms.Textarea(attrs={'rows': 5}))

class FinalQuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['resource', 'questions']

    def __init__(self, *args, **kwargs):
        super(FinalQuizForm, self).__init__(*args, **kwargs)
        self.fields['resource'].queryset = Resource.objects.all()

    questions = forms.JSONField(widget=forms.Textarea(attrs={'rows': 5}))

class MentorAvailabilityForm(forms.ModelForm):
    class Meta:
        model = MentorAvailability
        fields = ['date', 'start_time', 'end_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

class ScheduleSessionForm(forms.ModelForm):
    class Meta:
        model = ScheduledSession
        fields = ['notes']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter additional details...'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("End time must be later than start time.")

        return cleaned_data

class ScheduledSessionForm(forms.ModelForm):
    class Meta:
        model = ScheduledSession
        fields = ['date', 'start_time', 'end_time']


class FileUploadForm(forms.Form):
    file = forms.FileField(
        label="Upload a document",
        help_text="Supported formats: PDF, DOCX",
        widget=forms.ClearableFileInput(attrs={"class": "form-control"}),
    )