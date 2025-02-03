import itertools

def compare_songs(song1, song2):
    """Ask the user to compare two songs and choose their favorite."""
    while True:
        choice = input(f"Which do you prefer?\n1: {song1}\n2: {song2}\n(Enter 1 or 2): ").strip()
        if choice == '1':
            return song1
        elif choice == '2':
            return song2
        else:
            print("Invalid input. Please enter 1 or 2.")

def rank_songs(songs):
    """Sorts songs based on user preference."""
    ranked_songs = []
    
    for song in songs:
        inserted = False
        for i, ranked_song in enumerate(ranked_songs):
            if compare_songs(song, ranked_song) == song:
                ranked_songs.insert(i, song)
                inserted = True
                break
        if not inserted:
            ranked_songs.append(song)
    
    return ranked_songs

def main():
    songs = [
        "sooner than later", "the resistance", "fancy", "find your love", "over my dead body",
        "the real her", "look what you've done", "doing it wrong", "furthest thing", "from time",
        "you & the 6", "6 pm in new york", "jungle", "30 for 30 freestyle", "redemption",
        "weston road flows", "fire & desire", "passionfruit", "teenage fever", "nothing into somethings",
        "jaded", "summer games", "club paradise", "days in the east", "trust issues",
        "paris morton music", "the motion", "get along better", "race my mind", "8 am in charlotte"
    ]
    
    print("\nLet's decide your top 20 Drake songs! You'll be asked to choose between two songs multiple times.")
    sorted_songs = rank_songs(songs)
    
    print("\nYour Top 20 Drake Songs:")
    for i, song in enumerate(sorted_songs[:20], 1):
        print(f"{i}. {song}")

if __name__ == "__main__":
    main()
