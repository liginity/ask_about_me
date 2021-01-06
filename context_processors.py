from django.conf import settings


def askqDebug(context):
    return {"askq_debug": settings.DEBUG}
