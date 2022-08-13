import csv

is_finished = True
total = -1
count = 0
counts = 0
with open('data.csv', 'r') as f:
    wen = csv.reader(f)
    songs_list = list(wen)

print("Songs to Learn 1.0 - by Lindsay Ward")
print("6 songs loaded")

def main():
    Menu = '''Menu:
L - List songs
A - Add new song
C - Complete a song
Q - Quit'''
    while True:
        print(Menu)
        choose = input(">>> ").upper()
        if choose == "L":
            get_l(songs_list, total, count, counts)
        if choose == "A":
            get_a(songs_list)
        if choose == "C":
            get_c(songs_list)
        if choose == "Q":
            get_q(songs_list)
            print(f"{counts} songs has been loaded in data.csv")
            print("Have a nice day!")
            exit()


def get_l(songs_list, total, count, counts):
    for song in songs_list:
        total += 1
        if song[3] == "u":
            count += 1
            print(f"{total}. * {song[0]:<35}\t- {song[1]:30}\t({song[2]})")
        else:
            counts += 1
            print(f"{total}.   {song[0]:<35}\t- {song[1]:30}\t({song[2]})")

    print(f"{counts} songs learned,{count} songs still to learn")


def get_a(songs_list):
    global title_song, artist_of_song, input_year
    while True:
        title_song = input("Title: ")
        if title_song == "":
            print("Input can not be blank")
        else:
            break
    while True:
        artist_of_song = input("Artist: ")
        if artist_of_song == "":
            print("Input can not be blank")
        else:
            break
    while True:
        try:
            while is_finished != False:
                input_year = int(input("Year: "))
                if input_year < 0:
                    print("Number must be >= 0")
                else:
                    break
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            a = "u"
            b = [title_song, artist_of_song, str(input_year), a]
            add_song = f"{title_song} by {artist_of_song} {input_year} added to song list"
            print(add_song)
            songs_list.insert(4,b)
            break


def get_c(songs_list):
    if not 'u' in [i[3] for i in songs_list]:
        print('No songs to learn now!')
    else:
        while True:
            try:
                t = -1
                a_number = int(input("Enter the number of a song to mark as learned: "))
                for i in songs_list:
                    t += 1
                if a_number < 0:
                    print("Number must be >= 0")
                elif a_number > t:
                    print("Invalid number input")
                elif 0 <= a_number <= t:
                    if songs_list[a_number][3] == 'u':
                        songs_list[a_number][3] = "l"
                        print(f"{songs_list[a_number][0]} by {songs_list[a_number][1]} has been learned")
                    elif songs_list[a_number][3] == 'l':
                        print(f"You have already learned {songs_list[a_number][1]}")
                    break
            except ValueError:
                print("Invalid input; enter a valid number")


def get_q(songs_list):
    with open('data.csv', 'w', newline="") as file:
        csvf = csv.writer(file)
        csvf.writerows(songs_list)


main()
