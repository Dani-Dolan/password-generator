# Password Generator :key:

A program that will randomly combine words from given a text to generate a memorable passwords

## Install spaCy - A Natural Language Prcoessing Library
```
python3 -m pip install spacy
```

## Collect Words Into Nouns, Verbs, and Adjectives
Utilizes [spaCy](https://spacy.io/) to extract specific parts of speech like verbs, nouns, and adjectives 
```
$ python getNounsAdjVerb.py usdeclar.txt
Finished, see output in "words".
```

## Generate Passwords
```
$ python generatePassword.py -s 1 -w 2 words/* --l33t
CUTRenDeR`
w4Rbe4r"
foRmComM1+[
```
```
$ python generatePassword.py -n 3 -w 2 -m 5 words/*
MurderPower
InvestObject
TrialDerive
```

