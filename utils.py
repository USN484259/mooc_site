from django.shortcuts import redirect
def check_user(req):
    if req.user.is_authenticated:
        return
    return redirect("/account/login?next="+req.path)