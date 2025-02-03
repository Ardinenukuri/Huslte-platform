from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('terms/mentor/', views.mentor_terms, name='mentor_terms'),
    path('terms/participant/', views.participant_terms, name='participant_terms'),
    path('participant/dashboard/', views.participant_dashboard, name='participant_dashboard'),
    path('mentor/dashboard/', views.mentor_dashboard, name='mentor_dashboard'),
    path('participant/profile/', views.participant_profile, name='participant_profile'),
    path('mentor/profile/', views.mentor_profile, name='mentor_profile'),
    path('submit-feedback/<int:mentor_id>/', views.submit_feedback, name='submit_feedback'),
    path('learning-resources/', views.learning_resources, name='learning_resources'),
    path('upload-resource/', views.upload_resource, name='upload_resource'),
    path('rate-resource/<int:resource_id>/', views.rate_resource, name='rate_resource'),
    path('submit-mentorship-request/', views.submit_mentorship_request, name='submit_mentorship_request'),
    path('schedule-session/<int:request_id>/', views.schedule_session, name='schedule_session'),
    path('chat-with-mentor/<int:request_id>/', views.chat_with_mentor, name='chat_with_mentor'),
    path('manage-mentorship-requests/', views.manage_mentorship_requests, name='manage_mentorship_requests'),
    path('approve-mentorship-request/<int:request_id>/', views.approve_mentorship_request, name='approve_mentorship_request'),
    path('decline-mentorship-request/<int:request_id>/', views.decline_mentorship_request, name='decline_mentorship_request'),
    path('chat-with-mentee/<int:request_id>/', views.chat_with_mentee, name='chat_with_mentee'),
    path('manage-schedule/', views.manage_schedule, name='manage_schedule'),
    path('job-listings/', views.job_listings, name='job_listings'),
    path('save-job/<int:job_id>/', views.save_job, name='save_job'),
    path('apply-for-job/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('job-application-tracker/', views.job_application_tracker, name='job_application_tracker'),
    path('employer-dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('manage-applicants/<int:job_id>/', views.manage_applicants, name='manage_applicants'),
    path('update-application-status/<int:application_id>/<str:status>/', views.update_application_status, name='update_application_status'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)