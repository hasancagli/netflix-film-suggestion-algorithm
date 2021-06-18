import numpy as np
import pandas as pd
from imdbData import returnImdbList
import random

imdbScoresList = returnImdbList()
#print(imdbScoresList[0])

dataset = pd.read_csv('netflix_titles.csv')
dataset['imdb_scores'] = imdbScoresList

#print(dataset.head())

# Deleting if imdbScore is 0
print(len(dataset)) # Old value is 7787
dataset = dataset[dataset.imdb_scores != 0]
print(len(dataset)) # New value is 7384

print("***************** Welcome To The Recommendation Program *****************")

# Getting The Type
typeMovie = ""
while(typeMovie != "Movie" and typeMovie != "TV Series" and  typeMovie != "TV Show"): 
    typeMovie = input("Which Type Do You Want To Watch (TV Series, Movie, TV Show) : ")

# Getting The Minimum Imdb
imdb = str(input("Do you have any Minimum Imdb Score to List : (if not write 'no') : "))
if (imdb != 'no'):
    while(type(imdb) is not float):
        try: 
            imdb = float(imdb)
        except: 
            imdb = input("Please Write Your Minimum Imdb Score To List (1 to 10) : ")

# Getting Movie Types 
differentMovieTypes = "Some Types : \n1.Drama\n2.Horror\n3.Comedies\n4.Romantic\n5.Documentaries\n6.Sci-Fi\n7.Action\n8.Crime"
print(differentMovieTypes)
movieTypes = input("Please Enter The Movie Type Numbers That You Want To Watch (i.g : 1,4,5,7) : ")

listSplit = movieTypes.split(',')

movieTypesWithNames = []
for i in range(len(listSplit)):
    element = listSplit[i]
    if (element == '1'):
        movieTypesWithNames.append('Drama')
    elif(element == '2'):
        movieTypesWithNames.append('Horror')
    elif(element == '3'):
        movieTypesWithNames.append('Comedies')
    elif(element == '4'):
        movieTypesWithNames.append('Romantic')
    elif(element == '5'):
        movieTypesWithNames.append('Documentaries')
    elif(element == '6'):
        movieTypesWithNames.append('Sci-Fi')
    elif(element == '7'):
        movieTypesWithNames.append('Action')
    elif(element == '8'):
        movieTypesWithNames.append('Crime')

counter = 1
if (len(movieTypesWithNames) > 0) :
    
    if (imdb != 'no'):
        dataset = dataset[dataset.imdb_scores >= imdb]

    
    dataset= dataset[dataset.type == typeMovie]

    print('********************** Your Film/TV Series/TV Show Recommendations **********************')
    dataset_array = dataset.to_numpy()

    #print("Dataset Array Length : " , len(dataset_array))
    if (len(dataset_array) < 1) :
        print('Not Enough Data. Please Try Again With Different Choices.')
    else : 
        choosens = []
        for x in range(len(dataset_array)):
            """
            dataset_array_list = dataset.to_numpy()
            typeCheck = False
            for i in range(len(movieTypesWithNames)):
                element = movieTypesWithNames[i]
                for x in range(len(dataset_array_list)):

                    if (element in dataset_array_list[x][10]):
                        print(element)
                        print(dataset_array_list[x][10])
                        typeCheck = True

            """
            for i in range(len(movieTypesWithNames)):
                element = movieTypesWithNames[i]
                if (element in dataset_array[x][10]):
                    print('Movie ' + str(counter) + "\n" + "Name : "+ str(dataset_array[x][2]) + 
                    "\nType : " + str(dataset_array[x][1]) +
                    "\nImdb Score : " + str(dataset_array[x][12]) +
                    "\nRelease Year : "+ str(dataset_array[x][7]) +
                    "\nDuration : " + str(dataset_array[x][9]) +
                    "\nListed In : " + str(dataset_array[x][10]) + 
                    "\n*******************************\n")
                    counter += 1
                    break

else : 
    print('An error occured ...')