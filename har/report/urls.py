from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_connection_view, name='connection'),
    path('reports', views.render_reports_view, name='reports_list'),
    path('report', views.render_report_creation_view, name='report_create'),
    path('report/<int:id>', views.render_report_update_view, name='report_update'),
    path('report/<int:id>/deletion', views.render_report_deletion_view, name='report_delete'),
]
