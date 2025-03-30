import easygui

combo = {
    'Value':{
        'Beef burger': 5.69,
        'Fries': 1.00,
        'Fizzy drink': 1.00
    },

    'Cheezy':{
        'Cheeseburger': 6.69,
        'Fries': 1.00,
        'Fizzy drink': 1.00
    },

    'Super':{
        'Cheeseburger': 6.69,
        'Large fries': 2.00,
        'Smoothie': 2.00
    }
}

def display_menu():
    if not combo:
        easygui.msgbox("There is no combo in the main menu.\n\nMaybe try to add one.", title = "NOTE")
        return
    
    sentence = ("")
    for items, prices in combo.items():
        sentence += (f"\n({items}):\n")
        for items, prices in prices.items():
            sentence += (f"{items} - ${prices}\n")
    
    easygui.msgbox(sentence, title = "DISPLAY MENU")

def search_combo():
    if not combo:
        easygui.msgbox("There is no combo in the main menu to search.", title = "NOTE")
        return
    
    combo_to_search = easygui.buttonbox("Select a choice below:", title = "SEARCH PAGE", choices = list(combo.keys()))

    if combo_to_search:
        text = (f"\n({combo_to_search}):\n")
        for items, prices in combo[combo_to_search].items():
            text += (f"{items} - ${prices}\n")
    
    easygui.msgbox(text, title = "SEARCH RESULT")



def main():
    while True:
        choice = easygui.buttonbox("Choose an option below to proceed:", title = "MAIN MENU PAGE", choices = ["Display a combo", "Search a combo", "Remove a combo", "Add a combo", "Modify a combo", "[EXIT PROGRAM]"])

        if choice == "Display a combo":
            display_menu()
        elif choice == "Search a combo":
            search_combo()
        elif choice == "Remove a combo":
            pass
        elif choice == "Add a combo":
            pass
        elif choice == "Modify a combo":
            pass
        elif choice == "[EXIT PROGRAM]":
            easygui.msgbox("Thanks for using the program!", title = "GOODBYE")
            break

main()
