"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from firstapp import views
from formsapp import views as form_view
from form_to_file_app import views as file_form
from post_form_app import views as post_form_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mytestpage', views.first_testpage),
    path('myhtmlpage', views.my_html_page),
    path('', views.home_page),
    ##### Following page displays contents of list in html list format
    path('mylist', views.display_list_function),

    ####################### Following page displays contents read from binary file
    ######## first data is saved from dictionary and then it is read and displayed

    path('data_display_from_file', views.display_file_data),

    ###############################################################################
    #######  Using the app named as formsapp  ####################################

    ########## Display form to use get method  -- Displays form

    path('student_info', form_view.get_student_info),
    ###################################################################

    ##################################################################
    ######### Display data from the form ############################
    ##################################################################

    path('student_data_display', form_view.get_student_info_from_form),

    ##################################################################
    ##################################################################################
    ########################### Web pages from data from file ########################
    ############################ Following web pages are used for file processing ####
    ##################################################################################

    path('student_data_save_display', file_form.save_student_info),

    ############################################################################

    ######################## following either saves or displays data from file #####
    ############################################################################
    path('process_data', file_form.process_data_file),

    #############################################################################
    ###############################################################################
    ############################################################################

    ####### Following pages are from the app name as   post_form_app ###########

    ############################################################################
    ############################################################################

    ################### display form with post method  ###############################

    path('display_post_form', post_form_views.get_student_info_post_form),

    ##################################################################################

    ######################## process to display data from post-form ##

    path('student_data_post_form', post_form_views.get_student_info_from_post_form),



]
