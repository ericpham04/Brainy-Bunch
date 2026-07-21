from django.urls import path
from . import views
app_name="messages_app"
urlpatterns=[path("",views.inbox,name="inbox"),path("with/<int:user_id>/",views.conversation,name="conversation"),path("with/<int:user_id>/listing/<int:listing_id>/",views.conversation,name="conversation_with_listing")]
