from core.models import SiteSettings

def site_settings(request):
    try:
        settings = SiteSettings.objects.first()
    except:
        # If database isn't ready or SiteSettings doesn't exist
        settings = None
    
    return {
        'site_settings': settings
    }
