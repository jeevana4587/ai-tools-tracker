from .translations import translate, get_translation_context

def user_theme_language(request):
    theme = 'light'
    language = 'en'
    if request.user.is_authenticated:
        settings = getattr(request.user, 'usersettings', None)
        if settings:
            theme = settings.theme
            language = settings.language
    
    # Get translation context for the current language
    translations = get_translation_context(language)
    
    return {
        'user_theme': theme,
        'user_language': language,
        'translations': translations,
    } 