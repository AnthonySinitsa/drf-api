# clouds :D

## About Project

clouds lol

### How To

- python manage.py runserver

- ###### pmp runserver

<http://0.0.0.0:8000/api/v1/clouds>

- docker compose up

settings.py
REST_FRAMEWORK

in urls.py
from rest_framework import permissions
urlpatterns = [
  path('api-auth/', include('rest_framework.urls')),   #this adds a login
]

touch clouds/permissions.py

in permissions.py
from rest_framework import permissions
class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permissions(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    if obj.owner is None:
      return True
    return obj.owner == request.user

in views.py
from .permissions import IsOwnerOrReadOnly
inside CloudList class
  permission_classes = (IsOwnerOrReadOnly)
inside CloudDetail class
  permission_classes = (IsOwnerOrReadOnly)

docker stuff
docker-compose.yml
copy pasta?

in settings.py
DATABASES = {
  copy pasta
}

pip install psycopg2-binary
pipf
dcu --build
should error that needs to migrate
pmp migrate   #but this won't work because this migrates on PC not docker
docker compose run web pmp migrate
dcu
docker compose down   # this properly shuts down container but it'll remove data
docker compose run web pmp createsuperuser
dcu -d    # this runs in detached mode
docker compose logs
docker compose run web pmp migrate
docker compose run web pmp createsuperuser
docker compose stop
docker compose start
