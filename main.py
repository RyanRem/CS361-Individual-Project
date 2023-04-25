def bar():
    print("------------------------")
def sendQuery(q):
    print("\nsent query\n")
def general():
    bar()
    print("\n\nYou have selected the Popular Article by General Search\n")
    print("To navigate back to the search modes, press 1\n")
    print("Input any query to get the most popular article related to the search\n")
    print("After inputting a general search, you can decide whether or not to see the detailed article or the simplified article\n")
    genInput = input(":")
    bar()
    if genInput != '1':
        while True:
            detTF = input("\nInput...\n8 to see a detailed version\n9 to see a simplified version\n0 to return to search modes\n")
            if detTF == '8':
                print("\nDetailed version selected\n")
                break
            elif detTF == '9':
                print("\nSimplified version selected\n")
                break
            elif detTF == '0':
                print("\nExiting search mode\n")
                break
            else:
                print("\nInvalid input\n")
    
        
    bar()
def lang():
    bar()
    print("\n\nYou have selected the Popular Article By Language Mode\n")
    print("To navigate back to the search modes, press 1\n")
    print("Input a language to see the most popular article in that language. Ex. Spanish\n")
    print("After inputting a language, you can decide whether or not to see the detailed article or the simplified article\n")
    langPut = input(":")
    bar()
    if langPut != '1':
        while True:
            detTF = input("\nInput...\n8 to see a detailed version\n9 to see a simplified version\n0 to return to search modes\n")
            if detTF == '8':
                print("\nDetailed version selected\n")
                break
            elif detTF == '9':
                print("\nSimplified version selected\n")
                break
            elif detTF == '0':
                print("\nExiting search mode\n")
                break
            else:
                print("\nInvalid input\n")
    
        
    bar()

def country():
    bar()
    print("\n\nYou have selected the Popular Article By Country Mode\n")
    print("To navigate back to the search modes, press 1\n")
    print("Input a country to see the most popular article in that country.  Ex. Germany")
    print("After inputting a country, you can decide whether or not to see the detailed article or the simplified article\n")
    countryInput = input(":")
    bar()
    if countryInput != '1':
        while True:
            detTF = input("\nInput...\n8 to see a detailed version\n9 to see a simplified version\n0 to return to search modes\n")
            if detTF == '8':
                print("\nDetailed version selected\n")
                break
            elif detTF == '9':
                print("\nSimplified version selected\n")
                break
            elif detTF == '0':
                print("\nExiting search mode\n")
                break
            else:
                print("\nInvalid input\n")
    
        
    bar()
        
def category():
    bar()
    print("\n\nYou have selected the Popular Article By Category Mode\n")
    print("To navigate back to the search modes, press 1\n")
    print("Input a category to see the most popular article in that category.  Ex. Science\n")
    print("After inputting a category, you can decide whether or not to see the detailed article or the simplified article\n")
    catInput = input(":")
    bar()
    if catInput != '1':
        while True:
            detTF = input("\nInput...\n8 to see a detailed version\n9 to see a simplified version\n0 to return to search modes\n")
            if detTF == '8':
                print("\nDetailed version selected\n")
                break
            elif detTF == '9':
                print("\nSimplified version selected\n")
                break
            elif detTF == '0':
                print("\nExiting search mode\n")
                break
            else:
                print("\nInvalid input\n")
    
        
    bar()

def publication():
    bar()
    print("\n\nYou have selected the Popular Article By Publication Mode\n")
    print("To navigate back to the search modes, press 1\n")
    print("Input a publication to see the most popular article written by that publication.  Ex. National Geographic\n")
    print("After inputting a publication, you can decide whether or not to see the detailed article or the simplified article\n")
    pubInput = input(":")
    bar()
    if pubInput != '1':
        while True:
            detTF = input("\nInput...\n8 to see a detailed version\n9 to see a simplified version\n0 to return to search modes\n")
            if detTF == '8':
                print("\nDetailed version selected\n")
                break
            elif detTF == '9':
                print("\nSimplified version selected\n")
                break
            elif detTF == '0':
                print("\nExiting search mode\n")
                break
            else:
                print("\nInvalid input\n")
    
        
    bar()




print("Welcome to ArtiSearch!\n")
print("The application that allows you to search for the most popular article based on a custom search!\n ")




while True:
    

    bar()
    print("\n\nBelow are the search modes.  Each search mode will require different input and will explain the process\n")
    print("Search the most popular article by.... ")
    print("1 - Language\n")
    print("2 - Country\n")
    print("3 - Category\n")
    print("4 - Publication\n")
    print("5 - General Search\n")
    print("0 - exit program\n")
    
    userInput = input(":")

    if userInput == '1':
        lang()
    elif userInput == '2':
        country()
    elif userInput == '3':
        category()
    elif userInput == '4':
        publication()
    elif userInput == '5':
        general()
    elif userInput == '0':
        break
    else:
        print("Invalid input, try again\n\n")
    
