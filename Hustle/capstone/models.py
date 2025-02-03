from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('mentor', 'Mentor'),
        ('participant', 'Participant'),
    )
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    terms_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
class MenteeActivity(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentee_activities')
    activity = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity} - {self.timestamp}"

class Question(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question from {self.mentor.email} - {self.timestamp}"

class Message(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message to {self.mentor.email} - {self.timestamp}"


    
class ParticipantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='participant_profile')
    bio = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True, help_text="List your skills separated by commas.")
    interests = models.TextField(blank=True, null=True, help_text="List your interests separated by commas.")
    mentor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='mentees')
    certifications = models.FileField(upload_to='certifications/', blank=True, null=True)
    

    def __str__(self):
        return f"Participant Profile - {self.user.full_name}"

class MentorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mentor_profile')
    mentees = models.ManyToManyField(ParticipantProfile, related_name='mentors', blank=True)
    bio = models.TextField(blank=True, null=True)
    expertise_areas = models.TextField(blank=True, null=True, help_text="List your expertise areas separated by commas.")
    feedback = models.TextField(blank=True, null=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f"Mentor Profile - {self.user.full_name}"
    
class Feedback(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_feedbacks')
    rating = models.FloatField(default=0.0)
    feedback = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.mentor.full_name} from {self.mentee.full_name}"
    
class Progress(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Progress for {self.participant.full_name} - {self.task}"
    
class Resource(models.Model):
    FORMAT_CHOICES = [
        ('article', 'Article'),
        ('video', 'Video'),
        ('ebook', 'E-Book'),
    ]
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    topic = models.CharField(max_length=100)
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Rating(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = models.FloatField()
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating for {self.resource.title} by {self.user.full_name}"
    
class MentorshipRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
    ]

    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentorship_requests')
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mentorship Request from {self.mentee.full_name} to {self.mentor.full_name}"

class Session(models.Model):
    mentorship_request = models.ForeignKey(MentorshipRequest, on_delete=models.CASCADE, related_name='sessions')
    scheduled_time = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session on {self.scheduled_time}"

class ChatMessage(models.Model):
    mentorship_request = models.ForeignKey(MentorshipRequest, on_delete=models.CASCADE, related_name='chat_messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.full_name} at {self.timestamp}"
    
class JobListing(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full-Time'),
        ('part_time', 'Part-Time'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_listings')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SavedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_jobs')
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='saved_by')
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.full_name} saved {self.job_listing.title}"

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.full_name} applied for {self.job_listing.title}"