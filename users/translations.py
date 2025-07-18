# Custom translation system for English to Telugu

TRANSLATIONS = {
    'en': {
        # Settings
        'Settings': 'Settings',
        'Theme': 'Theme',
        'Language': 'Language',
        'Light': 'Light',
        'Dark': 'Dark',
        'English': 'English',
        'Telugu': 'Telugu',
        'Save_Settings': 'Save Settings',
        
        # Navigation
        'Home': 'Home',
        'Tools': 'Tools',
        'Categories': 'Categories',
        'Favourites': 'Favourites',
        'History': 'History',
        'Reviews': 'Reviews',
        'Feedback': 'Feedback',
        'Profile': 'Profile',
        'Logout': 'Logout',
        'Login': 'Login',
        'Register': 'Register',
        
        # Common
        'View_Details': 'View Details',
        'Added_on': 'Added on',
        'Category': 'Category',
        'Viewed_on': 'Viewed on',
        'You_havent_added_any_tools_to_your_favourites_yet': 'You haven\'t added any tools to your favourites yet.',
        'You_havent_viewed_any_tools_yet': 'You haven\'t viewed any tools yet.',
        
        # Tool related
        'Your_Favourite_Tools': 'Your Favourite Tools',
        'Your_Tool_History': 'Your Tool History',
        'All_Tools': 'All Tools',
        'Tool_of_the_Day': 'Tool of the Day',
        
        # Auth
        'Change_Password': 'Change Password',
        'Current_Password': 'Current Password',
        'New_Password': 'New Password',
        'Confirm_New_Password': 'Confirm New Password',
        'Back_to_Profile': 'Back to Profile',
        
        # Feedback
        'Submit_Feedback': 'Submit Feedback',
        'Thank_you_for_your_feedback': 'Thank you for your feedback!',
        
        # Reviews
        'Add_Review': 'Add Review',
        'Reviews_Dashboard': 'Reviews Dashboard',
        'Tool_Reviews': 'Tool Reviews',
    },
    'te': {
        # Settings
        'Settings': 'సెట్టింగ్‌లు',
        'Theme': 'థీమ్',
        'Language': 'భాష',
        'Light': 'వెలుగు',
        'Dark': 'చీకటి',
        'English': 'ఆంగ్లం',
        'Telugu': 'తెలుగు',
        'Save_Settings': 'సెట్టింగ్‌లను సేవ్ చేయండి',
        
        # Navigation
        'Home': 'హోమ్',
        'Tools': 'సాధనాలు',
        'Categories': 'వర్గాలు',
        'Favourites': 'ఇష్టమైనవి',
        'History': 'చరిత్ర',
        'Reviews': 'సమీక్షలు',
        'Feedback': 'అభిప్రాయం',
        'Profile': 'ప్రొఫైల్',
        'Logout': 'లాగ్అవుట్',
        'Login': 'లాగిన్',
        'Register': 'నమోదు',
        
        # Common
        'View_Details': 'వివరాలను చూడండి',
        'Added_on': 'జోడించబడింది',
        'Category': 'వర్గం',
        'Viewed_on': 'చూసిన తేదీ',
        'You_havent_added_any_tools_to_your_favourites_yet': 'మీరు ఇంకా మీ ఇష్టమైన వాటికి ఏదైనా సాధనాలను జోడించలేదు.',
        'You_havent_viewed_any_tools_yet': 'మీరు ఇంకా ఏదైనా సాధనాలను చూడలేదు.',
        
        # Tool related
        'Your_Favourite_Tools': 'మీ ఇష్టమైన సాధనాలు',
        'Your_Tool_History': 'మీ సాధన చరిత్ర',
        'All_Tools': 'అన్ని సాధనాలు',
        'Tool_of_the_Day': 'నేటి సాధనం',
        
        # Auth
        'Change_Password': 'పాస్‌వర్డ్ మార్చండి',
        'Current_Password': 'ప్రస్తుత పాస్‌వర్డ్',
        'New_Password': 'కొత్త పాస్‌వర్డ్',
        'Confirm_New_Password': 'కొత్త పాస్‌వర్డ్ నిర్ధారించండి',
        'Back_to_Profile': 'ప్రొఫైల్‌కి తిరిగి వెళ్లండి',
        
        # Feedback
        'Submit_Feedback': 'అభిప్రాయాన్ని సమర్పించండి',
        'Thank_you_for_your_feedback': 'మీ అభిప్రాయానికి ధన్యవాదాలు!',
        
        # Reviews
        'Add_Review': 'సమీక్ష జోడించండి',
        'Reviews_Dashboard': 'సమీక్షల డాష్‌బోర్డ్',
        'Tool_Reviews': 'సాధన సమీక్షలు',
    }
}

def translate(text, language='en'):
    """
    Translate text to the specified language
    """
    if language not in TRANSLATIONS:
        return text
    
    return TRANSLATIONS[language].get(text, text)

def get_translation_context(language='en'):
    """
    Get a context dictionary with translated strings
    """
    if language not in TRANSLATIONS:
        return {}
    
    return {key: value for key, value in TRANSLATIONS[language].items()} 