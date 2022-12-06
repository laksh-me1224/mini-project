''' Author: Lakshmi Senthilnathan
    SOB 28,29,30

An online movie booking site which wants to check if the audience who are willing to watch a movie is eligible or not eligible as the movie being rated pg
18+  

This programe checks if the audience who are willing to watch the movie is above 18 or no . Audience who are above 18 will be eligible to watch the movie.
The programe takes the input of the number of audience willing to watch the movie ,then takes the name and the age of all the audience.
The age of the audience is then put into a for loop which checks if they are 18+ to watch the movie . If the audience is not above 18 the audience name
will not
be printed in the final list of audience who are eligible.
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
print("list of audience who are eligible to watch the movie:")
print('')
print(list_of_audiencename_eligible)#printing the list of audience eligible to watch the movie 













        
    
        
        
    

    







            
