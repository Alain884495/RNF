from .settings import *

SESSION_COOKIE_NAME = 'sessionid_front'
CSRF_COOKIE_NAME = 'csrftoken_front'

LOGIN_URL = '/front/login/'
LOGOUT_REDIRECT_URL = '/front/login/'
