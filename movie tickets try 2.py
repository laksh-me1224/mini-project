file=open("list of names.txt",'r')
data=file.readlines()
for line in data:
    print(line,end='')
file.close()    

'''
# verifying the age limit for the movie show
print("")
number_of_audience = int(input("Enter the number of audiance who is willing to watch the movie :"))
print("")
print("NOTE:The audience for this movie should me above the age limit of 18 as this is rated pg 18+")
print("")
#creating empty list 
initial_list_of_audiencename=[]
list_of_audiencename_noteligible=[]
list_of_audiencename_eligible=[]
list_of_audienceage=[]
for i in range(number_of_audience):
    #taking the name and the age of the audience to check if they are eligible to watch the movie 
    name=input("enter the name of audience :")
    age=int(input("enter age of audience "))
    #useing append method from list to add the name and age entered by the audience into the empty list
    initial_list_of_audiencename.append(name)
    list_of_audienceage.append(age)
#traversing elements of  audience age from the list 
for j in list_of_audienceage:
    if (j<18):#checking if the audience age is less than 18
        #comparing the index position of age in audience age list with the list of audience name 
        indexage=list_of_audienceage.index(j)
        indexname=initial_list_of_audiencename[indexage]
        list_of_audiencename_noteligible.append(indexname)# appending name of audience not eligibe to list 
    else:
        indexage=list_of_audienceage.index(j)
        indexname=initial_list_of_audiencename[indexage]
        list_of_audiencename_eligible.append(indexname)
print("list of audience who are not eligible to watch the movie as the movie is rated pg18+")
print(list_of_audiencename_noteligible)#printing the list of audience not eligible to watch the movie 
print('')
print("list of audience who are eligible to watch the movie:")#printing the list of audience eligible to watch the movie 
print('')
print(list_of_audiencename_eligible)


import csv
field=["name of audience eligible","name of audience not eligible"]
rows=[list_of_audiencename_eligible,list_of_audiencename_noteligible]
print(rows)

filename='audience list of a movie.csv'

with open(filename,'w',newline='')as f:
    csv_w=csv.writer(f,delimiter=',')
    csv_w.writerow(field)
    csv_w.writerow(rows[0])
    csv_w.writerow(rows[1])
    print("file created")
'''
