# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 21:02:20 2020

@author: brenojaruzo
"""
def make_album(artist_name, album_name, number_of_songs=None):
	artist_dictionary = {'artist': artist_name, 'album': album_name}
	if number_of_songs:
		artist_dictionary['number_of_songs'] = number_of_songs
		return artist_dictionary
	else:
		return artist_dictionary

teste = make_album('alice in chains', 'dirt')

print(teste)