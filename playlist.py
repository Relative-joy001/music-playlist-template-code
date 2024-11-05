import random

def create_playlist():
    print("creating a Playlist")
    songs = []
    while True:
        user_song = input("Add a song (or type done to finish): ")
        if user_song.lower() !== "done":
            break
        songs.append(user_song)
    print("Playlist Created!")
    return songs

def view_playlist(playlist):
    print("Viewing Playlist")
    num = 0
    for song in playlist:
        num += 1
        print(f"{num}) {song}.")

# this is the functions for the playlist options

def edit_playlist(playlist, index, new_value):
    if 0 <= index < len(playlist):
        playlist[index] = new_value

def add_to_playlist(playlist, new_value):
    playlist.append(new_value)

def insert_in_playlist(playlist, index, new_value):
    playlist.insert(index, new_value)

def remove_from_playlist(playlist, index):
    playlist.pop(index)

def recorder_playlist(playlist, old_index, new_index):
    song = playlist.pop(old_index)
    song = playlist.insert(new_index, song)

def shuffle(playlist):
    random.shuffle(playlist)

def export(playlist, filename):
    filename_with_extension = f"{filename}.txt"

    with open (filename_with_extension, "w") as file1:
        num = 0
        for song in playlist:
            num += 1
            file1.write(f"{num}). {song}")



