from django.urls import path
from content.apps import ContentConfig
from content import views

app_name = ContentConfig.name

urlpatterns = [
    path('docs/upload/', views.DocumentCreateAPIView.as_view(), name='doc_upload'),
    path('docs/', views.DocumentListAPIView.as_view(), name='docs_list'),
    path('docs/<int:pk>', views.DocumentRetrieveAPIView.as_view(), name='doc_detail'),
    path('docs/update/<int:pk>', views.DocumentUpdateAPIView.as_view(), name='doc_update'),
    path('docs/delete/<int:pk>', views.DocumentDestroyAPIView.as_view(), name='doc_delete'),
]
