from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    

    path("login/",views.loginPage, name="login"),
    path("regis/",views.registrationPage, name="regs"),
    path("logout/",views.logoutUser, name="logout"),
    
    path("",views.home , name="home"),
    path("user/",views.userPage, name="user-page"),

    path("account/",views.accountSettings , name="account"),


    path("products/",views.products , name="products"),
    path("customers/<str:pk>/",views.customers ,name="customer"),

    path("create_order/<str:pk>/", views.createOrder , name="create_order"),
    path("update_order/<str:pk>/", views.updateOrder , name="update_order"),
    path("delete_order/<str:pk>/", views.deleteOrder , name="delete_order"),


    path("reset_password/", auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_sent_form.html"), name='reset_password'),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name='password_reset_done'),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_sent_form.html"), name='password_reset_confirm'),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name='password_reset_complete'),


]



"""
1 - Submit email form                      //PasswordResetView.as_view()
2 - Email sent success message             //PasswordResetDoneView.as_view()
3 - Link to password Reset form in email   //PasswordResetConfirmView.as_view()
4 - Password succesfully changed message   //PasswordResetCompleteView.as_view()
"""