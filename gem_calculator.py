import math

def main():
    drop_table = [5,3,2]

    drop_rarity = 0
    for drop in drop_table:
        drop_rarity = drop_rarity + drop

    drop_rates = []
    for drop in drop_table:
        drop_rates.append(drop / drop_rarity)

    gems = ["sapphire","emerald","ruby"]
    xp_rates = [50,67.5,85]

    trip_control = 28
    trip_bag = 127
    trip_control_gems = []
    trip_bag_gems = []

    for drop in drop_rates:
        trip_control_gems.append(trip_control*drop)
        trip_bag_gems.append(trip_bag*drop)

    xp_trip_control = 0.0
    xp_trip_bag = 0.0
    counter = 0
    for xp in xp_rates:
        xp_trip_control = xp_trip_control + (trip_control_gems[counter] * xp)
        xp_trip_bag = xp_trip_bag + (trip_bag_gems[counter] * xp)

    xp_base = int(input("Enter the current xp: "))
    xp_goal = int(input("Enter target xp: "))
    xp_target = xp_goal - xp_base

    print("\n","With average rates, you will need the following number of trips:","\n")
    print("Trips without gem bag: ",(xp_target/xp_trip_control))
    print("Trips with gem bag: ",(xp_target/xp_trip_bag))


    return 0

main()