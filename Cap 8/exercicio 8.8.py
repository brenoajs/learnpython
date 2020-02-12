def make_album(artist_name, album_name, number_of_songs=None):
    artist_dictionary = {'artist': artist_name, 'album': album_name}
    if number_of_songs:
        artist_dictionary['number_of_songs'] = number_of_songs
        return artist_dictionary
    else:
        return artist_dictionary


while True:

    print("Qual o nome do artista que você quer capturar? ")
    print("\nPara encerrar a brincadeira, digite 'q' ")

    artist_name = input("Digite o nome do artista: ")

    if artist_name == 'q':
        break

    print("Qual o nome do album que você quer capturar? ")
    print("\nPara encerrar a brincadeira, digite 'q' ")

    album_name = input("Digite o nome do album: ")

    if album_name == 'q':
        break

    cdzao = make_album(artist_name, album_name)
    print(cdzao)
