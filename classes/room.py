
class Room:

    def __init__(self, room_name):
        self.room_name = room_name
        self.guests = []
        self.songs = []

    def number_of_guests_in_room(self):
        return len(self.guests)

    def check_in_guest_to_room(self, guest):
        if self.number_of_guests_in_room() < 5:
            self.guests.append(guest)
        else:
            return "Sorry, no more space. Pick another room."  

    def check_out_guests(self, guest):
        self.guests.remove(guest)

    def empty_room(self):
        self.guests.clear()

    def add_song(self, song):
        self.songs.append(song)
    