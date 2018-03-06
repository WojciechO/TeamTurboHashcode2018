from ride import Ride
from car import Car

def read_input(fname):
    with open('./In/{}'.format(fname), 'r')as reader:
        R, C, F, N, B, T = [int(i) for i in reader.readline().split(" ")]

        cars = []

        for car in range(0, F):
            cars.append(Car())

        rides = []
        for ride in range(0, N):
            a, b, x, y, s, f = [int(i) for i in reader.readline().split(" ")]
            rides.append(Ride(a, b, x, y, s, f))

    return R, C, B, T, cars, rides

def write_output(results):
    pass


def taxi_metric(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])


if __name__ == "__main__":
    read_input('a_example.in')