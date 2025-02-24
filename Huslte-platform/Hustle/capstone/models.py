from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Avg

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
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress_records')
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Progress for {self.participant.full_name} - {self.task}"
 
class Resource(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name="uploaded_courses")
    created_at = models.DateTimeField(auto_now_add=True)
    final_quiz = models.OneToOneField('Quiz', on_delete=models.SET_NULL, null=True, blank=True, related_name="final_quiz")
    cover_image = models.ImageField(upload_to='resumes/', null=True, blank=True)

    def average_rating(self):
        avg_rating = self.ratings.aggregate(avg=models.Avg('rating'))['avg']
        return round(avg_rating, 1) if avg_rating else 0 

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
    mentor_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mentorship Request from {self.mentee.full_name} to {self.mentor.full_name}"

class Session(models.Model):
    mentorship_request = models.ForeignKey(
        MentorshipRequest, on_delete=models.CASCADE, related_name='sessions'
    )
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scheduled_sessions')
    scheduled_time = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    is_confirmed = models.BooleanField(default=False)  # ✅ Add field for confirmation
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
    accepted_by_mentor_email = models.EmailField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=False, null=False)  # ✅ Resume file upload
    cover_letter = models.TextField()

    def __str__(self):
        return f"{self.user.full_name} applied for {self.job_listing.title}"
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    is_seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Notification for {self.user.username}"
    
class ChatMessage(models.Model):
    mentorship_request = models.ForeignKey(MentorshipRequest, on_delete=models.CASCADE, related_name='chat_messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    message = models.TextField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.full_name} at {self.timestamp}"


class Thread(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='threads')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField(default=0)  # <-- Ensure this field is present
    downvotes = models.IntegerField(default=0)
    tags = models.CharField(max_length=100, blank=True)  # Optional: For categorizing threads

    def __str__(self):
        return self.title


class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    

    def __str__(self):
        return f"Comment by {self.user.username} on {self.thread.title}"

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='votes')
    vote_type = models.CharField(max_length=10, choices=[('upvote', 'Upvote'), ('downvote', 'Downvote')])

    class Meta:
        unique_together = ('user', 'comment')  # Prevent duplicate votes by the same user on the same comment

    def __str__(self):
        return f"{self.vote_type} by {self.user.username} on {self.comment.text[:50]}"

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    certificate_file = models.FileField(upload_to='certificates/', null=True, blank=True)
    issued_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Certificate: {self.user.username} - {self.resource.title}"
    
class Chapter(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="chapters")
    title = models.CharField(max_length=255)
    content = models.TextField()
    chapter_number = models.PositiveIntegerField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.resource.title} - Chapter {self.chapter_number}: {self.title}"
    
class Quiz(models.Model):
    chapter = models.OneToOneField(Chapter, on_delete=models.CASCADE, related_name="quiz", null=True, blank=True)
    title = models.CharField(max_length=255)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="quizzes", null=True, blank=True)
    questions = models.JSONField(default=list)  # Store questions as JSON (Multiple Choice)
    is_final_quiz = models.BooleanField(default=False)

    def __str__(self):
        if self.is_final_quiz:
            return f"Final Quiz - {self.resource.title}"
        return f"Quiz for {self.chapter.title}"

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_progress')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="progress")
    completed_chapters = models.ManyToManyField(Chapter, blank=True)
    completed_quizzes = models.ManyToManyField(Quiz, blank=True)
    final_score = models.FloatField(null=True, blank=True)
    quiz_attempts = models.JSONField(default=dict)
    certificate = models.OneToOneField(Certificate, on_delete=models.SET_NULL, null=True, blank=True)


    def progress_percentage(self):
        total_chapters = self.resource.chapters.count()
        completed_chapters = self.completed_chapters.count()
        total_quizzes = Quiz.objects.filter(chapter__resource=self.resource).count() + 1  # +1 for final quiz
        completed_quizzes = self.completed_quizzes.count()

        chapter_progress = (completed_chapters / total_chapters * 50) if total_chapters > 0 else 0
        quiz_progress = (completed_quizzes / total_quizzes * 50) if total_quizzes > 0 else 0
    
        return chapter_progress + quiz_progress


    def __str__(self):
        return f"{self.user.username} - {self.resource.title} Progress"


class MentorAvailability(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="availability")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.mentor.full_name} available on {self.date} from {self.start_time} to {self.end_time}"

class ScheduledSession(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mentor_scheduled_sessions")
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="participant_scheduled_sessions", null=True, blank=True)  # ✅ Add this field
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    notes = models.TextField(blank=True, null=True)  
    is_confirmed = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mentor.full_name} - {self.date} ({self.start_time} to {self.end_time})"


class Question(models.Model):
    QUESTION_TYPES = [
        ('MCQ', 'Multiple Choice'),
        ('SHORT_ANSWER', 'Short Answer'),
        ('DOCUMENT_UPLOAD', 'Document Upload')
    ]
    
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_questions')
    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    options = models.JSONField(blank=True, null=True)  # Store MCQ options
    correct_answer = models.TextField(blank=True, null=True)  # For MCQ and Short Answer
    
    def __str__(self):
        return self.question_text

class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quiz_attempts")
    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE, related_name="attempts")
    answers = models.JSONField(default=dict)  # Store user's answers
    score = models.FloatField()
    attempt_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} ({self.score}%)"


class Enrollment(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
