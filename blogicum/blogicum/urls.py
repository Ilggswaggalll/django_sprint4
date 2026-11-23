from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.urls import include, path, reverse_lazy
from django.views.generic import CreateView


class ConfirmLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/logout_confirm.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/registration/', CreateView.as_view(
        form_class=UserCreationForm,
        template_name='registration/registration_form.html',
        success_url=reverse_lazy('login'),
    ), name='registration'),
    path('auth/logout/', ConfirmLogoutView.as_view(), name='logout'),
    path('auth/', include('django.contrib.auth.urls')),
    path('pages/', include('pages.urls')),
    path('', include('blog.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'
