from ride import Ride


def read_input(fname):
    with open('./In/{}'.format(fname), 'r')as reader:
        R, C, F, N, B, T = [int(i) for i in reader.readline().split(" ")]

        rides = []
        for ride in range(0, N):
            a, b, x, y, s, f = reader.readline().split(" ")
            rides.append(Ride(a, b, x, y, s, f))

    return R, C, F, N, B, T, rides

def write_output(results):
    pass


def taxi_metric(point1, point2):
    pass


if __name__ == "__main__":
    read_input('a_example.in')