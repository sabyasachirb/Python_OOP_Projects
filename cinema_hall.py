class Star_Cinema:
    def __init__(self):
        self._hall_list = []

    @classmethod
    def _entry_hall(cls, hall):
        cls._hall_list.append(hall)



class Hall(Star_Cinema):
    def __init__(self, rows, cols, halls_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._halls_no = halls_no

    def _entry_show(self, show_id, movie_name, time):
        self.id = str(show_id)
        self.movie_name = str(movie_name)
        self.time = str(time)
        show_details = (self.id, self.movie_name, self.time)
        self._show_list.append(show_details)

        seat_allocation = []
        for _ in range(self._rows):
            row = []
            for _ in range(self._cols):
                row.append('free')
            seat_allocation.append(row)
        self._seats[show_id] = seat_allocation

    def _book_seats(self, show_id, seats_to_book):
        if show_id not in self._seats:
            print("ERROR: Show doesn't exist.")
            return

        seat_allocation = self._seats[show_id]
        for (row, col) in seats_to_book:
            if 0 <= row < self._rows and 0 <= col < self._cols:
                if seat_allocation[row][col] == 'free':
                    seat_allocation[row][col] = 'booked'
                    print(f"Seat at row {row}, col {col} booked successfully.")
                else:
                    print(f"Error: Seat at row {row}, col {col} is already booked.")
            else:
                print(f"Error: Seat at row {row}, col {col} is out of range.")

        self._seats[show_id] = seat_allocation

    def _view_show_list(self):
        if not self._show_list:
            print("ERROR: No shows available.")
            return

        print(f"Shows running in Hall {self._halls_no}: ")
        for show in self._show_list:
            id, movie_name, time = show
            print(f"ID: {id}, Movie: {movie_name}, Time: {time}")

    def _view_available_seats(self, show_id):
        if show_id not in self._seats:
            print("ERROR: Show doesn't exist.")
            return

        seat_allocation = self._seats[show_id]
        print(f"Available seats for show ID {show_id} in Hall {self._halls_no}:")
        available_seats = []
        for row in range(self._rows):
            for col in range(self._cols):
                if seat_allocation[row][col] == 'free':
                    available_seats.append((row, col))
                    print(f"Seat at row {row}, col {col} is available.")
        if not available_seats:
            print("No available seats for this show.")


class Counter:
    def __init__(self, hall):
        self._hall = hall

    def view_all_shows(self):
        self._hall._view_show_list()

    def view_seats(self, show_id):
        self._hall._view_available_seats(show_id)

    def book_tickets(self, show_id, seats_to_book):
        self._hall._book_seats(show_id, seats_to_book)


