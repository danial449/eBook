"""
URL configuration for ebook_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
     path("", include("books.urls")),
     path("", include("users.urls")),
     path("", include("cart.urls")),


     # password Change
    path('password_change/' , auth_views.PasswordChangeView.as_view() , name='password_change'), #as_view is used for class based views cuz passwordchangeview is django builtin vie which is class-based view
    path('password_change/done/' , auth_views.PasswordChangeDoneView.as_view() , name='password_change_done'), 
    #password Reset
    path('password_reset/' , auth_views.PasswordResetView.as_view() , name='password_reset'), 
    path('password_reset/done/' , auth_views.PasswordResetDoneView.as_view() , name='password_reset_done'), 
    path('reset/<uidb64>/<token>' , auth_views.PasswordResetConfirmView.as_view() , name='password_reset_confirm'), 
    path('reset/done/' , auth_views.PasswordResetCompleteView.as_view() , name='password_reset_complete'), 
]
 # there is password manage process given below:

    # password_change
    # password_change_done

    # password_reset
    # password_reset_done
    # password_reset_confirm
    # password_reset_complete

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()