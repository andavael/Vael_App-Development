from datetime import datetime, timedelta

local_destinations = {
    "Boracay": {"Available dates": [], "Available slots": 50, "Tour expenditure": 5500},
    "El Nido Palawan": {"Available dates": [], "Available slots": 50, "Tour expenditure": 4500},
    "Baguio City": {"Available dates": [], "Available slots": 50, "Tour expenditure": 3900},
}

foreign_destinations = {
    "Hong Kong City": {"Available dates": [], "Available slots": 25, "Tour expenditure" : 5700},
    "Bangkok Thailand": {"Available dates": [], "Available slots": 25, "Tour expenditure" : 5200},
    "Bali Indonesia": {"Available dates": [], "Available slots":  25, "Tour expenditure" : 4500},
}

feedback = {
    "Ease of Booking": [],
    "Destination": [],
    "Accommodation": [],
    "Overall Tour Experience": []
}

users = {}
booked_tours = {}
user_wallet = 0
tg_username = "summer_guide"
tg_password = "ADTG"

def generate_dates(start_date, end_date):
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)
    return dates

start_date = datetime(2024, 4, 1)
end_date = datetime(2024, 5, 31)

for destination in local_destinations.values():
    destination["Available dates"] = generate_dates(start_date, end_date)

for destination in foreign_destinations.values():
    destination["Available dates"] = generate_dates(start_date, end_date)

def create_acc():  
    global username
    print("_" * 100, "\n")
    print("CREATE AN AD SUMMER ACCOUNT \n")

    while True:
        try:
            username = input("\tPlease enter a username (or leave blank to exit): ")
            if not username:
                print("\n\tExiting...\n")
                exit()
            elif username in users:
                print ("\n> Username already exists. Please enter a new one.\n")
                continue
            else:
                password = input("\tEnter a password: ")
                if len(password) < 8:
                    print("\n> Password must be at least 8 characters long.\n")
                    continue
                else:
                    confirm_password = input("\tConfirm Password: ")
                    if password != confirm_password:
                        print("\n> Passwords do not match. Try Again\n")
                        continue
                    else:
                        users[username] = {"password": password,  "user_wallet": user_wallet}
                        print("\nRegistration Successful!\n")
                        print(f'> Your username is {username} and your Password is {password}.')
                        print("_" * 100)
                        return main()
        except ValueError as e:
            print("\n\t >> ", e)
            return main()

def sign_in():
    print("_" * 100, "\n")
    print("LOG IN TO YOUR AD SUMMER ACCOUNT \n")

    while True:
        try:
            username = input("\tEnter your username (or leave bank to exit): ")
            if not username:
                print("\n\tExiting...\n")
                exit()
            elif username.lower() not in users:
                print("\n> Username does not exist. Please try again.\n")
                continue
            else:
                password = str(input("\tEnter your password: "))
                if users.get(username.lower())["password"] == password:
                    print("\nYou have successfully signed in to  AD Summer Guides!")
                    return user_menu(username)
                else:
                    print("\n> Invalid sign-in information. Please Try again.\n")
                    continue
        except ValueError as e:
            print("\n\t >> ", e)
            return main()

def tour_login():
    print("_" * 100, "\n")
    print("LOG IN AS A TOUR-GUIDE \n")

    while True:
        try:
            tg_user = input("\tEnter your tour guide username (or leave bank to exit): ")
            if not tg_user:
                print("\n\tExiting...\n")
                exit()
            elif tg_user != tg_username:
                print("\n> Invalid tour guide username. Please try again. \n")
                continue
            else:
                tg_pass = input("\tEnter your tour guide password: ")
                if tg_pass == tg_password:
                    print("\n You have succesfull signed in as an AS Summer tour guide.")
                    return admin_menu(tg_username)
        except ValueError as e:
            print("\n\t >> ", e)
            return main()

def available_tours():
    print("_" * 100, "\n")
    print("AVAILABLE TOURS FOR SUMMER 2024")
    print("> AD Summer Guides offers a wide variety of tours in different places from around the world!\n")
    print("\t 1. Local Destination Tours")
    print("\t 2. Foreign Destination Tours")
    print("\t 3. Exit ")
    while True:
        try:
            list_choice = int(input("\n> Enter the corresponding number of the list you wish to view: "))
            if list_choice == 1:
                print("\nAVAILABLE TOURS FOR LOCAL DESTINATIONS\n")
                for i, (destination, details) in enumerate(local_destinations.items(), start=1):
                    print(f"\t{i}. Destination: {destination}")
                    print(f"\t   Available dates: April 1 - May 31")
                    print(f"\t   Available slots: {details['Available slots']}")
                    print(f"\t   Tour Expenditure: Php. {details['Tour expenditure']}\n")
                try:
                    choice = input("> Would you like to proceed with another transaction? (YES/NO): ")
                    if choice.lower() == "yes":
                        return user_menu(username)
                    elif choice.lower() == "no":
                        print("\nHave A Wonderful Summer Experience. Goodbye!")
                        print("Exiting...\n")
                        exit()
                    else: 
                        print("\nInvalid input. Please try again.")
                        return available_tours()
                except ValueError as e:
                    print("\n\t >> ", e)
                    return user_menu(username)
            elif list_choice == 2:
                print("\nAVAILABLE TOURS FOR FOREIGN DESTINATIONS\n")
                for i, (destination, details) in enumerate(foreign_destinations.items(), start=1):
                    print(f"\t{i}. Destination: {destination}")
                    print(f"\t   Available dates: April 1 - May 31")
                    print(f"\t   Available slots: {details['Available slots']}")
                    print(f"\t   Tour Expenditure: Php. {details['Tour expenditure']}\n")
                try:
                    choice = input("\n> Would you like to proceed with another transaction? (YES/NO): ")
                    if choice.lower() == "yes":
                        return user_menu(username)
                    elif choice.lower() == "no":
                        print("\nHave A Wonderful Summer Experience. Goodbye!")
                        print("Exiting...\n")
                        exit()
                    else: 
                        print("\nInvalid input. Please try again.")
                        return available_tours()
                except ValueError as e:
                    print("\n\t >> ", e)
                    return user_menu(username)
            elif list_choice == 3:
                print("\nHave A Wonderful Summer Experience. Goodbye!")
                print("Exiting...\n")
                exit()
            else:
                print("\nInvalid input. Please try again.")
                print("_" * 100)
                return available_tours()
        except ValueError as e:
            print("\n\t >> ", e)

def tour_calc():
    print("_" * 100, "\n")
    print("\t SPECIAL PROMOTION:")
    print(f"\t> Children aged 0-12 years old receive a 25% discount on every tour slot.\n")
    print("_" * 100, "\n")
    print("CALCULATE YOUR TOUR EXPENSES FOR SUMMER 2024\n")
    print("\t 1. Local Destination Tours")
    print("\t 2. Foreign Destination Tours")
    print("\t 3. Exit ")

    while True:
        try:
            list_choice = int(input("\nPlease enter the corresponding number of the list you wish to view: "))
            if list_choice == 1:
                while True:
                    print("\nAVAILABLE TOURS FOR LOCAL DESTINATIONS\n")
                    for i, (destination, details) in enumerate(local_destinations.items(), start=1):
                        print(f"\t{i}. Destination: {destination}")
                        print(f"\t     Available slots: {details['Available slots']}")
                        print(f"\t     Tour Expenditure: Php. {details['Tour expenditure']}\n")
                    try:
                        des_choice = str(input("\n\tEnter your desired destination: ")).strip().title()
                        if des_choice in local_destinations:
                            adult_slot = int(input("\tEnter the number of ADULT slots you want to avail: "))
                            child_slot = int(input("\tEnter the number of CHILD slots you want to avail: ")) 
                            total_slots = adult_slot + child_slot
                            if local_destinations[des_choice]['Available slots'] >= total_slots:
                                adult_cost = adult_slot * local_destinations[des_choice]['Tour expenditure']
                                child_cost = child_slot * local_destinations[des_choice]['Tour expenditure'] * 0.75
                                total_cost = adult_cost + child_cost
                                print("\n","*" * 100, "\n")
                                print(f"\tTOUR EXPENDITURE IN {des_choice}\n")
                                print(f"\t\t> CHILD TOUR QTY                          :   {child_slot}")
                                print(f"\t\t> CHILD TOUR EXPENSES                     :   {child_cost}")
                                print(f"\t\t> ADULT TOUR QTY                          :   {adult_slot}")
                                print(f"\t\t> ADULT TOUR EXPENSES                     :   {adult_cost}")
                                print(f"\n\tTOTAL EXPENDITURE FOR {des_choice} TOUR     :   {total_cost}\n")
                                print("*" * 100, "\n")
                                print("To book a tour, please recharge according to the computed expenses.")
                                try:
                                    choice= str(input("> Would you like to proceed with the recharge? (YES/NO): "))
                                    if choice.lower() == "yes":
                                        return recharge_account()
                                    elif choice.lower() == "no":
                                        return user_menu(username)
                                    else:
                                        print("\nInvalid Input. Please try again.")
                                        continue
                                except ValueError as e:
                                    print("\n\t >> ", e)
                                    return user_menu(username)
                            else:
                                print("\n> Not enough slots available for your desired tour. Choose another destination or leave blank to exit")
                                return tour_calc()
                        else:
                            print("\n> Tour for the chosen destination does not exist. Enter a valid input from the list.")
                            continue
                    except ValueError as e:
                        print("\n\t >> ", e)
                        return user_menu(username)
            if list_choice == 2:
                while True:
                    print("\nAVAILABLE TOURS FOR FOREIGN DESTINATIONS\n")
                    for i, (destination, details) in enumerate(foreign_destinations.items(), start=1):
                        print(f"\t{i}. Destination: {destination}")
                        print(f"\t     Available slots: {details['Available slots']}")
                        print(f"\t     Tour Expenditure: Php. {details['Tour expenditure']}\n")
                    try:
                        des_choice = str(input("\n\tEnter your desired destination: ")).strip().title()
                        if des_choice in foreign_destinations:
                            adult_slot = int(input("\tEnter the number of ADULT slots you want to avail: "))
                            child_slot = int(input("\tEnter the number of CHILD slots you want to avail: ")) 
                            total_slots = adult_slot + child_slot
                            if foreign_destinations[des_choice]['Available slots'] >= total_slots:
                                adult_cost = adult_slot * foreign_destinations[des_choice]['Tour expenditure']
                                child_cost = child_slot * foreign_destinations[des_choice]['Tour expenditure'] * 0.75
                                total_cost = adult_cost + child_cost
                                print("\n","*" * 100, "\n")
                                print(f"\tTOUR EXPENDITURE IN {des_choice}\n")
                                print(f"\t\t> CHILD TOUR QTY                          :   {child_slot}")
                                print(f"\t\t> CHILD TOUR EXPENSES                     :   {child_cost}")
                                print(f"\t\t> ADULT TOUR QTY                          :   {adult_slot}")
                                print(f"\t\t> ADULT TOUR EXPENSES                     :   {adult_cost}")
                                print(f"\n\tTOTAL EXPENDITURE FOR {des_choice} TOUR     :   {total_cost}\n")
                                print("*" * 100, "\n")
                                print("To book a tour, please recharge according to the computed expenses.")
                                try:
                                    choice= str(input("> Would you like to proceed with the recharge? (YES/NO): "))
                                    if choice.lower() == "yes":
                                        return recharge_account()
                                    elif choice.lower() == "no":
                                        return user_menu(username)
                                    else:
                                        print("\nInvalid Input. Please try again.")
                                        continue
                                except ValueError as e:
                                    print("\n\t >> ", e)
                                    return user_menu(username)
                            else:
                                print("\n> Not enough slots available for your desired tour. Choose another destination or leave blank to exit")
                                return tour_calc()
                        else:
                            print("\n> Tour for the chosen destination does not exist. Enter a valid input from the list.")
                            continue
                    except ValueError as e:
                        print("\n\t >> ", e)
                        return user_menu(username)
            elif choice == 3:
                print("\nHave A Wonderful Summer Experience. Goodbye!")
                print("Exiting...\n")
                exit()
            else:
                print("Invalid input. Enter a valid integer from the list.")
                return tour_calc()
        except ValueError as e:
            print("\n\t >> ", e)
            return user_menu(username)

def recharge_account():
    global username
    user_recharge = 0

    print("_" * 100, "\n")
    print("RECHARGE ACCOUNT\n")

    while True:
        try:
            print(f"\tBALANCE : {users[username]['user_wallet']}\n")
            user_recharge = int(input("\n\tEnter the amount you'd like to add in your account: Php "))
            users[username]['user_wallet'] += user_recharge
            print(f"\t> You have successfully recharged an amount of Php. {user_recharge}!") 
            print(f"\n\tUPDATED BALANCE: Php {users[username]['user_wallet']} \n")
        except ValueError as e:
            print("\n\t >> ", e)
            return user_menu(username)
        except KeyError:
            print("\nUsername not found. Please try again.")
            return user_menu(username)
        
        while True:
            choice = input("> Would you like to proceed? (YES/NO): ")
            if choice.lower() == "yes":
                return user_menu(username)
            elif choice.lower() == "no":
                print("\nHave A Wonderful Summer Experience. Goodbye!")
                return
            else:
                print("\nInvalid input. Please enter 'YES' or 'NO'.")
        
def book_tour():
    global booked_tours
    print("_" * 100, "\n")
    print("BOOK A TOUR FOR SUMMER 2024\n")
    print("\t 1. Local Destination Tours")
    print("\t 2. Foreign Destination Tours")

    while True:
        try:
            list_choice = int(input("\nPlease enter the corresponding number of the list you wish to view: "))
            if list_choice == 1:
                while True:
                    print("\nAVAILABLE TOURS FOR LOCAL DESTINATIONS\n")
                    for i, (destination, details) in enumerate(local_destinations.items(), start=1):
                        print(f"\t{i}. Destination: {destination}")
                        print(f"\t     Available dates: April 1 - May 31")
                        print(f"\t     Available slots: {details['Available slots']}")
                        print(f"\t     Tour Expenditure: Php. {details['Tour expenditure']}\n")
                    try:
                        des_choice = str(input("\n\tEnter the name of the destination you wish to be tour-guided with: ")).strip().title()
                        if des_choice in local_destinations:
                            if local_destinations[des_choice]['Available slots'] > 0:
                                adult_slots = int(input("\tEnter the number of ADULT slots you want to avail: "))
                                child_slots = int(input("\tEnter the number of CHILD slots you want to avail: "))
                                total_slots = adult_slots + child_slots
                                if total_slots <= local_destinations[des_choice]['Available slots']:
                                    date_choice = input("\tEnter your date choice (YYYY-MM-DD): ")
                                    if date_choice in local_destinations[des_choice]['Available dates']:
                                        total_expenditure = (adult_slots * local_destinations[des_choice]['Tour expenditure']) + (child_slots * (local_destinations[des_choice]['Tour expenditure'] * 0.75))
                                        if users[username]['user_wallet'] >= total_expenditure:
                                            local_destinations[des_choice]['Available slots'] -= total_slots
                                            users[username]['user_wallet'] -= total_expenditure
                                            booked_tours.setdefault(des_choice, {}).setdefault(date_choice, []).append({'guest': username, 'slots': total_slots})
                                            local_destinations[des_choice]['Available dates'].remove(date_choice)
                                            print(f"\nYou have successfully booked {adult_slots} adult slot(s) and {child_slots} child slot(s) for a tour in {des_choice} on {date_choice} for Php. {total_expenditure}.")
                                            print(f"> You now have a total of Php. {users[username]['user_wallet']} in your account.\n")
                                            print("_" * 100, "\n")
                                            print_choice = str(input("\n> Do you wish to receive a printed copy of your booked tour? (YES/NO): "))
                                            if print_choice.lower() == "yes":
                                                print("\n","*" * 100, "\n")
                                                print(f"\tTHANK YOU FOR BOOKING WITH AD SUMMER GUIDES!\n\n")
                                                print(f"\t\t> GUEST                   :   {username}")
                                                print(f"\t\t> TOUR DESTNATION         :   {des_choice}")
                                                print(f"\t\t> TOUR DATE               :   {date_choice}")
                                                print(f"\t\t> TOTAL SLOTS BOOKED      :   {total_slots}")
                                                print(f"\t\t> TOTAL EXPENDITURE       :   {total_expenditure}\n")
                                                print(f"\n\tENJOY YOUR SUMMER TOUR IN {des_choice}\n")
                                                print("*" * 100, "\n")
                                                return_choice = input("> Would you like to return to the user menu? (YES/NO): ")
                                                if return_choice.lower() == "yes":
                                                    return user_menu(username)
                                                elif return_choice.lower() == "no":
                                                    print("\nHave A Wonderful Summer Experience. Goodbye!")
                                                    print("Exiting...\n")
                                                    exit()
                                                else:
                                                    print("\nInvalid Input. Please try again.")
                                                    continue
                                            elif print_choice.lower() == "no":
                                                print("\nThank you for booking with us. Have a blast this summer 2024!\n")
                                                return user_menu(username)
                                            else:
                                                print("\nInvalid Input. Please try again.")
                                                continue
                                        else:
                                            print("\n> You do not have enough balance in your account. Please recharge your account on the user menu.")
                                            user_menu(username)
                                            return
                                    else:
                                        print("\n> Your desired tour is not available on the date you chose. Please book another date.")
                                        continue
                                else:
                                    print("\n> Not enough slots available for your desired tour.")
                                    continue
                            else:
                                print(f"\n> There are no available slots for a tour in {des_choice}.")
                                slot_choice = str(input("Would you like to choose another destination? (YES/NO):  "))
                                if slot_choice.lower() == "yes":
                                    return book_tour()
                                elif slot_choice.lower() == "no":
                                    print("\nHave A Wonderful Summer Experience. Goodbye!")
                                    return
                                else:
                                    print("\nInvalid input. Please try again.")
                                    return book_tour()
                        else:
                            print("\n> Tour for the chosen destination does not exist. Enter a valid input from the list.")
                            continue
                    except ValueError as e:
                        print("\n\t >> ", e)
                        return book_tour()
            elif list_choice == 2:
                while True:
                    print("\nAVAILABLE TOURS FOR FOREIGN DESTINATIONS\n")
                    for i, (destination, details) in enumerate(foreign_destinations.items(), start=1):
                        print(f"\t{i}. Destination: {destination}")
                        print(f"\t     Available dates: April 1 - May 31")
                        print(f"\t     Available slots: {details['Available slots']}")
                        print(f"\t     Tour Expenditure: Php. {details['Tour expenditure']}\n")
                    try:
                        des_choice = str(input("\n\tEnter the name of the destination you wish to be tour-guided with: ")).strip().title()
                        if des_choice in foreign_destinations:
                            if foreign_destinations[des_choice]['Available slots'] > 0:
                                adult_slots = int(input("\tEnter the number of ADULT slots you want to avail: "))
                                child_slots = int(input("\tEnter the number of CHILD slots you want to avail: "))
                                total_slots = adult_slots + child_slots
                                if total_slots <= foreign_destinations[des_choice]['Available slots']:
                                    date_choice = input("\tEnter your date choice (YYYY-MM-DD): ")
                                    if date_choice in foreign_destinations[des_choice]['Available dates']:
                                        total_expenditure = (adult_slots * foreign_destinations[des_choice]['Tour expenditure']) + (child_slots * (foreign_destinations[des_choice]['Tour expenditure'] * 0.75))
                                        if users[username]['user_wallet'] >= total_expenditure:
                                            foreign_destinations[des_choice]['Available slots'] -= total_slots
                                            users[username]['user_wallet'] -= total_expenditure
                                            booked_tours.setdefault(des_choice, {}).setdefault(date_choice, []).append({'guest': username, 'slots': total_slots})
                                            foreign_destinations[des_choice]['Available dates'].remove(date_choice)
                                            print(f"\nYou have successfully booked {adult_slots} adult slot(s) and {child_slots} child slot(s) for a tour in {des_choice} on {date_choice} for Php. {total_expenditure}.")
                                            print(f"> You now have a total of Php. {users[username]['user_wallet']} in your account.\n")
                                            print_choice = str(input("\n> Do you wish to receive a printed copy of your booked tour? (YES/NO): "))
                                            if print_choice.lower() == "yes":
                                                print("\n","*" * 100, "\n")
                                                print(f"\tTHANK YOU FOR BOOKING WITH AD SUMMER GUIDES!\n\n")
                                                print(f"\t\t> GUEST                   :   {username}")
                                                print(f"\t\t> TOUR DESTNATION         :   {des_choice}")
                                                print(f"\t\t> TOUR DATE               :   {date_choice}")
                                                print(f"\t\t> TOTAL SLOTS BOOKED      :   {total_slots}")
                                                print(f"\t\t> TOTAL EXPENDITURE       :   {total_expenditure}\n")
                                                print(f"\n\tENJOY YOUR SUMMER TOUR IN {des_choice}\n")
                                                print("*" * 100, "\n")
                                                return_choice = input("> Would you like to return to the user menu? (YES/NO): ")
                                                if return_choice.lower() == "yes":
                                                    return user_menu(username)
                                                elif return_choice.lower() == "no":
                                                    print("\nHave A Wonderful Summer Experience. Goodbye!")
                                                    print("Exiting...\n")
                                                    exit()
                                                else:
                                                    print("\nInvalid Input. Please try again.")
                                                    continue
                                            elif print_choice.lower() == "no":
                                                print("\nThank you for booking with us. Have a blast this summer 2024!\n")
                                                return user_menu(username)
                                            else:
                                                print("\nInvalid Input. Please try again.")
                                                continue
                                        else:
                                            print("\n> You do not have enough balance in your account. Please recharge your account on the user menu.")
                                            user_menu(username)
                                            return
                                    else:
                                        print("\n> Your desired tour is not available on the date you chose. Please book another date.")
                                        continue
                                else:
                                    print("\n> Not enough slots available for your desired tour.")
                                    continue
                            else:
                                print(f"\n> There are no available slots for a tour in {des_choice}.")
                                slot_choice = str(input("Would you like to choose another destination? (YES/NO):  "))
                                if slot_choice.lower() == "yes":
                                    return book_tour()
                                elif slot_choice.lower() == "no":
                                    print("\nHave A Wonderful Summer Experience. Goodbye!")
                                    return
                                else:
                                    print("\nInvalid input. Please try again.")
                                    return book_tour()
                        else:
                            print("\n> Tour for the chosen destination does not exist. Enter a valid input from the list.")
                            continue
                    except ValueError as e:
                        print("\n\t >> ", e)
                        return book_tour()
            else:
                print("\nInvalid input. Please enter '1' for Local Destination Tours or '2' for Foreign Destination Tours.")
                continue
        except ValueError as e:
            print("\n\t >> ", e)
            return user_menu(username)
        
def send_feedback():
    factors = ["Ease of Booking", "Destination", "Accommodation", "Overall Tour Experience"]

    print("_" * 100)
    print("\nSEND FEEDBACK FOR YOUR TOUR EXPERIENCE\n")

    try:
        user_feedback = {}
        for factor in factors:
            while True:
                try:
                    rating = int(input(f"\tRating for {factor} (1-5): "))
                    if not 1 <= rating <= 5:
                        raise ValueError("\n> Rating must be between 1 and 5.")
                    user_feedback[factor] = rating
                    break
                except ValueError:
                    print("\n> Invalid input. Please enter a number between 1 and 5.")

        feedback[username] = user_feedback

        copy_choice = input("\n> Would you like a copy of your responses? (YES/NO): ")
        if copy_choice.lower() == "yes":
            print("\n","*" * 100, "\n")
            print(f"\tFEEDBACK BY {username.upper()}\n")
            for factor, rating in user_feedback.items():
                print(f"\t\t> {factor.upper()} : {rating}")
            print("\n","*" * 100, "\n")
            return_choice = input("> Would you like to return to the user menu? (YES/NO): ")
            if return_choice.lower() == "yes":
                return user_menu(username)
            elif return_choice.lower() == "no":
                print("\nHave A Wonderful Summer Experience. Goodbye!")
                print("Exiting...\n")
                exit()
            else:
                print("\nInvalid Input. Please try again.")
                return
        elif copy_choice.lower() == "no":
            return feedback
        else:
            print("\nInvalid Input. Please try again.")
            return send_feedback()
    except ValueError as e:
        print("\n[ERROR!] ", e)
        print("_" * 10)
        return send_feedback()
    
def booked_list():
    global booked_tours
    print("_" * 100, "\n")
    print("BOOKED TOURS LIST\n")

    if not booked_tours:
        print("\tNo tours have been booked")
    else:
        for destination, dates in booked_tours.items():
            print(f"\t{destination.upper()}")
            print("\tDATES BOOKED:")
            for date, guests in dates.items():
                print(f"\t> {date}:")
                for booking in guests:
                    print(f"\t  guest: {booking['guest']}, {booking['slots']} slots")
            print("\n")

    while True:
        try:
            return_choice = input("\n> Would you like to return to the admin menu? (YES/NO): ")
            if return_choice.lower() == "yes":
                return admin_menu(tg_username)
            elif return_choice.lower() == "no":
                print("\nHave A Wonderful Summer Experience. Goodbye!")
                print("Exiting...\n")
                exit()
            else:
                print("\nInvalid Input. Please try again.")
                continue 
        except ValueError as e:
            print("\n\t >> ", e)
            return admin_menu(tg_username)

def add_destination():
    print("_" * 100)
    print("\nADD DESTINATIONS IN AD SUMMER GUIDES!")

    while True:
        try:
            destination_type = input("\n\tEnter destination type (local/foreign): ")
            if destination_type.lower() not in ["local", "foreign"]:
                raise ValueError("\n> Invalid destination type. Please enter 'local' or 'foreign'.")

            destination_dict = local_destinations if destination_type.lower() == "local" else foreign_destinations

            destination_name = input("\tEnter destination name: ")
            available_slots = int(input("\tEnter available slots: "))
            tour_expenditure = int(input("\tEnter tour expenditure: "))

            destination_dict[destination_name] = {
                "Available dates": generate_dates(start_date, end_date),
                "Available slots": available_slots,
                "Tour expenditure": tour_expenditure
            }
            
            if destination_type.lower() == "local":
                print("\nUPDATED LIST OF LOCAL DESTINATIONS \n")
                for i, (destination, details) in enumerate(local_destinations.items(), start=1):
                        print(f"\t{i}. Destination: {destination}")
                        print(f"\t     Available dates: April 1 - May 31")
                        print(f"\t     Available slots: {details['Available slots']}")
                        print(f"\t     Tour Expenditure: Php. {details['Tour expenditure']}\n")
            else:
                print("\nUPDATED LIST OF FOREIGN DESTINATIONS:")
                for i, (destination, details) in enumerate(foreign_destinations.items(), start=1):
                        print(f"\t{i}. Destination: {destination}")
                        print(f"\t     Available dates: April 1 - May 31")
                        print(f"\t     Available slots: {details['Available slots']}")
                        print(f"\t     Tour Expenditure: Php. {details['Tour expenditure']}\n")
            try:
                add_choice = input("\n> Would you like to add another destination? (YES/NO): ")
                if add_choice.lower() == "yes":
                    return add_destination()
                elif add_choice.lower() == "no":
                    return modify_list()
                else:
                    print("\nInvalid Input. Please try again.")
                    continue
            except ValueError as e:
                print("\n[ERROR!] ", e)
                print("_" * 10)
                return remove_destination()
        except ValueError as e:
            print("\n[ERROR!] ", e)
            print("_" * 10)
            return modify_list()

def remove_destination():
    print("_" * 100)
    print("\nREMOVE DESTINATIONS IN AD SUMMER GUIDES!")

    while True:
        try:
            destination_type = input("\n\tEnter destination type to remove (local/foreign): ")
            if destination_type.lower() not in ["local", "foreign"]:
                raise ValueError("\n> Invalid destination type. Please enter 'local' or 'foreign'.")

            destination_dict = local_destinations if destination_type.lower() == "local" else foreign_destinations

            destination_name = input("\tEnter destination name to remove (observe proper casing): ")

            if destination_name in destination_dict:
                destination_dict.pop(destination_name)
                print(f"\n> {destination_name} removed successfully from {destination_type} destinations.")
            else:
                print(f"\n> {destination_name} not found in the list of {destination_type} destinations.")
            
            if not destination_dict:
                print("\n> No more destinations on the list.")

            if destination_type.lower() == "local":
                print("\nUPDATED LIST OF LOCAL DESTINATIONS \n")
                for i, (destination, details) in enumerate(local_destinations.items(), start=1):
                    print(f"\t{i}. Destination: {destination}")
                    print(f"\t     Available dates: April 1 - May 31")
                    print(f"\t     Available slots: {details['Available slots']}")
                    print(f"\t     Tour Expenditure: Php. {details['Tour expenditure']}\n")
            else:
                print("\nUPDATED LIST OF FOREIGN DESTINATIONS:")
                for i, (destination, details) in enumerate(foreign_destinations.items(), start=1):
                    print(f"\t{i}. Destination: {destination}")
                    print(f"\t     Available dates: April 1 - May 31")
                    print(f"\t     Available slots: {details['Available slots']}")
                    print(f"\t     Tour Expenditure: Php. {details['Tour expenditure']}\n")    
            try:
                remove_choice = input("\n> Would you like to remove another destination? (YES/NO): ")
                if remove_choice.lower() == "yes":
                    return remove_destination()
                elif remove_choice.lower() == "no":
                    return modify_list()
                else:
                    print("\nInvalid Input. Please try again.")
                    continue
            except ValueError as e:
                print("\n[ERROR!] ", e)
                print("_" * 10)
                return remove_destination()
        except ValueError as e:
            print("\n[ERROR!] ", e)
            print("_" * 10)
            return modify_list()

def view_feedback():
    factors = ["Ease of Booking", "Destination", "Accommodation", "Overall Tour Experience"]

    print("_" * 100)
    print("\nVIEW FEEDBACK AVERAGES\n")

    while True:
        try:
            if not feedback:
                print("\tNo feedbacks yet.")
                return

            factor_totals = {factor: 0 for factor in factors}
            factor_counts = {factor: 0 for factor in factors}

            for user_feedback in feedback.values():
                for factor in factors:
                    if factor in user_feedback:
                        factor_totals[factor] += user_feedback[factor]
                        factor_counts[factor] += 1

            total_users = len(feedback)
            for factor in factors:
                if factor_counts[factor] > 0:
                    average_rating = factor_totals[factor] / factor_counts[factor]
                    print(f"\t> {factor}: {average_rating:.2f}")
                else:
                    print(f"\t> {factor}: No ratings yet.")

            return_choice = input("\n> Would you like to return to the admin menu? (YES/NO): ")
            if return_choice.lower() == "yes":
                return admin_menu(tg_username)
            elif return_choice.lower() == "no":
                print("\nHave A Wonderful Summer Experience. Goodbye!")
                print("Exiting...\n")
                exit()
            else:
                print("\nInvalid Input. Please try again.")
                return view_feedback()
        except ValueError as e:
            print("\n[ERROR!] ", e)
            print("_" * 10)
            return view_feedback()

def modify_list():
    print("_" * 100)
    print("\nMODIFY TOUR DESTINATIONS IN AD SUMMER GUIDES!\n")
    print("\t 1. Add a new destination")
    print("\t 2. Remove existing destination")
    print("\t 3. Return to admin menu")
    try:
        choice = int(input("\n> Please enter the number of your directory selection: "))
        if choice == 1:
            add_destination()
        elif choice ==  2:
            remove_destination()
        elif choice == 3:
            return admin_menu(tg_username)
        else:
            print("\nInvalid input. Please try again.")
            print("_" * 100)
            return modify_list()
    except ValueError as e:
        print("\n[ERROR!] ", e )
        print("_" * 10)
        return admin_menu(tg_username)

def admin_menu(tg_username):
    print("_" * 100)
    print("\nWELCOME TO AD SUMMER GUIDES!")
    print(f"You are logged in as {tg_username}\n")
    print("\t 1. Show list of booked tours")
    print("\t 2. Modify destinations list")
    print("\t 3. View Feedbacks")
    print("\t 4. Log-out")
    try:
        choice = int(input("\n> Please enter the number of your directory selection: "))
        if choice == 1:
            booked_list()
        elif choice ==  2:
            modify_list()
        elif choice ==  3:
            view_feedback()
        elif choice == 4:
            print("_" * 100)
            print(f"\nAre you sure you want to logout as {tg_username}? \n")
            print("\t 1. Log-out and return to main menu.")
            print("\t 2. Log-out and exit.")
            print("\t 3. Cancel.")
            while True:
                choice = input("\n> Enter your choice: ")
                if choice == "1":
                    print(f"\nSuccessfully logged out as {tg_username}.\n")
                    print("_" * 100)
                    return main()
                elif choice == "2":
                    print("\nHave A Wonderful Summer Experience. Goodbye!")
                    print("Exiting...\n")
                    exit()  
                elif choice == "3":
                    print("Log out cancelled.")
                    return admin_menu(tg_username)
                else:
                    print("Invalid choice. Please refer to the list.")
                    continue
        else:
            print("\nInvalid input. Please try again.")
            print("_" * 100)
            return admin_menu(tg_username)
    except ValueError as e:
        print("\n[ERROR!] ", e )
        print("_" * 10)
        return main()

def user_menu(username):
    print("_" * 100)
    print("\nWELCOME TO AD SUMMER GUIDES!")
    print(f"You are logged in as {username}\n")
    print("\t 1. Show Available Tours and Destinations")
    print("\t 2. Complimentary Tour cost calculation")
    print("\t 3. Recharge Account")
    print("\t 4. Book A Tour")
    print("\t 5. Send Feedback")
    print("\t 6. Log-out")

    try:
        choice = int(input("\n> Please enter the number of your directory selection: "))
        if choice == 1:
            available_tours()
        elif choice ==  2:
            tour_calc()
        elif choice == 3:
            recharge_account()
        elif choice == 4:
            book_tour()
        elif choice == 5:
            send_feedback()
        elif choice == 6:
            print("_" * 100)
            print(f"\nAre you sure you want to logout as {username}? \n")
            print("\t 1. Log-out and return to main menu.")
            print("\t 2. Log-out and exit.")
            print("\t 3. Cancel.")
            while True:
                choice = input("\n> Enter your choice: ")
                if choice == "1":
                    print(f"\nSuccessfully logged out as {username}.\n")
                    print("_" * 100)
                    return main()
                elif choice == "2":
                    print("\nHave A Wonderful Summer Experience. Goodbye!")
                    print("Exiting...\n")
                    exit()  
                elif choice == "3":
                    print("Log out cancelled.")
                    return user_menu(username)
                else:
                    print("Invalid choice. Please refer to the list.")
                    continue
        elif choice == 4:
            print("Exiting...")
            exit()
        else:
            print("\nInvalid input. Please try again.")
            print("_" * 100)
            return user_menu(username)
    except ValueError as e: 
        print("\n[ERROR!] ", e )
        print("_" * 10)
        return main()

def main():
    print("\nWELCOME TO AD SUMMER GUIDES!")
    print("We are looking forward to provide you with an exceptional tour guide experience this summer.")
    print("_" * 100, "\n")
    print("\t 1. Create an account")
    print("\t 2. Sign-in")
    print("\t 3. Log-in as Tour Guide")
    print("\t 4. Exit")

    try:
        choice = int(input("\n> Please enter the number of your directory selection: "))
        if choice == 1:
            create_acc()
        elif choice == 2:
            sign_in()
        elif choice == 3:
            tour_login()
        elif choice == 4:
            print("\nHave A Wonderful Summer Experience. Goodbye!")
            print("Exiting...\n")
            exit()
        else:
            print("\nInvalid input. Please try again.")
            print("_" * 100)
            return main()
    except ValueError as e: 
        print("\n[ERROR!] ", e )
        print("_" * 100)
        return main()
main()