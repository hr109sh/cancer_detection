from django.urls import path
from cancer_detection import views

app_name = 'cancer_detection'
urlpatterns = [
    path('cancer_detection/',views.radius_vs_texture,name="radius_vs_texture"),
    path('perimeter_vs_area/',views.perimeter_vs_area,name="perimeter_vs_area"),
    path('smoothness_vs_compactness/',views.smoothness_vs_compactness,name="smoothness_vs_compactness"),
    path('concavity_vs_concavepoints/',views.concavity_vs_concavepoints,name="concavity_vs_concavepoints"),
    path('symmetry_vs_fractaldimension/',views.symmetry_vs_fractaldimension,name="symmetry_vs_fractaldimension"),
    path('radius_se_vs_texture_se/',views.radius_se_vs_texture_se,name="radius_se_vs_texture_se"),
    path('perimeter_se_vs_area_se/',views.perimeter_se_vs_area_se,name="perimeter_se_vs_area_se"),
    path('smoothness_se_vs_compactness_se/',views.smoothness_se_vs_compactness_se,name="smoothness_se_vs_compactness_se"),
    path('concavity_se_vs_concavepoints_se/',views.concavity_se_vs_concavepoints_se,name="concavity_se_vs_concavepoints_se"),
    path('symmetry_se_vs_radius_worst/',views.symmetry_se_vs_radius_worst,name="symmetry_se_vs_radius_worst"),
    path('registration/',views.registration,name="registration"),
    path('user_registration/',views.user_registration,name="user_registration"),
    path('contact_form/',views.contact_form,name="contact_form")


]
