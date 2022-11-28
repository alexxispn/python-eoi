song = '''You look so beautiful in this light
Your silhouette over me
The way it brings out the blue in your eyes
Is the Tenerife sea
And all of the voices surrounding us here
They just fade out when you take a breath
Just say the word and I will disappear
Into the wilderness'''

word_to_replace = input('Introduce la palabra que quieres reemplazar de la '
                        'canción: ')
word_to_replace_length = len(word_to_replace)
new_word = input('Introduce la nueva palabra: ')
index = song.index(word_to_replace)
new_song = song[:index] + new_word + song[index + word_to_replace_length:]
print(new_song)
