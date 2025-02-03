from msvcrt import getch
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm, ParticipantProfileForm, MentorProfileForm, FeedbackForm, ResourceSearchForm, ResourceUploadForm, RatingForm, MentorshipRequestForm, SessionForm, ChatMessageForm, JobApplicationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User, MenteeActivity, Question, Message, ParticipantProfile, MentorProfile, Feedback, Progress, Resource, MentorshipRequest, ChatMessage, Session, JobListing, SavedJob, JobApplication
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import Avg


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']
            
            # Authenticate using the email as username
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
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'capstone/signup.html', {'form': form})

def mentor_terms(request):
    return render(request, 'capstone/mentor_terms.html')

def participant_terms(request):
    return render(request, 'capstone/participant_terms.html')

@login_required
def participant_dashboard(request):
    if request.user.user_type != 'participant':
        return redirect('login')  # Redirect to login if user is not a participant
    progress = 75  # Example progress value
    notifications = [
        "New resource: Python Basics",
        "Mentor response: Feedback on your project",
    ]
    context = {
        'user': request.user,
        'progress': progress,
        'notifications': notifications,
    }
    return render(request, 'capstone/participant_dashboard.html', context)

@login_required
def mentor_dashboard(request):
    if request.user.user_type != 'mentor':
        return redirect('login')  # Redirect to login if user is not a mentor
    #Fetch data for the mentor
    mentee_activities = MenteeActivity.objects.filter(mentor=request.user).order_by('-timestamp')[:5]  # Last 5 activities
    questions = Question.objects.filter(mentor=request.user).order_by('-timestamp')[:5]  # Last 5 questions
    messages = Message.objects.filter(mentor=request.user).order_by('-timestamp')[:5]  # Last 5 messages

    context = {
        'user': request.user,
        'mentee_activities': mentee_activities,
        'questions': questions,
        'messages': messages,
    }
    
    return render(request, 'capstone/mentor_dashboard.html', context)

@login_required
def participant_profile(request):
    profile, created = ParticipantProfile.objects.get_or_create(user=request.user)
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
    return render(request, 'capstone/participant_profile.html', {'form': form, 'progress_percentage': progress_percentage})

@login_required
def mentor_profile(request):
    profile, created = MentorProfile.objects.get_or_create(user=request.user)
    mentees = ParticipantProfile.objects.filter(mentor=request.user)
    feedbacks = Feedback.objects.filter(mentor=request.user)

    if request.method == 'POST':
        form = MentorProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('mentor_profile')
    else:
        form = MentorProfileForm(instance=profile)
    return render(request, 'capstone/mentor_profile.html', {'form': form, 'mentees': mentees, 'feedbacks': feedbacks})

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
    resources = Resource.objects.all().annotate(avg_rating=Avg('ratings__rating')).order_by('id')
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
    
    # Pagination
    paginator = Paginator(resources, 5)  # Show 5 resources per page
    page_number = request.GET.get('page')
    if not page_number: 
        page_number = 1
    try:
        resources = paginator.page(page_number)
    except PageNotAnInteger:
        resources = paginator.page(1)
    except EmptyPage:
        resources = paginator.page(paginator.num_pages)

    context = {
        'resources': resources,
        'form': form,
    }
    return render(request, 'capstone/learning_resources.html', context)

@login_required
@user_passes_test(lambda u: u.user_type == 'mentor' or u.is_superuser)
def upload_resource(request):
    if request.method == 'POST':
        form = ResourceUploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_resources')
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
    if request.method == 'POST':
        form = MentorshipRequestForm(request.POST)
        if form.is_valid():
            mentorship_request = form.save(commit=False)
            mentorship_request.mentee = request.user
            mentorship_request.save()
            return redirect('participant_dashboard')
    else:
        form = MentorshipRequestForm()
    return render(request, 'capstone/submit_mentorship_request.html', {'form': form})

@login_required
def schedule_session(request, request_id):
    mentorship_request = get_object_or_404(MentorshipRequest, id=request_id, mentee=request.user)
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.mentorship_request = mentorship_request
            session.save()
            return redirect('mentee_dashboard')
    else:
        form = SessionForm()
    return render(request, 'capstone/schedule_session.html', {'form': form, 'mentorship_request': mentorship_request})

@login_required
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
    mentorship_request.status = 'approved'
    mentorship_request.save()
    return redirect('manage_mentorship_requests')

@login_required
def decline_mentorship_request(request, request_id):
    mentorship_request = get_object_or_404(MentorshipRequest, id=request_id, mentor=request.user)
    mentorship_request.status = 'declined'
    mentorship_request.save()
    return redirect('manage_mentorship_requests')

@login_required
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

    context = {
        'job_listings': job_listings,
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
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.user = request.user
            job_application.job_listing = job_listing
            job_application.save()
            return redirect('job_application_tracker')
    else:
        form = JobApplicationForm(initial={'job_listing': job_listing})
    return render(request, 'capstone/apply_for_job.html', {'form': form, 'job_listing': job_listing})

@login_required
def job_application_tracker(request):
    job_applications = JobApplication.objects.filter(user=request.user)
    context = {
        'job_applications': job_applications,
    }
    return render(request, 'capstone/job_application_tracker.html', context)

@login_required
def employer_dashboard(request):
    if request.user.user_type != 'mentor' and not request.user.is_superuser:
        return redirect('login')  # Only mentors and admins can access
    job_listings = JobListing.objects.filter(employer=request.user)
    context = {
        'job_listings': job_listings,
    }
    return render(request, 'capstone/employer_dashboard.html', context)

@login_required
def manage_applicants(request, job_id):
    job_listing = get_object_or_404(JobListing, id=job_id, employer=request.user)
    job_applications = JobApplication.objects.filter(job_listing=job_listing)
    context = {
        'job_listing': job_listing,
        'job_applications': job_applications,
    }
    return render(request, 'capstone/manage_applicants.html', context)


def update_application_status(request, application_id, status):
    return JsonResponse({"message": "Application status updated!"})
