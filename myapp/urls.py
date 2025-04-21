from django.views.generic import TemplateView

urlpatterns += [
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
