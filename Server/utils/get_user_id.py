from django.shortcuts import get_object_or_404
from Users.models import CustomUser
from django.contrib.sessions.models import Session


# get user id by sessionid
def get_user_by_sessionid(sessionid):
    if not sessionid:
        raise ValueError("Forbidden")

    try:
        session = Session.objects.get(pk=sessionid)
        user = get_object_or_404(
            CustomUser, pk=session.get_decoded().get("_auth_user_id")
        )
        return user
    except Exception:
        raise ValueError("Forbidden")
