from rest_framework import routers

from .views import SignUpView


router = routers.DefaultRouter()
router.register(prefix='signup', viewset=SignUpView, basename='user-signup')

urls = router.urls
