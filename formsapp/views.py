from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


##### Display Form to retrieve student information using get method

def get_student_info(request):
    return render(request, "form_student_info.html")

###### Use form - method=get retrieve all form values and display them on the same page

def get_student_info_from_form (request):
    try:
        student_info = ""
        firstname = str(request.GET.get("first_name"))
        if firstname != "":
            student_info += " First Name:   " + firstname + "</br>"
        else:
            student_info += " First Name:   " + "Not Entered" + "</br>"

        lastname = str(request.GET.get("last_name"))
        if lastname != "":
            student_info += " Last Name:   " + lastname + "</br>"
        else:
            student_info += " Last Name:   " + "Not Entered" + "</br>"

        program_enrolled = str(request.GET.get("program"))
        if program_enrolled != "":
            student_info += " Program Enrolled:   " + program_enrolled + "</br>"
        else:
            student_info += " Program Enrolled:   " + "Not Enrolled Yet!" + "</br>"

        student_number = str(request.GET.get("student_number"))
        if student_number != "":
            student_info += " Student Number entered:   " + student_number + "</br>"
        else:
            student_info += " Student Number entered:   " + "Not Entered Yet!" + "</br>"

        my_enrollment_status = str(request.GET.get("my_status"))

        if my_enrollment_status != "":
            student_info += " Enrollment status: " + my_enrollment_status + "</br>"
        else:
            student_info += " My Enrollment status is NOT selected!  </br>"

        year_enrolled = ""
        first_year = str(request.GET.get("year1"))
        second_year = str(request.GET.get("year2"))
        third_year = str(request.GET.get("year3"))
        fourth_year = str(request.GET.get("year4"))
        if first_year == "" and second_year == "" and third_year == "" and fourth_year == "":
            year_enrolled += " Not currently enrolled in the program yet! </br>"
        if first_year == "year1":
            year_enrolled += " Enrolled in First Year courses </br>"
        if second_year == "year2":
            year_enrolled += " Enrolled in Second Year courses  </br>"
        if third_year == "year3":
            year_enrolled += " Enrolled in Third Year courses  </br>"
        if fourth_year == "year4":
            year_enrolled += " Enrolled in Fourth Year courses  </br>"

        student_info += "</br></br>"
        student_info += year_enrolled

        student_data_display = {}
        student_data_display['output_info'] = student_info
        print(student_data_display)

    except:
        pass

    return HttpResponse(student_info)
