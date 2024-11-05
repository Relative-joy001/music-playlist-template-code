import playlist

options = ["Create", "View", "Add", "Insert", "Remove", "Edit", "Recorder", "Shuffle", "Export", "Exit"]

music_playlist = []


def display_options(options):
    count = 0
    while count < len(options):
        options = options[count]
        print(f"{count + 1}. {option}")
        count += 1

print("Welcome t the playlist creator")

choice = ""
while choice != "exit":
    print("What whould you like to do?")
    display_options(options)
    choice = input(":")
    choice= choice.lower()

    if choice == "create" or choice == "1":
        music_playlist = playlist.create_playlist()

    elif choice == "view" or choice == "2":
        music_playlist = playlist.view_playlist(music_playlist)
        print(view)

    elif choice == "add" or choice == "3":
        new_song = input("Enter your song title: ")
        add = playlist.add_to_playlist(music_playlist, new_song)

    elif choice == "insert" or choice == "4":
        index = int(input("Enter your song index: "))
        new_song = input("Enter your song title: ")
        insert = playlist.insert_in_playlist(music_playlist, index, new_song)
        
    elif chooice == "remove" or choice == "5":
        index = int(input("Enter your song index: "))
        remove = playlist.remove_from_playlist(music_playlist, index)

    elif choice == "edit" or choice == "6":
        index = int(input("Enter your song index: "))
        new_song = input("Enter your song title: ")
        edit = playlist.edit_playlist(music_playlist, index, new_song)

    elif choice == "recorder" or choice == "7":
        old_index = int(input("Enter the old index of the song: "))
        new_index = int(input("Enter the new index of the song: "))
        recorder = playlist.recorder_playlist(music_playlist, old_index, new_index)

    elif choice == "shuffle" or choice == "8":
        shuffle = playlist.shuffle(music_playlist)

    elif choice == "export" or chioce == "9":
        filename = input("Enter your filename: ")
        export = playlist.export(music_playlist, filename)
        print(f"Playlist exported to {filename}.txt")


print("Thanks for running the playlist creator!")
