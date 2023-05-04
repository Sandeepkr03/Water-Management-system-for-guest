

# Constants
CORPORATION_WATER_COST = 1.0
BOREWELL_WATER_COST = 1.5
Apartment_Water_Consumption = {'2': 900, '3': 1500}

# Global variables
apartment_type = None
corporation_ratio = None
borewell_ratio = None
no_of_guests = 0
total_corporation_water = 0
total_borewell_water = 0
total_water_consumption = 0
without_tanker_bill = 0


def allot_water(apartment_type, ratio):
    global corporation_ratio, borewell_ratio, total_corporation_water, total_borewell_water, total_water_consumption, without_tanker_bill

    corporation_ratio, borewell_ratio = map(int, ratio.split(':'))

    total_water_consumption = Apartment_Water_Consumption[apartment_type]
    
    ratio_factor = total_water_consumption/(corporation_ratio+borewell_ratio)
    
    total_corporation_water = corporation_ratio * ratio_factor
    
    total_borewell_water = borewell_ratio * ratio_factor
    
    without_tanker_bill = (total_corporation_water * CORPORATION_WATER_COST + total_borewell_water * BOREWELL_WATER_COST)


def add_guests(num_guests):
    global no_of_guests

    no_of_guests += num_guests


def calculate_guest_bill(no_of_litres):
    if no_of_litres <= 500:
        return no_of_litres*2
    elif no_of_litres <= 1500:
        return 500*2 + (no_of_litres-500)*3
    elif no_of_litres <= 3000:
        return 500*2 + 1000*3 + (no_of_litres-1500)*5
    else:
        return 500*2 + 1000*3 + 1500*5 + (no_of_litres-3000)*8


def calculate_cost():
    global without_tanker_bill, no_of_guests, total_water_consumption

    water_consumed_guest = (no_of_guests * 10 * 30)
    
    total_water_consumption += water_consumed_guest
    
    total_bill = without_tanker_bill + \
        calculate_guest_bill(water_consumed_guest)
    print(total_water_consumption, round(total_bill))


