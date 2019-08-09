import argparse
import webbrowser
from QQMusicAPI import QQMusic as qqm


DEFAULT_TOP = 3


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for musics or play them in your browser using QQMusic")
    parser.add_argument("search",
        help="Search for a song on QQMusic",
        metavar="song name or keyword")
    parser.add_argument("-p", "--play",
        help="Play the song by index",
        action="store_true")
    parser.add_argument("-t", "--top",
        help="Show the given number of songs that are best matched",
        type=int)
    parser.add_argument("-b", "--best",
        help="Play the best matched song",
        action="store_true")
    args = parser.parse_args()
    matched = qqm.search(args.search)
    data = matched.data
    print("Search key: <" + args.search + ">")
    print("================================================")
    print("Matched songs: " + str(matched.total_num))
    top = args.top if args.top else DEFAULT_TOP
    top = top if top < matched.total_num else matched.total_num
    print("================================================")
    print("Best matched(" + str(top) +"):")
    for i in range(top):
        print("["+str(i+1)+"]")
        print("\tName:\t\t"+data[i].name)
        print("\tTitle:\t\t"+data[i].title)
        data[i].extract()
        print("\tAlbum Name:\t"+data[i].album_name)
        print("\tAlbum Title:\t"+data[i].album_title)
        if len(data[i].singer) > 1:
            print("\tSingers:")
            for j in data[i].singer:
                print("\t\t\t"+j.name)
        else:
            print("\tSinger:\t\t" + data[i].singer[0].name)
        print("\tURL:\t\t" + data[i].song_url())
    if args.play:
        print("================================================")
        if args.best:
            play = 0
        else:
            play = input("Play(enter q to quit): ")
            if play == 'q':
                exit(0)
            try:
                play = int(play) - 1
            except:
                print("Error: Not an integer: " + str(play))
                exit(1)
            play = play if play < matched.total_num else matched.total_num
        data[play].extract()
        print("Now playing("+ str(play+1) +"):")
        print("\tName:\t\t" + data[play].name)
        print("\tTitle:\t\t" + data[play].title)
        print("\tAlbum Name:\t"+data[play].album_name)
        print("\tAlbum Title:\t"+data[play].album_title)
        if len(data[play].singer) > 1:
            print("\tSingers:")
            for i in data[play].singer:
                print("\t\t\t"+i.name)
        else:
           print("\tSinger:\t\t" + data[play].singer[0].name)
        print("\tURL:\t\t" + data[play].song_url())
        webbrowser.open(data[play].song_url())
