from django.shortcuts import render
from django.http import HttpResponse
import pickle

# Create your views here.

############################ file processing from form
################### following page displays student form
#########################################################

###### ****** ######
def save_student_info(request):
    return render(request, "file_save_student_info.html")


###################

#################################### Following functions saves or retrieves and displays
########################################## data from file #################
def process_data_file(request):
    try:
        if request.method == "GET":
            if request.GET.get('save_data') == "save":
                student_data = {}
                student_data['first_name'] = request.GET.get('first_name')
                student_data['last_name'] = request.GET.get('last_name')
                student_data['student_number'] = request.GET.get('student_number')
                student_data['program'] = request.GET.get('program')
                student_data['my_status'] = request.GET.get('my_status')

                year_enrolled = ""
                first_year = str(request.GET.get("year1"))
                second_year = str(request.GET.get("year2"))
                third_year = str(request.GET.get("year3"))
                fourth_year = str(request.GET.get("year4"))
                if first_year == "" and second_year == "" and third_year == "" and fourth_year == "":
                    year_enrolled += " Not currently enrolled in the program yet! </br>"
                year_enrolled += first_year + ';'
                year_enrolled += second_year + ';'
                year_enrolled += third_year + ';'
                year_enrolled += fourth_year + ';'

                student_data['enrollment_year'] = year_enrolled
                file_name = "student.dat"
                try:
                    data_file = open(file_name, "ab")
                    pickle.dump(student_data, data_file)
                    data_file.close()
                except:
                    print("Error opening file....")

                return render(request, "file_save_student_info.html")

            elif request.GET.get('save_data') == 'display':
                display_table = """ 	<html>
    					<head>
    					<style>
    					table {
      						width: 80%;
      						border: 2px solid red
    						}
    						th, td {
      						border: 1px solid black;
      						border-radius: 2px;
    						}
    					</style>
    					</head>
    			    <body style='background:aqua'>"""
                display_table += "<h2 align='right'> Muhammad Khan </h2>"
                display_table += "<h2 align='right' > Student Number: N012345 </h2>"
                display_table += """
                                    <table>
                                    <tr>
                                    <th> First Name </th>
                                    <th> Last Name </th>
                                    <th> Student Number </th>
                                    <th> Program Enrolled </th>
                                    <th> Enrollment status </th>
                                    <th> Courses from Years </th>

                                    </tr>

                """
                file_name = "student.dat"
                try:
                    data_file = open(file_name, "rb")
                    data_from_file = {}
                    while True:
                        try:
                            data_from_file = pickle.load(data_file)
                            firstname = data_from_file['first_name']
                            lastname = data_from_file['last_name']
                            studentnumber = data_from_file['student_number']
                            program_enrolled_in = data_from_file['program']
                            my_enrollment_status = data_from_file['my_status']
                            enrolled_years = data_from_file['enrollment_year']

                            display_table += """
                                                <tr>
                                                <td align='center'> %s </td>
                                                <td align='center'> %s </td>
                                                <td align='center'> %s </td>
                                                <td align='center'> %s </td>
                                                <td align='center'> %s </td>
                                                <td align='center'> %s </td>
                                                </tr>

                            """ % (firstname, lastname, studentnumber, program_enrolled_in, my_enrollment_status,
                                   enrolled_years)
                        except:
                            data_file.close()
                            display_table += "</table> </body>"
                            break

                except:
                    print("Error opening file to read .. File may not exist")

    except:
        pass

    return HttpResponse(display_table)

########################################################################################################