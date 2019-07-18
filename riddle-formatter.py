# Riddle formatter
# A script to add some simple MarkDown formatting to riddles
#  so that people can see the riddles and click to see the answers.
#  I used this when making riddles I posted on a Discord server,
#  and I don't know if the answer hiding formatting works elsewhere.

# Copyright [2019] Lars Rune "SeaLiteral" Præstmark
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import random
# The riddles file should be a text file with one riddle per line,
#  each line must have a question, an andswer and an explanation,
#  separated by tabs.
# The default riddles are in Spanish, and the explanations are
#  in English. Some riddles involve two meanings of one word,
#  others split a word into two parts, then give synonyms for the word
#  and those words its parts look like.

riddles=open('riddles.tsv').read().splitlines()
print(len(riddles))

random.shuffle(riddles) # shuffle the riddles
print('\n'.join(riddles))
print()

def length_as_string(x):
    if ' 'not in x and '++' not in x:
        return str(len(x))
    parts=x.split()
    suffix = ' ('+str(len(parts))+' palabras)'
    if ('++' in x):
        parts=x.split('++')
        suffix=' = '+ str(len(x.replace('++','')))
    return ' + '.join ([str(len(i)) for i in parts])+suffix

def sound_length_as_string(x):
    # Replace some digraphs with single characters,
    # then count chartacters.
    y=x
    for i in '''qu k
h 
ll ł'''.splitlines():
        (a,b)=tuple(i.split(' '))
        y=y.replace(a,b)
    return length_as_string(y)

def count_syllables(x):
    y=x
    # This actually counts vowels but tries to remove diphthongs first.
    for i in 'aeiou':
        if (i!='i'):
            y=y.replace('i'+i,i)
            y=y.replace(i+'i',i)
        if (i!='u'):
            y=y.replace('u'+i,i)
            y=y.replace(i+'u',i)
        for i in 'áéíóú':
            if (i!='í'):
                y=y.replace('i'+i,i)
                y=y.replace(i+'i',i)
            if (i!='ú'):
                y=y.replace('u'+i,i)
                y=y.replace(i+'u',i)
    for i in 'bcdfghjklmnpqrstvwxyz':
        y=y.replace(i,'')
    return length_as_string(y)

for i in riddles:
    parts=i.split('\t')
    if len(parts)<3:
        print(parts)
        raise ValueError ('Missing explanation')
    else:
        # On Discord, you can hide text by putting it
        #  between pairs of pipe characters,
        #  people can then view it by clicking on it.
        print('Adivinanza: '+parts[0]+
              '\nRespuesta: ||'+parts[1].replace('++', ' + ')
              +'||\nExplicación: ||'+parts[2]+'||\nLetras: ||'+
              length_as_string(parts[1])+'||, fonemas: ||'+
              sound_length_as_string(parts[1])+'||, sílabas: ||'+
              count_syllables(parts[1])+
              '||\n\n')
