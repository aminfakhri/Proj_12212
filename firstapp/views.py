from django.shortcuts import render
from django.http import HttpResponse
import pickle

# Create your views here.
def first_testpage(request):
    return render(request, "testpage.html")
########################################################

############### My second page ########################

def my_html_page(request):
    my_page = """
    <html>
    <head>
    <title> Information Page </title>
    </head>
    <body bgcolor='aqua'>

    <h1> Hello World </h1>
    <h2> This is my second page </h2>
    <h3> I am testing html page in this example </h3>
    </body>   
    </html>  
    """
    return HttpResponse(my_page)

#######################################################################
######################################################################
###### Another page - my third page

def home_page(request):
    my_page = """
        <html>
        <head>
        <title> Information Page </title>
        </head>
        <body bgcolor='yellow'>

        <h1> Hello World </h1>
        <h2> This is my third page </h2>
        <h3> I am testing html page in this example </h3>
        </body>   
        </html>  
        """
    return HttpResponse(my_page)

##################################################################################
##################################################################################

####### Following function creates html file using list  #####*********######*****

def my_function_list():
    computer_parts = ['CPU - i-11 Intel Processor', 'RAM - 64 GB', 'Secondary Storage - 10 TB', 'Keyboard;Mouse', 'Monitor 144 refresh cycle', 'GPU']
    my_info = """
    <body bgcolor='aqua'>
    <p ><h1 align="center">Muhammad Khan</h1> </p>
    <p ><h2 align="center">Student Number: N012345</h2></p>
    <p><h3 align="center"> Components of computer<h3/></h3></p>
    """
    list_head = "<ol type='i'>"
    end_list_head = "</ol>"
    li = "<li>"
    li_end = "</li>"
    display_list = ""

    my_info += list_head


    for component in computer_parts:
        display_list += li + component + li_end


    my_info += display_list

    my_info += end_list_head


    my_info += "</body>"


    return my_info  #### complete my_info is returned to the calling function

####################################################################################
####################################################################################
#### Call my_function_list() in the views.py function call display_list_function
def display_list_function(request):
    data_to_display=my_function_list()
    return HttpResponse(data_to_display)

#####################################################################################
#####################################################################################


############################# Working with Files  ##################################


####### Following function creates file and saves data in file
######## Next the same function opens file and creates web displayable function

def read_file_create_html ():


    file_name = "data.dat"
    #print("Content-type: text/html")
    #print()
    head_and_body = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    table {
      width: 80%;
      border: 2px solid red
    }
    th, td {
      border: 0px solid black;
      border-radius: 2px;
    }
    </style>
    </head>
    <body style='background:aqua'>
    """

    head_and_body_end = "</body>"
    vehicle_data = [{"car_dealer": "ABC Chevy", "vehicle_info": "Ford;VINF01234;White;Sedan;FWD", "city": "Toronto"},
                    {"car_dealer": "Nissan North", "vehicle_info": "Nissan;VINN01234;Grey;SUV;AWD",
                     "city": "Thunder Bay"},
                    {"car_dealer": "GMC City", "vehicle_info": "GMC;VINGMC01234;Black;Truck;AWD", "city": "Toronto"},
                    {"car_dealer": "Lexus GTA", "vehicle_info": "Lexus;VINL01234;White;SUV;AWD", "city": "Markham"},
                    {"car_dealer": "Nissan GTA", "vehicle_info": "Nissan;VINN4567;White;Sedan;FWD", "city": "Brampton"},
                    {"car_dealer": "Nissan GTA", "vehicle_info": "Rogue;VIN4568;Red;SUV;AWD", "city": "Toronto"},

                    ]

    file_info = open("data.dat", "wb")
    for data in vehicle_data:
        pickle.dump(data, file_info)
    file_info.close()

    def create_table(file_name):
        table_head = "<h2 align='center'> Muhammad Khan </h2>"
        table_head += "<h3 align='center'> Student ID: N012345 </h3> </br> </br>"
        table_head += "<table> <tr><th> Car Dealer </th> <th>Manufacturer </th> <th> VIN number </th> <th> Vehicle Color </th>"
        table_head += "<th> Vehicle type </th> <th> Vehicl Drive type </th> <th> City </th> </tr> "
        build_tab_rows = ""
        table_end = "</table>"

        file_info = open(file_name, "rb")

        tab_row = "<tr align='left'>"
        tab_row_end = "</tr>"
        tab_data = "<td align='left'>"
        tab_data_end = "</td>"

        while True:
            try:
                file_read_data = pickle.load(file_info)
                car_dealer = file_read_data["car_dealer"]
                city = file_read_data["city"]
                vehicle_info = file_read_data["vehicle_info"].split(';')
                vehicle_make = vehicle_info[0]
                vehicle_VIN = vehicle_info[1]
                vehicle_color = vehicle_info[2]
                vehicle_type = vehicle_info[3]
                vehicle_drive_type = vehicle_info[4]

                build_tab_rows += tab_row
                build_tab_rows += tab_data + car_dealer + tab_data_end
                build_tab_rows += tab_data + vehicle_make + tab_data_end
                build_tab_rows += tab_data + vehicle_VIN + tab_data_end
                build_tab_rows += tab_data + vehicle_color + tab_data_end
                build_tab_rows += tab_data + vehicle_type + tab_data_end
                build_tab_rows += tab_data + vehicle_drive_type + tab_data_end
                build_tab_rows += tab_data + city + tab_data_end
                build_tab_rows += tab_row_end

            except EOFError:
                file_info.close()
                break

        complete_table = head_and_body + table_head + build_tab_rows + table_end + head_and_body_end
        return (complete_table)
    #### Now call the inner function create_table(file_name)
    ########################################################
    ######################-----------------###############---------########
    data_from_file = create_table(file_name)
    return data_from_file
    #print(data_from_file)

################################################################################
###################### Create views.display_file_data ( request ) function

#################################################################################
#######--------***********--------------*********** ----------###################
########## After saving data in file --- Read data from file and return string  ###
### display function from the file

def display_file_data (request):
    file_data=read_file_create_html()
    return HttpResponse(file_data)


###############################################################################
##############################################################################