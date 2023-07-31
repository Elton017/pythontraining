class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        
    def __str__(self):
        return f'Title: {self.title}, Artist: {self.artist}, Duration: {self.duration}'
        
class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.current = 0
        
    def add_song(self, song: Song):
        if song not in self.playlist:
            self.playlist.append(song)
    
    def remove_song(self, title):
        found = False
        for song in self.playlist:
            if song.title == title:
                self.playlist.remove(song)
                found = True
        if not found:
            print('not found')
    
    def play(self):
        if 0 <= self.current < len(self.playlist):
            return self.playlist[self.current]
        else:
            print('no song')
    
    def next_song(self):
        self.current += 1
        if self.current >= len(self.playlist):
            self.current = 0
        return self.playlist[self.current]
    
    def previous_song(self):
        self.current -= 1
        if self.current < 0:
            self.current = len(self.playlist) - 1
        return self.playlist[self.current]
    
    def display_playlist(self):
        for song in self.playlist:
            print(song.__str__())

s1 = Song('hello', 'jeff', 4.5)
s2 = Song('byeo', 'jeff', 1.59)
s3 = Song('he231o', 'jeff', 3.13)

# Create MusicPlayer instance
m = MusicPlayer()

# Add songs to the playlist
m.add_song(s1)
m.add_song(s2)
m.add_song(s3)

# Remove song from the playlist
m.remove_song('hello')

# Display the playlist
m.display_playlist()