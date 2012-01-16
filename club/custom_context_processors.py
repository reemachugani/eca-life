from club.models import Club
from profiles.models import StudentProfile

def my_club_list(request):
    my_club_list=[]
    for club in Club.objects.all():
        if StudentProfile.objects.get(user = request.user) in club.members.all():
            my_club_list.append(club)
    
    return {'my_club_list': my_club_list}