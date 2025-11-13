from .settings import *

SESSION_COOKIE_NAME = 'sessionid_back'
CSRF_COOKIE_NAME = 'csrftoken_back'

LOGIN_URL = '/admin/login/'
LOGOUT_REDIRECT_URL = '/admin/login/'
