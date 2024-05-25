import random
from collections import deque

class Spotify:
    def __init__(self):
        # Initialize two sample playlists
        self.playlist_1 = ["Song1", "Song2", "Song3"]
        self.playlist_2 = ["Song4", "Song5", "Song6"]
        
        # Set the current playlist to playlist_1 and start at the first song
        self.current_playlist = self.playlist_1
        self.current_index = 0
        
        # Initialize an empty queue using deque
        self.queue = deque()
    
    def prev(self):
        # Move to the previous song if possible
        if self.current_index > 0:
            self.current_index -= 1
        elif self.queue:
            # If at the first song and there are items in the queue, play the last song of the next playlist in the queue
            self.current_playlist = list(self.queue.popleft())
            self.current_index = len(self.current_playlist) - 1
        else:
            self.current_index = 0  # Stay at the first song if there's no previous song or queue
        
        print(f"Playing: {self.current_playlist[self.current_index]}")
    
    def _next(self):
        # Move to the next song if possible
        if self.current_index < len(self.current_playlist) - 1:
            self.current_index += 1
        elif self.queue:
            # If at the last song and there are items in the queue, play the first song of the next playlist in the queue
            self.current_playlist = list(self.queue.popleft())
            self.current_index = 0
        else:
            self.current_index = 0  # Loop back to the first song if there's no next song or queue
        
        print(f"Playing: {self.current_playlist[self.current_index]}")
    
    def shuffle(self):
        # Shuffle the current playlist and start from the first song
        random.shuffle(self.current_playlist)
        self.current_index = 0
        print("Playlist shuffled.")
    
    def add_to_queue(self, item):
        # Add a single song or an entire playlist to the queue
        if isinstance(item, list):  # If item is a list (playlist)
            self.queue.append(deque(item))
        elif isinstance(item, str):  # If item is a string (song)
            self.queue.append(deque([item]))
        else:
            raise ValueError("Item must be a song (str) or playlist (list).")
        
        print(f"Added to queue: {item}")
    
    def clear_queue(self):
        # Clear the queue
        self.queue.clear()
        print("Queue cleared.")
    
    def play(self):
        # Start playing from the queue if there's anything in it
        if self.queue:
            self.current_playlist = list(self.queue.popleft())
            self.current_index = 0
        
        print(f"Playing: {self.current_playlist[self.current_index]}")
    
    def get_queue(self):
        # Return the current queue as a list for display
        return list(self.queue)

# Example usage
spotify = Spotify()

# Adding songs and playlists to the queue
spotify.add_to_queue("Song7")
spotify.add_to_queue(spotify.playlist_2)

# Playing songs
spotify.play()  # Start playing the first song
spotify._next()  # Go to the next song
spotify.prev()  # Go to the previous song

# Shuffling the playlist
spotify.shuffle()

# Clearing the queue
spotify.clear_queue()

# Displaying the current queue
print(f"Current queue: {spotify.get_queue()}")
