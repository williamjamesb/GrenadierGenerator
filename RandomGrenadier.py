import random as rd
import names as nm
import datetime

#Internal parameters


#Guardsmen object
class Grenadier:
    sex = None
    name = None
    age = None
    rank = None
    squad = None
    personality = None
    skill = []
    flaw = []
    ambition = None
    friends = []
    rivals = []
    fav_food = None
    confirmed_kills = 0
    awards = []
    battles = 0
    remarks = []

#Generate basics
def basics(g):
    g.sex = 'male'
    g.name = nm.get_full_name(gender = g.sex)
    g.age = rd.randint(18,28)
    g.rank = 'Obergrenadier'
    g.remarks = ['Deployed '+str(datetime.date.today())]
    return g

#Generate demeanor
def demeanor(g):
    demeanors = [
    'Affable',
    'Backwater',
    'Heroic',
    'Spiteful',
    'Boisterous',
    'Braggart',
    'Cocky',
    'Dissenter',
    'Dreamer',
    'Gambler',
    'Green',
    'Incompetent',
    'Jaded',
    'Joker',
    'Loner',
    'Loose cannon',
    'Loyal',
    'Mentor',
    'Leech',
    'Never bathes',
    'Nihilist',
    'Numb',
    'Obsessive',
    'Old',
    'Optimist',
    'Pessimist',
    'Pious',
    'Psychotic',
    'Quiet',
    'Reckless',
    'Sarcastic',
    'Sensible',
    'Slacker',
    'Smooth',
    'Steely',
    'Strict',
    'Superstitious',
    'Talkative',
    'Thief',
    'Twitchy',
    'Narcissist',
    'Sympathizer',
    'Old',
    'Green',
    'Fanatic'
    ]
    g.personality = rd.choice(demeanors)

    if g.personality == 'Old':
        g.age = rd.randint(29,65)
        g.personality = rd.choice(demeanors)
    elif g.personality == 'Green':
        g.age = rd.randint(16,18)
        g.rank = 'Grenadier'

    #Favorite food
    foods = [
    'Schnitzel',
    'Bratwurst',
    'Schweinshaxe',
    'Hasenpfeffer',
    'Spaetzle',
    'Bratkartoffeln',
    'Leberkaese',
    'Gulasch',
    'Schwartzwaelder Kirchtorte',
    'Saurkraut'
    ]
    g.fav_food = rd.choice(foods)

    return g

#Generate ambition
def ambition(g):
    ambitions = [
    'marry a distant paramour',
    'start a business',
    'get promoted',
    'travel the world',
    'earn the respect of their comrades',
    'earn the respect of their superiors',
    'make a difference',
    'bring honor to their family',
    'make it home',
    'start a family',
    'become rich',
    'become a movie star',
    'become a sports star',
    'acquire knowledge',
    'meet someone famous',
    'learn to fly',
    'redeem themselves',
    'transfer to a different regiment',
    'protect a friend',
    'get laid',
    'write a book',
    'own their own house',
    'set a record',
    'serve up a cold plate of vengeance',
    'kill communists',
    'impress the Hauptmann',
    'sleep in',
    'just get five god damn minutes of peace and quiet for once',
    'eat like a king',
    'be remembered',
    'die for the Fuhrer',
    'get back to the good old days',
    'desert at the first opportunity'
    ]

    if rd.random() < 0.1:
        g.ambition = 'survive'
    else:
        g.ambition = rd.choice(ambitions)

    return g

#Generate flaws and boons
def traits(g):
    nflaws = rd.randint(0,2)
    nskills = rd.randint(0,2)
    if g.personality == 'Incompetent':
        nflaws = nflaws + 1
    elif g.personality == 'Heroic':
        nskills = nskills + 1

    skills = [
    'Nerves of steel',
    'Tinkerer',
    'Lucky',
    'Cook',
    'Crack shot',
    'Combat master',
    'Street fighter',
    'Lateral thinker',
    'Lightning reflexes',
    'Rapid reload',
    'Bulging biceps',
    'Heightened senses',
    'Tough as nails',
    'Unshakeable faith',
    'Foresight',
    'Ambidextrous',
    'Duelist',
    'Tireless',
    'Bookworm',
    'Observant',
    'Handyman',
    'Quick draw',
    'Hardy',
    'Born leader',
    'Unarmed warrior',
    'Unremarkable',
    'Silent move',
    'Good sense of direction',
    'Sound judgement',
    'Survivalist',
    'Athlete',
    'Good looking',
    'Unshakeable pride',
    'Patient',
    'Musician',
    'Awesome scar',
    'Trustworthy',
    'Hard target',
    'Die hard',
    'Cautious',
    'Zealous',
    'Mustache',
    'Beard',
    'Bald'
    ]

    flaws = [
    'Clumsy',
    'Unlucky',
    'Fragile',
    'Hesitant',
    'Careless',
    'Pacifist',
    'Dumb',
    'Death-wish',
    'Coward',
    'Paranoid',
    'Addict',
    'Slow',
    'Oblivious',
    'Awkward',
    'Poor discipline',
    'Bad back',
    'Allergies',
    'Ugly',
    'Poor health',
    'Weak',
    'Overweight',
    'Unbearable guilt',
    'Tainted',
    'Poor aim',
    'Insomniac',
    'Old wound',
    'Bad eyesight',
    'Basically deaf',
    'Dyslexic',
    'Illiterate',
    'Short temper',
    'Asthma',
    'Flat footed'
    ]

    for s in range(0,nskills):
        g.skill.append(rd.choice(skills))

    for s in range(0,nflaws):
        g.flaw.append(rd.choice(flaws))

    return g
