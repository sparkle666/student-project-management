from django.conf import settings


def add_debug(request):
    return {'DEBUG': settings.DEBUG}
