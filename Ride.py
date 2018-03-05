
class Ride:

    def __init__(self, a, b, x, y, s, f):
        """
        Ride class defines one ride in the input.
        In encapsulates the information:
        ● a – the row of the start intersection (0 ≤ a < R)
        ● b – the column of the start intersection (0 ≤ b < C)
        ● x – the row of the finish intersection (0 ≤ x < R)
        ● y – the column of the finish intersection (0 ≤ y < C)
        ● s – the earliest start (0 ≤ s < T)
        ● f – the latest finish (0 ≤ f ≤ T) , (f ≥ s + |x − a| + |y − b|)
        """

        self.start_point = [a, b]
        self.finish_point = [x, y]
        self.earliest_start = s
        self.latest_finish = f

    def get_route_length(self):
        pass


