import water_management

def main():
    print("*****Water Management System*****")
    ALLOT_WATER  = "ALLOT_WATER"
    ADD_GUESTS  = "ADD_GUESTS"
    BILL = "BILL"
    print("Enter Your Input")
    allotments = input(":").split()
    guests = True
    guests_list = []
    while guests:
        guests_ = input(":")
        if guests_.split()[0] == ADD_GUESTS:
            guests_list.append((guests_).split())
        elif  guests_.split()[0] == BILL:
            guests = False

    water_management.allot_water(allotments[1], allotments[2])
    for guest in guests_list:
        water_management.add_guests(int(guest[1]))
    water_management.calculate_cost()


if __name__=="__main__":
    main()
    



#Enter Your Input in this format:
# ALLOT_WATER 2 3:7
# ADD_GUESTS 2
# ADD_GUESTS 2
# ADD_GUESTS 2
# ADD_GUESTS 3
# BILL = 3600 11215




