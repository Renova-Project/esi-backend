from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'secteurs', views.SecteurViewSet)
router.register(r'organismes', views.OrganismeViewSet)
router.register(r'typestages', views.TypeStageViewSet)
router.register(r'stages', views.StageViewSet)
router.register(r'candidats', views.CandidatViewSet)
router.register(r'demandes', views.DemandeViewSet)
router.register(r'offrestages', views.OffreStageViewSet)

urlpatterns = [
  path('', include(router.urls)),
]