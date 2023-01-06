from rest_framework import routers

from .views import SignUpView, EditCredentialsView

router = routers.DefaultRouter()
router.register(prefix='signup', viewset=SignUpView, basename='signup')
router.register(prefix='edit_credentials', viewset=EditCredentialsView, basename='edit_credentials')

urls = router.urls
