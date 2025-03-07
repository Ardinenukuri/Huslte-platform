from django.contrib import admin
from .models import (
    User, MenteeActivity, Question, Message, ParticipantProfile, MentorProfile,
    Feedback, Progress, Resource, Rating, MentorshipRequest, Session, ChatMessage,
    JobListing, SavedJob, JobApplication, Notification, Thread, Comment, Vote,
    Certificate, Chapter, Quiz, UserProgress, MentorAvailability, ScheduledSession,
    QuizAttempt, Enrollment
)


# ✅ Custom Admin for User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "user_type", "language_preference", "phone_number", "is_active")
    search_fields = ("full_name", "email", "user_type")
    list_filter = ("user_type", "language_preference", "is_active")


# ✅ MenteeActivity
@admin.register(MenteeActivity)
class MenteeActivityAdmin(admin.ModelAdmin):
    list_display = ("mentor", "activity", "timestamp")
    list_filter = ("mentor", "timestamp")



# ✅ Message
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("mentor", "message", "timestamp")
    search_fields = ("mentor__email", "message")


# ✅ ParticipantProfile
@admin.register(ParticipantProfile)
class ParticipantProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "mentor")
    search_fields = ("user__full_name", "mentor__full_name")


# ✅ MentorProfile
@admin.register(MentorProfile)
class MentorProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "rating")
    search_fields = ("user__full_name",)
    list_filter = ("rating",)


# ✅ Feedback
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("mentor", "mentee", "rating", "timestamp")
    list_filter = ("rating", "timestamp")
    search_fields = ("mentor__full_name", "mentee__full_name")


# ✅ Progress
@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ("participant", "task", "completed", "timestamp")
    list_filter = ("completed", "timestamp")


# ✅ Resource
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "created_at")
    search_fields = ("title", "created_by__full_name")
    list_filter = ("created_at",)


# ✅ Rating
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("resource", "user", "rating", "created_at")
    list_filter = ("rating", "created_at")


# ✅ MentorshipRequest
@admin.register(MentorshipRequest)
class MentorshipRequestAdmin(admin.ModelAdmin):
    list_display = ("mentee", "mentor", "status", "created_at")
    list_filter = ("status", "created_at")


# ✅ Session
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("mentorship_request", "mentor", "scheduled_time", "is_confirmed")
    list_filter = ("is_confirmed", "scheduled_time")


# ✅ ChatMessage
@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ("mentorship_request", "sender", "message", "timestamp")
    list_filter = ("timestamp",)


# ✅ JobListing
@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ("title", "employer", "location", "job_type", "created_at")
    search_fields = ("title", "employer__full_name")
    list_filter = ("job_type", "created_at")


# ✅ SavedJob
@admin.register(SavedJob)
class SavedJobAdmin(admin.ModelAdmin):
    list_display = ("user", "job_listing", "saved_at")
    search_fields = ("user__full_name", "job_listing__title")


# ✅ JobApplication
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("user", "job_listing", "status", "applied_at")
    list_filter = ("status", "applied_at")


# ✅ Notification
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "message", "is_read", "created_at")
    list_filter = ("is_read", "created_at")


# ✅ Thread
@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "created_at", "upvotes", "downvotes")
    search_fields = ("title", "created_by__full_name")
    list_filter = ("created_at",)


# ✅ Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("thread", "user", "text", "created_at", "upvotes", "downvotes")
    list_filter = ("created_at",)


# ✅ Vote
@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("user", "comment", "vote_type")


# ✅ Certificate
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("user", "resource", "issued_at")


# ✅ Chapter
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ("resource", "title", "chapter_number", "is_completed")


# ✅ Quiz
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "resource", "is_final_quiz")


# ✅ UserProgress
@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "resource")


# ✅ MentorAvailability
@admin.register(MentorAvailability)
class MentorAvailabilityAdmin(admin.ModelAdmin):
    list_display = ("mentor", "date", "start_time", "end_time", "is_booked")


# ✅ ScheduledSession
@admin.register(ScheduledSession)
class ScheduledSessionAdmin(admin.ModelAdmin):
    list_display = ("mentor", "participant", "date", "start_time", "end_time", "is_confirmed")


# ✅ QuizAttempt
@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "quiz", "score", "attempt_date")


# ✅ Enrollment
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("participant", "resource", "enrolled_at")

