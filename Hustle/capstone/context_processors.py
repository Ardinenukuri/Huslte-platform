from .models import MentorshipRequest

def mentorship_requests(request):
    if request.user.is_authenticated and request.user.user_type == 'participant':
        return {
            'mentorship_requests': MentorshipRequest.objects.filter(mentee=request.user)
        }
    return {}
