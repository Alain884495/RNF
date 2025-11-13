# monprojet/monprojet/settings_front.py

from .settings import *

# --- Configuration spécifique au front (app utilisateur) ---

# Nom de cookie différent pour éviter les conflits avec /admin
SESSION_COOKIE_NAME = "front_sessionid"
CSRF_COOKIE_NAME = "front_csrftoken"

# Si tu développes en local
CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8000", "http://localhost"]

# (Optionnel) si tu veux changer le titre du site dans l'admin
# ADMIN_SITE_HEADER = "Gestion Front Utilisateur"
