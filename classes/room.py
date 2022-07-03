class Room:

    def __init__(self, name):
        self.room_name = name['room name']               
        self.room_capacity = name['capacity']
        self.room_guests = name['current guests']
        self.room_playlist = name['playlist']
        

    def check_you_can_add_room(self):
        new_room = self.room_name
        return new_room
    
    def check_in_status(self):
        guest_max = self.room_capacity
        guest_list = self.room_guests
        if guest_list >= guest_max:
            return 'full capacity, sorry!'
        else:
            return 'free to check in'
    
    def add_guest_to_room(self):
        guest_list = self.room_guests
        status = self.check_in_status() 
        if status == 'free to check in':
            guest_list += 1
            return guest_list
        else:
            return status
    
    def remove_guest_from_room(self):
        guest_list = self.room_guests
        status = self.check_in_status() 
        if guest_list == 0:
            return 'the room is empty!'
        else:
            guest_list -= 1
        return guest_list
        
    def add_song_to_room(self, song):
        songs_list = self.room_playlist
        songs_list.append(song)
        return songs_list[-1]

    def remove_song_from_room(self, song):
        songs_list = self.room_playlist
        songs_list.append(song)       
        songs_list.remove(song)
        for item in songs_list:
            return item
    
    