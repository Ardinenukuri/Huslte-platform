import datetime
from msvcrt import getch
from sre_parse import parse_template
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm, ParticipantProfileForm, JobSubmitForm, MentorProfileForm, MentorRatingForm, JobUploadForm, FeedbackForm, ResourceSearchForm, ResourceUploadForm, RatingForm, MentorshipRequestForm, SessionForm, ChatMessageForm, JobApplicationForm, MentorshipResponseForm, ThreadForm, ChangeEmailForm, PasswordChangeForm, DeleteAccountForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User, MenteeActivity, Question, Message, ParticipantProfile, MentorProfile, Feedback, Progress, Resource, MentorshipRequest, ChatMessage, Session, JobListing, SavedJob, JobApplication, Notification, Thread, Comment, Vote
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import Avg
from .google_calendar import get_google_calendar_service, create_calendar_event
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def homepage(request):
    return render(request, 'capstone/homepage.html')

def about_us(request):
    return render(request, 'capstone/about_us.html')

def features(request):
    return render(request, 'capstone/features.html')

def contact_us(request):
    return render(request, 'capstone/contact_us.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']
            
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None and user.user_type == user_type:
                login(request, user)
                if user.user_type == 'participant':
                    return redirect('participant_dashboard')
                elif user.user_type == 'mentor':
                    return redirect('mentor_dashboard')
            else:
                form.add_error(None, 'Invalid email, password, or user type')
    else:
        form = LoginForm()
    
    return render(request, 'capstone/login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.username = form.cleaned_data['username']
            user.save()

            
            send_mail(
                'Welcome to Hustle Platform!',
                f'Hi {user.full_name},\n\nWelcome to Hustle Platform! 🚀\n\nExplore mentorship, learning resources, and job opportunities.\n\nHappy Learning,\nThe Hustle Platform Team',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'capstone/signup.html', {'form': form})

def mentor_terms(request):
    return render(request, 'capstone/mentor_terms.html')

def participant_terms(request):
    return render(request, 'capstone/participant_terms.html')

@login_required
def participant_dashboard(request, participant_id=None):
    if participant_id:
        participant = get_object_or_404(User, id=participant_id, user_type='participant')
    else:
        participant = request.user  

    mentorship_request = MentorshipRequest.objects.filter(
        mentee=participant, status='approved'
    ).first()  

    mentor = mentorship_request.mentor if mentorship_request else None

    notifications = Notification.objects.filter(user=participant, is_seen=False).order_by('-created_at')

    context = {
        'user': participant,
        'mentor': mentor,  
        'notifications': notifications,
    }
    return render(request, 'capstone/participant_dashboard.html', context)


@login_required
def mentor_dashboard(request):
    if request.user.user_type != 'mentor' and not request.user.is_superuser:
        return redirect('login')   
    notifications = Notification.objects.filter(user=request.user, is_seen=False).order_by('-created_at')
    mentees = User.objects.filter(
        id__in=MentorshipRequest.objects.filter(mentor=request.user, status='approved').values_list('mentee_id', flat=True)
    )
    mentorship_requests = MentorshipRequest.objects.filter(mentor=request.user, status='pending')
    messages = Message.objects.filter(mentor=request.user).order_by('-timestamp')[:5]
    context = {
        'user': request.user,
        'notifications': notifications,
        'mentees': mentees,
        'messages': messages,
        'mentorship_requests': mentorship_requests,
    }

    return render(request, 'capstone/mentor_dashboard.html', context)

@login_required
def participant_profile(request, participant_id):
    participant = get_object_or_404(User, id=participant_id, user_type='participant')
    profile, created = ParticipantProfile.objects.get_or_create(user=participant)
    progress = Progress.objects.filter(participant=request.user)
    total_tasks = progress.count()
    completed_tasks = progress.filter(completed=True).count()
    progress_percentage = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
    
    if request.method == 'POST':
        form = ParticipantProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('participant_profile')
    else:
        form = ParticipantProfileForm(instance=profile)
    return render(request, 'capstone/participant_profile.html', {'form': form, 'progress_percentage': progress_percentage, 'participant': participant})

@login_required
def mentor_profile(request, mentor_id):
    mentor = get_object_or_404(User, id=mentor_id, user_type='mentor')
    profile, created = MentorProfile.objects.get_or_create(user=mentor)
    mentees = User.objects.filter(
        id__in=MentorshipRequest.objects.filter(mentor=mentor, status='approved').values_list('mentee_id', flat=True)
    )
    feedbacks = Feedback.objects.filter(mentor=mentor)

    if request.method == 'POST':
        form = MentorProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('mentor_profile', mentor_id=mentor.id)
    else:
        form = MentorProfileForm(instance=profile)

    return render(request, 'capstone/mentor_profile.html', {
        'profile': profile,
        'form': form,
        'mentor': mentor,
        'mentees': mentees,
        'feedbacks': feedbacks,
    })

@login_required
def submit_feedback(request, mentor_id):
    mentor = get_object_or_404(User, id=mentor_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.mentor = mentor
            feedback.mentee = request.user
            feedback.save()
            return redirect('participant_dashboard')
    else:
        form = FeedbackForm()
    return render(request, 'capstone/submit_feedback.html', {'form': form, 'mentor': mentor})

def learning_resources(request):
    base_template = "mentor-base.html" if request.user.is_authenticated and request.user.user_type == "mentor" else "participant-base.html"
    resources = Resource.objects.all().annotate(avg_rating=Avg('ratings__rating')).order_by('id')
    mentorship_requests = MentorshipRequest.objects.filter(mentee=request.user)
    form = ResourceSearchForm(request.GET)

    if form.is_valid():
        keyword = form.cleaned_data.get('keyword')
        topic = form.cleaned_data.get('topic')
        format = form.cleaned_data.get('format')
        difficulty = form.cleaned_data.get('difficulty')

        if keyword:
            resources = resources.filter(title__icontains=keyword)
        if topic:
            resources = resources.filter(topic__icontains=topic)
        if format:
            resources = resources.filter(format=format)
        if difficulty:
            resources = resources.filter(difficulty=difficulty)

    paginator = Paginator(resources, 5)  
    page_number = request.GET.get('page')
    if not page_number: 
        page_number = 1
    try:
        resources = paginator.page(page_number)
    except PageNotAnInteger:
        resources = paginator.page(1)
    except EmptyPage:
        resources = paginator.page(paginator.num_pages)

    resources = Resource.objects.all()

    context = {
        'resources': resources,
        'form': form,
        'mentorship_requests': mentorship_requests,
        "base_template": base_template,
    }
    return render(request, 'capstone/learning_resources.html', context)

def mlearning_resources(request):
    base_template = "mentor-base.html" if request.user.is_authenticated and request.user.user_type == "mentor" else "participant-base.html"
    resources = Resource.objects.all().annotate(avg_rating=Avg('ratings__rating')).order_by('id')
    mentorship_requests = MentorshipRequest.objects.filter(mentee=request.user)
    form = ResourceSearchForm(request.GET)

    if form.is_valid():
        keyword = form.cleaned_data.get('keyword')
        topic = form.cleaned_data.get('topic')
        format = form.cleaned_data.get('format')
        difficulty = form.cleaned_data.get('difficulty')

        if keyword:
            resources = resources.filter(title__icontains=keyword)
        if topic:
            resources = resources.filter(topic__icontains=topic)
        if format:
            resources = resources.filter(format=format)
        if difficulty:
            resources = resources.filter(difficulty=difficulty)
    
    
    paginator = Paginator(resources, 5)  
    page_number = request.GET.get('page')
    if not page_number: 
        page_number = 1
    try:
        resources = paginator.page(page_number)
    except PageNotAnInteger:
        resources = paginator.page(1)
    except EmptyPage:
        resources = paginator.page(paginator.num_pages)

    resources = Resource.objects.all()

    context = {
        'resources': resources,
        'form': form,
        'mentorship_requests': mentorship_requests,
        "base_template": base_template,
    }
    return render(request, 'capstone/mentor-learning_resources.html', context)


@login_required
@user_passes_test(lambda u: u.user_type == 'mentor' or u.is_superuser)
def upload_resource(request):
    if request.method == 'POST':
        form = ResourceUploadForm(request.POST)
        if form.is_valid():
            form.save()
            participants = User.objects.filter(user_type='participant')
            for participant in participants:
                Notification.objects.create(
                    user=participant,
                    message=f"A new resource has been uploaded"
                )
            return redirect('mentor_dashboard')
    else:
        form = ResourceUploadForm()
    return render(request, 'capstone/upload_resource.html', {'form': form})

@login_required
def rate_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.resource = resource
            rating.user = request.user
            rating.save()
            return redirect('learning_resources')
    else:
        form = RatingForm()
    return render(request, 'capstone/rate_resource.html', {'form': form, 'resource': resource})

@login_required
def submit_mentorship_request(request):
    mentors = User.objects.filter(user_type='mentor')  

    if request.method == 'POST':
        form = MentorshipRequestForm(request.POST)
        if form.is_valid():
            mentorship_request = form.save(commit=False)
            mentorship_request.mentee = request.user
            mentorship_request.save()
            return redirect('participant_dashboard')
    else:
        form = MentorshipRequestForm()

    return render(request, 'capstone/submit_mentorship_request.html', {
        'form': form,
        'mentors': mentors,  
    })

@login_required
def schedule_session(request, request_id):
    mentorship_request = get_object_or_404(MentorshipRequest, id=request_id, mentee=request.user)
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.mentorship_request = mentorship_request
            session.save()

            
            event_link = create_calendar_event(
                summary=f"Session with {mentorship_request.mentor.full_name}",
                description=session.notes,
                start_time=session.scheduled_time.isoformat(),
                end_time=(session.scheduled_time + datetime.timedelta(hours=1)).isoformat(),
                timezone='UTC',
                attendees=[{'email': mentorship_request.mentor.email}]
            )

            
            Notification.objects.create(
                user=mentorship_request.mentor,
                message=f"A session has been scheduled with {request.user.full_name} on {session.scheduled_time}. Event link: {event_link}"
            )
            Notification.objects.create(
                user=request.user,
                message=f"A session has been scheduled with {mentorship_request.mentor.full_name} on {session.scheduled_time}. Event link: {event_link}"
            )

            return redirect('participant_dashboard')
    else:
        form = SessionForm()
    return render(request, 'capstone/schedule_session.html', {'form': form, 'mentorship_request': mentorship_request})

def chat_with_mentor(request, request_id):
    mentorship_request = get_object_or_404(MentorshipRequest, id=request_id, mentee=request.user)
    chat_messages = ChatMessage.objects.filter(mentorship_request=mentorship_request).order_by('timestamp')

    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.mentorship_request = mentorship_request
            chat_message.sender = request.user
            chat_message.save()

            
            if not mentorship_request.mentor.is_active:
                send_mail(
                    'New Message from Your Mentee',
                    f'Hi {mentorship_request.mentor.full_name},\n\nYou have a new message from {request.user.full_name}.\nLog in to check it.\n\nBest,\nHustle Platform Team',
                    settings.DEFAULT_FROM_EMAIL,
                    [mentorship_request.mentor.email],
                    fail_silently=False,
                )

            return redirect('chat_with_mentor', request_id=request_id)
    else:
        form = ChatMessageForm()

    return render(request, 'capstone/chat_with_mentor.html', {'form': form, 'chat_messages': chat_messages, 'mentorship_request': mentorship_request})


@login_required
def manage_mentorship_requests(request):
    mentorship_requests = MentorshipRequest.objects.filter(mentor=request.user, status='pending')
    return render(request, 'capstone/manage_mentorship_requests.html', {'mentorship_requests': mentorship_requests})

@login_required
def approve_mentorship_request(request, request_id):
    mentorship_request = get_object_or_404(MentorshipRequest, id=request_id, mentor=request.user)
    if request.method == 'POST':
        form = MentorshipResponseForm(request.POST, instance=mentorship_request)
        if form.is_valid():
            mentorship_request.status = 'approved'  
            form.save()

        
            mentee_profile, created = ParticipantProfile.objects.get_or_create(user=mentorship_request.mentee)
            mentee_profile.mentor = request.user  
            mentee_profile.save()

            
            Notification.objects.create(
                user=mentorship_request.mentee,
                message=f"Your mentorship request has been approved by {request.user.full_name}. Response: {mentorship_request.mentor_response}"
            )

            messages.success(request, f"You are now mentoring {mentorship_request.mentee.full_name}.")
            return redirect('manage_mentorship_requests')
    else:
        form = MentorshipResponseForm(initial={'status': 'approved'})
    return render(request, 'capstone/mentorship_response.html', {'form': form, 'mentorship_request': mentorship_request})

@login_required
def decline_mentorship_request(request, request_id):
    mentorship_request = get_object_or_404(MentorshipRequest, id=request_id, mentor=request.user)
    if request.method == 'POST':
        form = MentorshipResponseForm(request.POST, instance=mentorship_request)
        if form.is_valid():
            mentorship_request.status = 'declined'  
            form.save()
            
            Notification.objects.create(
                user=mentorship_request.mentee,
                message=f"Your mentorship request has been declined by {request.user.full_name}. Response: {mentorship_request.mentor_response}"
            )
            return redirect('manage_mentorship_requests')
    else:
        form = MentorshipResponseForm(initial={'status': 'declined'})
    return render(request, 'capstone/mentorship_response.html', {'form': form, 'mentorship_request': mentorship_request})

def chat_with_mentee(request, request_id):
    mentorship_request = get_object_or_404(MentorshipRequest, id=request_id, mentor=request.user)
    chat_messages = ChatMessage.objects.filter(mentorship_request=mentorship_request).order_by('timestamp')

    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.mentorship_request = mentorship_request
            chat_message.sender = request.user
            chat_message.save()

    
            if not mentorship_request.mentee.is_active:
                send_mail(
                    'New Message from Your Mentor',
                    f'Hi {mentorship_request.mentee.full_name},\n\nYou have a new message from {request.user.full_name}. Log in to check it.\n\nBest,\nHustle Platform Team',
                    settings.EMAIL_HOST_USER,
                    [mentorship_request.mentee.email],
                    fail_silently=False,
                )

            return redirect('chat_with_mentee', request_id=request_id)
    else:
        form = ChatMessageForm()

    return render(request, 'capstone/chat_with_mentee.html', {'form': form, 'chat_messages': chat_messages, 'mentorship_request': mentorship_request})

@login_required
def manage_schedule(request):
    sessions = Session.objects.filter(mentorship_request__mentor=request.user).order_by('scheduled_time')
    return render(request, 'capstone/manage_schedule.html', {'sessions': sessions})

def job_listings(request):
    job_listings = JobListing.objects.all()
    location = request.GET.get('location')
    industry = request.GET.get('industry')
    job_type = request.GET.get('job_type')

    if location:
        job_listings = job_listings.filter(location__icontains=location)
    if industry:
        job_listings = job_listings.filter(industry__icontains=industry)
    if job_type:
        job_listings = job_listings.filter(job_type=job_type)

        
    job_applications = JobApplication.objects.filter(user=request.user)



    context = {
        'job_listings': job_listings,
        'job_applications': job_applications, 
    }
    return render(request, 'capstone/job_listings.html', context)

@login_required
def save_job(request, job_id):
    job_listing = get_object_or_404(JobListing, id=job_id)
    SavedJob.objects.get_or_create(user=request.user, job_listing=job_listing)
    return redirect('job_listings')


@login_required
def apply_for_job(request, job_id):
    job_listing = get_object_or_404(JobListing, id=job_id)
    mentor = job_listing.employer  

    if request.method == 'POST':
        print("POST request received!")  
        print("POST Data:", request.POST)  
        print("FILES Data:", request.FILES) 

        form = JobSubmitForm(request.POST, request.FILES) 
        if form.is_valid():
            print("Form is valid!")  
            job_application = form.save(commit=False)
            job_application.user = request.user
            job_application.job_listing = job_listing
            job_application.save()
            print("Job application saved!")  

            
            Notification.objects.create(
                user=mentor,  
                message=f"{request.user.full_name} has applied for your job listing: {job_listing.title}.",
                job_application=job_application,
            )

            return redirect('job_application_tracker')  
        else:
            print("Form Errors:", form.errors)  

    else:
        form = JobSubmitForm(initial={'job_listing': job_listing})

    return render(request, 'capstone/apply_for_job.html', {
        'form': form,
        'job_listing': job_listing,
    })



@login_required
def job_application_tracker(request):
    job_applications = JobApplication.objects.filter(user=request.user)
    context = {
        'job_applications': job_applications,
    }
    return render(request, 'capstone/job_application_tracker.html', context)



@login_required
def manage_applicants(request, job_id):
    job_listing = get_object_or_404(JobListing, id=job_id, employer=request.user)
    job_applications = JobApplication.objects.filter(job_listing=job_listing, status='submitted')
    context = {
        'job_listing': job_listing,
        'job_applications': job_applications,
    }
    return render(request, 'capstone/manage_applicants.html', context)


def update_application_status(request, application_id, status):
    return JsonResponse({"message": "Application status updated!"})


@login_required
def mark_notification_seen(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_seen = True
    notification.save()
    return redirect('participant_dashboard')

@login_required
def upvote_message(request, message_id):
    message = get_object_or_404(ChatMessage, id=message_id)
    message.upvotes += 1
    message.save()
    return redirect('chat_with_mentor', request_id=message.mentorship_request.id)

@login_required
def downvote_message(request, message_id):
    message = get_object_or_404(ChatMessage, id=message_id)
    message.downvotes += 1
    message.save()
    return redirect('chat_with_mentor', request_id=message.mentorship_request.id)



@login_required
def google_callback(request):
    
    get_google_calendar_service()
    return redirect('participant_dashboard')

@login_required
def create_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.created_by = request.user  
            thread.save()
            return redirect('thread_detail', thread_id=thread.id)  
    else:
        form = ThreadForm()  
    return render(request, 'capstone/create_thread.html', {'form': form})

@login_required
def mcreate_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.created_by = request.user  
            thread.save()
            return redirect('mentorthread_detail', thread_id=thread.id)  
    else:
        form = ThreadForm()  
    return render(request, 'capstone/mentor-create_thread.html', {'form': form})

@login_required
def reply_to_thread(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        Comment.objects.create(thread=thread, user=request.user, text=text)
        return redirect('thread_detail', thread_id=thread.id)
    return render(request, 'capstone/reply_to_thread.html', {'thread': thread})

@login_required
def vote_comment(request, comment_id, vote_type):
    comment = get_object_or_404(Comment, id=comment_id)  

    
    existing_vote = Vote.objects.filter(user=request.user, comment=comment).first()
    if existing_vote:
        if existing_vote.vote_type != vote_type:
            if vote_type == 'upvote':
                comment.upvotes += 1
                comment.downvotes -= 1
            else:
                comment.upvotes -= 1
                comment.downvotes += 1
            existing_vote.vote_type = vote_type
            existing_vote.save()
    else:
        if vote_type == 'upvote':
            comment.upvotes += 1
        else:
            comment.downvotes += 1
        Vote.objects.create(user=request.user, comment=comment, vote_type=vote_type)

    
    comment.save()

    
    return redirect('thread_detail', thread_id=comment.thread.id)

@login_required
def mvote_comment(request, comment_id, vote_type):
    comment = get_object_or_404(Comment, id=comment_id)  

    
    existing_vote = Vote.objects.filter(user=request.user, comment=comment).first()
    if existing_vote:
        
        if existing_vote.vote_type != vote_type:
            
            if vote_type == 'upvote':
                comment.upvotes += 1
                comment.downvotes -= 1
            else:
                comment.upvotes -= 1
                comment.downvotes += 1
            existing_vote.vote_type = vote_type
            existing_vote.save()
    else:
        
        if vote_type == 'upvote':
            comment.upvotes += 1
        else:
            comment.downvotes += 1
        Vote.objects.create(user=request.user, comment=comment, vote_type=vote_type)

    
    comment.save()

    
    return redirect('mentorthread_detail', thread_id=comment.thread.id)


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    user = request.user  

  
    is_mentor = hasattr(user, 'mentor')  
    is_admin = user.is_staff or user.is_superuser

    if user == comment.user or is_mentor or is_admin:
        thread_id = comment.thread.id
        comment.delete()
        return redirect(reverse('thread_detail', args=[thread_id]))
    
    
    return HttpResponseForbidden("You are not allowed to delete this comment.")

@login_required
def mdelete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    user = request.user  

    
    is_mentor = hasattr(user, 'mentor')  
    is_admin = user.is_staff or user.is_superuser

    if user == comment.user or is_mentor or is_admin:
        thread_id = comment.thread.id
        comment.delete()
        return redirect(reverse('mentorthread_detail', args=[thread_id]))
    
    
    return HttpResponseForbidden("You are not allowed to delete this comment.")


def list_threads(request):
    
    threads = Thread.objects.all().order_by('-created_at')  
    return render(request, 'capstone/list_threads.html', {'threads': threads})

def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    return render(request, 'capstone/thread_detail.html', {'thread': thread})

def vote_thread(request, thread_id, action):
    thread = get_object_or_404(Thread, id=thread_id)
    
    if action == "upvote":
        thread.upvotes += 1
    elif action == "downvote":
        thread.downvotes += 1
    
    thread.save()
    return redirect('list_threads') 

def mentorlist_threads(request):
    
    threads = Thread.objects.all().order_by('-created_at')  
    return render(request, 'capstone/mentor-list_threads.html', {'threads': threads})

def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    return render(request, 'capstone/thread_detail.html', {'thread': thread})

def mentorthread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    return render(request, 'capstone/mentor-thread_detail.html', {'thread': thread})

def vote_thread(request, thread_id, action):
    thread = get_object_or_404(Thread, id=thread_id)
    
    if action == "upvote":
        thread.upvotes += 1
    elif action == "downvote":
        thread.downvotes += 1
    
    thread.save()
    return redirect('list_threads') 

def mvote_thread(request, thread_id, action):
    thread = get_object_or_404(Thread, id=thread_id)
    
    if action == "upvote":
        thread.upvotes += 1
    elif action == "downvote":
        thread.downvotes += 1
    
    thread.save()
    return redirect('mentorlist_threads') 

@login_required
def delete_thread(request, id):
    thread = get_object_or_404(Thread, id=id)
    
    if request.user == thread.created_by or request.user.is_staff:
        thread.delete()

    return redirect('list_threads')

@login_required
def mdelete_thread(request, id):
    thread = get_object_or_404(Thread, id=id)
    
    if request.user == thread.created_by or request.user.is_staff:
        thread.delete()

    return redirect('mentorlist_threads')

@login_required
def account_settings(request):
    return render(request, 'capstone/account_settings.html')

@login_required
def maccount_settings(request):
    return render(request, 'capstone/mentor-account_settings.html')

@login_required
def change_email(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data['new_email']
            request.user.email = new_email
            request.user.save()
            messages.success(request, 'Your email has been updated successfully.')
            return redirect('account_settings')
    else:
        form = ChangeEmailForm()
    return render(request, 'capstone/change_email.html', {'form': form})

@login_required
def mchange_email(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data['new_email']
            request.user.email = new_email
            request.user.save()
            messages.success(request, 'Your email has been updated successfully.')
            return redirect('mentor-account_settings')
    else:
        form = ChangeEmailForm()
    return render(request, 'capstone/mentor-change_email.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()  
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password has been updated successfully.')
            return redirect('login')  
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'capstone/change_password.html', {'form': form})

@login_required
def mchange_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()  
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password has been updated successfully.')
            return redirect('login')  
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'capstone/mentor-change_password.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        form = DeleteAccountForm(request.POST)
        if form.is_valid():
            request.user.delete()  
            logout(request)  
            messages.success(request, 'Your account has been deleted successfully.')
            return redirect('login')
    else:
        form = DeleteAccountForm()
    return render(request, 'capstone/delete_account.html', {'form': form})

@login_required
def mdelete_account(request):
    if request.method == 'POST':
        form = DeleteAccountForm(request.POST)
        if form.is_valid():
            request.user.delete()  
            logout(request)  
            messages.success(request, 'Your account has been deleted successfully.')
            return redirect('login')
    else:
        form = DeleteAccountForm()
    return render(request, 'capstone/mentor-delete_account.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.user_type == 'mentor' or u.is_superuser)
def mentor_job_listings(request):
    """Mentors can upload and view job listings."""
    job_listings = JobListing.objects.filter(employer=request.user)

    if request.method == 'POST':
        form = JobUploadForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user 
            job.save()

             
            participants = User.objects.filter(user_type='participant')
            for participant in participants:
                Notification.objects.create(
                    user=participant,
                    message=f"A new job has been posted: {job.title}."
                )

            messages.success(request, "Job listing created successfully!")
            return redirect('mentor_job_listings')
    else:
        form = JobUploadForm()

    context = {
        'job_listings': job_listings,
        'form': form,
    }
    return render(request, 'capstone/mentor-job_listings.html', context)

@login_required
def rate_mentor(request, mentor_id):
    mentor = get_object_or_404(User, id=mentor_id, user_type='mentor')

    if request.method == 'POST':
        form = MentorRatingForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.mentor = mentor
            feedback.mentee = request.user  
            feedback.save()
            messages.success(request, "Your feedback has been submitted successfully!")
            return redirect('participant_dashboard')

    else:
        form = MentorRatingForm()

    return render(request, 'capstone/rate_mentor.html', {'form': form, 'mentor': mentor})

@login_required
def notification_seen(request, notification_id, job_id):
    """ Marks a notification as seen and redirects the mentor to manage applicants. """
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_seen = True
    notification.save()

    return redirect('manage_applicants', job_id=job_id)



@login_required
def update_application_status(request, application_id, status):
    job_application = get_object_or_404(JobApplication, id=application_id, job_listing__employer=request.user)

    # ✅ Update application status
    # ✅ If the mentor accepts the application, store their email
    if status == "accepted":
        job_application.accepted_by_mentor_email = request.user.email  # Mentor's email
    else:
        job_application.accepted_by_mentor_email = None
    job_application.status = status
    job_application.save()

    # ✅ Notify the participant
    Notification.objects.create(
        user=job_application.user,  # Notify the applicant
        message=f"Your application for '{job_application.job_listing.title}' has been {status.replace('_', ' ')}.",
    )

    # ✅ Remove application from Manage Applicants Page (Redirect back)
    messages.success(request, f"Application {status.replace('_', ' ')} successfully!")
    return redirect('manage_applicants', job_id=job_application.job_listing.id)
