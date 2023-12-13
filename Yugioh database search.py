#December 5 2023
#Rhodri Williams
#Title - Yugioh database searching tool
#Description - a console based program that allows the user to iterate through the Yugioh Database for cards they are looking for. 

import csv
from Functions import csv_to_list, cardtype_tolist, write_to_file


def main():
    # Title message
    print("\nWelcome to the Yugioh card searcher")

    search_result = []
    card_list = csv_to_list("Yugi_db_cleaned.csv")  #Makes list to be easy to read

    main_menu = False
    while main_menu == False:   # MAIN MENU
        print("\nWELCOME to the MAIN MENU:\nChoose an option below:")
        print("1: Search by name")
        print("2: Search by card set")
        print("3: Sort by card type")
        user_choice = input("Enter your choice (1-3): ").lower()  #Lowered for if statements

        if user_choice == "1":
            # Implement card search functionality
            search_state = True
            while search_state == True:   # FIRST QUESTION
                search_result.clear()
                searchee = input("Enter the card name:")   #Must be cap sensitive and can be any card name

                rolling_counter = 0
                for card in card_list:
                    
                    if searchee in card[1]:
                        rolling_counter += 1
                        print(f"{rolling_counter}: {card[1]}")
                        search_result.append(card[1:])    #Skips past the first value of each item being the card set, because we dont need it
                
                
                user_decision_check = False

                while user_decision_check == False:    # Loop to not go through until the user gives valid variable
                    user_continue = input("Did you find what you were looking for? y/n: ").lower() #Lower for if statement
                
                    if user_continue == "y" and len(search_result) > 0:   

                        
                        if len(search_result) == 1:   #User convenience to not have to select the card they have as number 1
                        
                            print("\nOk, here are the details:\n")
                            print("Card name: ", search_result[0][0])
                            print("Card type: ",search_result[0][1])
                            if search_result[0][1] == "Monster":   #Prints all required details for monster card and specifies stats based off of the type of monsters

                                print("Card attribute: ",search_result[0][2])
                                    
                                print("Monster type: ", search_result[0][3])
                                if "Xyz" in search_result[0][3]:
                                    print("Xyz Rank: ",search_result[0][5] )
                                if "Link" in search_result[0][3]:
                                    print("Link arrows: ",search_result[0][6])
                                else:
                                    print("Monster level: ", search_result[0][4])

                            
                                
                            choose_again = False
                            while choose_again == False:   # Loop to not go through until the user gives valid variable
                                    do_it_again = input("Would you like to search again? y/n: ").lower() #Lower for if statement
                                 
                                    if do_it_again == "y":
                                        print("Lets do it again: ")
                                        choose_again = True
                                        user_decision_check = True    #Sets the loops to make sure they will go through again when prompted
                                        search_state = True
            
                                    if do_it_again == "n":
                                        user_decision_check = True
                                        choose_again = True        # Makes sure none of the loops will go through
                                        search_state = False
                                       
                                    
                                  
                                    if do_it_again != "y" and do_it_again != "n":     # Error handling sparkle sparkle
                                        print("Invalid response, please try again:\n")
                         

                        if len(search_result) > 1:   # Specifially if there is more than one search result
                            card_search_choice_loop = True  # Set to True to enter the loop
                            while card_search_choice_loop: # Loop to not go through until the user gives valid variable
                                card_search_choice = input("Which number corresponds to your card?: ")   #String input because easier to work with technically

                                # Check if the input is a valid integer
                                if card_search_choice.isdigit():      #Checks to see if string is a digit, in which it makes it into an integer
                                    card_search_choice = int(card_search_choice)

                                    # Check if the input is greater than 0
                                    if card_search_choice > 0:
                                        card_search_choice_loop = False  # Exit the loop since a valid input is provided
                                        print("\nOk, here are the details:\n")
                                        print("Card name: ", search_result[card_search_choice - 1][0])
                                        print("Card type: ", search_result[card_search_choice - 1][1])

                                        if search_result[card_search_choice - 1][1] == "Monster":    #Will only print extra details if it is a monster card
                                            print("Card attribute: ", search_result[card_search_choice - 1][2])
                                            print("Monster type: ", search_result[card_search_choice - 1][3])
                                            user_decision_check = True

                                            if "Xyz" in search_result[0][3]:
                                                print("Xyz Rank: ", search_result[card_search_choice - 1][5])

                                            if "Link" in search_result[0][3]:
                                                print("Link arrows: ", search_result[card_search_choice - 1][6])
                                            else:
                                                print("Monster level: ", search_result[card_search_choice - 1][4])

                                        

                                        choose_again = False
                                        while choose_again == False:   # Loop to not go through until the user gives valid variable
                                            do_it_again = input("Would you like to search again? y/n: ").lower() #Lower for if statement
                                              
                                            if do_it_again == "y":
                                                print("Lets do it again: ")   #Does as it says
                                                choose_again = True
                                               
                                            if do_it_again == "n":
                                                user_decision_check = True
                                                choose_again = True    #Back to main menu we go
                                                search_state = False
                                              
                                            else:
                                                print("Invalid response, please try again:\n")   #Error handling, more sparkles

                                    if card_search_choice == 0:
                                        print("The value has to be higher than 0. Try again.")   #If Delano is trying some funny business to try and call index position -1, this will surely stop him
                                else:
                                    print("Invalid input. Please enter a valid number.")   #Error handling again
                    if user_continue == "n":     
                        search_again = False   #User did not find their card in the search results
                        while search_again == False: # Loop to not go through until the user gives valid variable
                            try_again = input("Did you want to search again? (Names are caps sensitive) y/n: ").lower() #Lower for if statements
                           
                            if try_again == "y":
                                user_decision_check = True   #Runs through loops again
                                search_again = True
                               
                            if try_again == "n":
                                user_decision_check = True   #Doesn't run through loops again
                                search_again = True
                            
                                search_state = False
                            if user_decision_check == False: 
                                print("Invalid response1, please try again:\n")   #Error handling
                    if user_continue != "y" and user_continue != "n":
                        
                        print("Invalid response, please try again:\n")   #More error handling
                        
        if user_choice == "2":
           
            search_set_loop = False
            while search_set_loop == False: # Loop to not go through until the user gives valid variable
                search_set = input("Would you like to search for a set or list all available sets? (1 or 2, respectively:)")
                if search_set == "1":
                    user_set_search = input("Ok, please enter the name of a set, remember capital letters matter: ")
                    rolling_counter = 0
                    search_result.clear()
                    for card in card_list:   #Adds all cards in set to search result
                    
                        if user_set_search in card[0]:
                            rolling_counter += 1
                            print(f"{rolling_counter}: {card[1]}")
                            search_result.append(card)
                            
                    write_to_fileone_loop = False
                    while write_to_fileone_loop == False and len(search_result) > 0: # Loop to not go through until the user gives valid variable, also makes sure it wont be writing NOTHING to a file
                        write_to_fileone = input("Would you like to write this data to file?: (y/n): ").lower()  #Lower for if statement
                        if write_to_fileone == "y":
                            user_filename = input("Enter the file name: ")

                            did_I_dowell = write_to_file(search_result,user_filename)   #Calls function to write to file
                            print(did_I_dowell)
                            write_to_fileone_loop = True



                        if write_to_fileone == "n":
                            write_to_fileone_loop = True   #Exits
                        if write_to_fileone != "y" and write_to_fileone != "n":
                            print("Invalid response, please try again\n")   #Error handling

                    if len(search_result) == 0:
                        print("No card set found")
                    search_set_again_loop = False
                    while search_set_again_loop == False:
                        search_set_again = input("Would you like to search again? y/n: ").lower() #Lower for if statements
                        if search_set_again == "y":
                            search_set_again_loop = True
                        if search_set_again == "n":
                            search_set_again_loop = True
                            search_set_loop = True
                        if search_set_again != "y" and search_set_again != "n":
                            print("Invalid response, please try again: ")

                        




                    

                if search_set == "2":
                    search_result.clear()
                    for item in card_list:
                        if item[0] not in search_result:
                            search_result.append(item[0])
                    for set in search_result:
                        print(set)     #Lists off all the available sets to choose from
                  
                if search_set != "1" and search_set != "2":
                    print("Invalid response, please try again:\n")
                
        if user_choice == "3":
            sort_card_loop = False
            while sort_card_loop == False: # Loop to not go through until the user gives valid variable
                search_result.clear()
                sort_card = input("What would you like to sort by? (Monster, Spell, Trap:)").lower()   #Lower for if statements, will call function to sort through a list and save to file
                if sort_card == "monster":
                    search_result = cardtype_tolist(card_list,"Monster")
                    sort_card_loop = True
                if sort_card == "spell":
                    search_result = cardtype_tolist(card_list,"Spell")
                    sort_card_loop = True
                if sort_card == "trap":
                    search_result = cardtype_tolist(card_list,"Trap")
                    sort_card_loop = True
                if sort_card_loop == False:
                    print("Invalid response, please try again:\n")
                    sort_card_loop = False
                write_to_fileone_loop = False
                while write_to_fileone_loop == False and len(search_result) > 0:   #Saves data to file
                    write_to_fileone = input("Would you like to write this data to file?: (y/n): ").lower() #Lower for if statements
                    if write_to_fileone == "y":
                        user_filename = input("Enter the file name: ")

                        did_I_dowell = write_to_file(search_result,user_filename)
                        print(did_I_dowell)
                        write_to_fileone_loop = True



                    if write_to_fileone == "n":
                        write_to_fileone_loop = True
                    if write_to_fileone != "y" and write_to_fileone != "n":
                        print("Invalid response, please try again\n")   #Error handling

                sortit_again_loop = False
                while sortit_again_loop == False and len(search_result) > 0: # Loop to not go through until the user gives valid variable and make sure the search result list is clear
                    sortit_again = input("Would you like to sort through the list again? (y/n): ").lower() #If statements

                    if sortit_again == "y":
                        sortit_again_loop = True
                        sort_card_loop = False          #Either continues, exits to main menu, or error.
                    if sortit_again == "n":
                        sortit_again_loop = True
                    if sortit_again_loop == False:
                        print("Invalid response, please try againL\n") #Error handling

        if user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "done":   #Gives the user an error if the correct option isnt selected
            print("Invalid choice. Please enter a valid response.")

        if user_choice == "done":   #Exits program
            main_menu = True
    
if __name__ == "__main__":
    main()




    




