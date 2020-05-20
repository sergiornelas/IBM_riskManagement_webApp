from django.shortcuts import redirect
from django.contrib import messages
from .models import exclude_patch
#from django.core.mail import send_mail

def exclude(request):
    if request.method == 'POST':
        
        client = request.user
        patch_id = request.POST['patch_id']
        title = request.POST['title']
        justification = request.POST['justification']
        exclude_date = request.POST['exclude_date']

        #Check if user has made inquiry already
        if request.user.is_authenticated:
            has_contacted = exclude_patch.objects.all().filter(patch_id=patch_id, client=client)
            if has_contacted:
                messages.error(request, 'You have already made an exception for this patch')
                return redirect('dashboard')
               
        exclude = exclude_patch(patch_id=patch_id, client=client, title=title, justification=justification, exclude_date=exclude_date)
        
        exclude.save()

        messages.success(request, "Your request has been submitted, an approver will get back to you soon")

        return redirect('dashboard')