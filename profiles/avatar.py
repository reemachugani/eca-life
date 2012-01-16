from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from profiles.forms import AvatarUploadForm
from profiles.models import StudentProfile

def add_avatar(request):
    student = StudentProfile.objects.get(user = request.user)
    form = AvatarUploadForm(request.POST or None,
        request.FILES or None, instance=student)
    if request.method == 'POST' and 'avatar' in request.FILES:
        if form.is_valid():
            student.avatar = request.FILES['avatar']
            student.save()
        return redirect('/profiles/%s/' %request.user.username)
    return render_to_response('profiles/add_avatar.html', {'form':form}, context_instance = RequestContext(request))
            
            