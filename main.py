#
# Runs the algorithm on specified input file

import utils
import ride as ridez
import car as carz

R, C, B, T, cars, rides = utils.read_input('a_example.in')

time = 0
while time < T:

    for car in cars:
        if car.status == carz.CarStatus.BENCH:
            for ride in rides:
                if ride.status == ridez.RideStatus.WAITING_FOR_ASSIGNMENT:
                    car.assign_ride(ride)

        car.move(time)

    time += 1


