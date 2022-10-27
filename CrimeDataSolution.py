#imports
import csv

# functions
def month_from_number(n):
    
    months = {1:'January', 2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    
    return months[n]

def read_in_file(filename):

    content = []
    
    file = open(filename, encoding="UTF-8")
    file_csv = csv.reader(file)

    for line in file_csv:
        content.append(line)

    file.close()
    
    return content

def create_reported_date_dict(lst):

    my_dict = {}

    for i in range(1, len(lst)):
        if(lst[i][1] not in my_dict):
            my_dict[lst[i][1]] = 1
        else:
            my_dict[lst[i][1]] += 1
    
    return my_dict


def create_reported_month_dict(lst):
    my_dict = {}

    for i in range(1, len(lst)):
        if((lst[i][1])[:2] not in my_dict):
            my_dict[(lst[i][1])[:2]] = 1
        else:
            my_dict[(lst[i][1])[:2]] += 1

    return my_dict

def create_offense_dict(lst):
    my_dict = {}

    for i in range(1, len(lst)):
        if(lst[i][7] not in my_dict):
            my_dict[lst[i][7]] = 1
        else:
            my_dict[lst[i][7]] += 1
    
    return my_dict


def create_offense_by_zip(lst):
    offense_and_zip = []
    my_dict = {}
    occurrences = []
    
    for i in range(1, len(lst)):
        offense_and_zip.extend([[lst[i][7], lst[i][13]]])
    
    for element in offense_and_zip:
        occurrences.append(offense_and_zip.count(element))
    
    for i in range(len(offense_and_zip)):
        if(offense_and_zip[i][0] not in my_dict):
            my_dict.update({offense_and_zip[i][0]:{}})

        my_dict[offense_and_zip[i][0]].update({offense_and_zip[i][1]:occurrences[i]})

    return my_dict



if __name__ == "__main__":

    # Main program
    print("KCPD Crime Data")

    while(True):
        try:
            file = input("Enter the name of the crime data file ==> ")
            content = read_in_file(file)
            break
        except FileNotFoundError:
            print(f"Could not find {file}. Please try again.")
            
    print(create_offense_by_zip(content))
    worst_month = max(create_reported_month_dict(content), key=create_reported_month_dict(content).get)
    num_offenses_in_worst_month = max(create_reported_month_dict(content).values())

    print(month_from_number(int(worst_month)), num_offenses_in_worst_month)

    most_common_offense = max(create_offense_dict(content), key=create_offense_dict(content).get) 
    most_common_offense_name = max(create_offense_dict(content).values())

    print(most_common_offense, most_common_offense_name)

    

    
