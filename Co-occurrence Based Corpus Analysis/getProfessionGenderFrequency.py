import numpy as np

def GetEnglishGender(stc):
    gender = -1
    stc = stc.lower()
    stc = stc.split(" ")
    for i in stc:
        if(i in ["he", "him", "male", "man", "his", "boy", "father"]):
            gender = 1
    for i in stc:
        if(i in ["she", "her", "female", "woman", "girl", "mother", "lady", "hers"]):
            if(gender == -1 or gender == 0):
                gender = 0
            else:
                gender = 2
    return gender

def GetHindiGender(stc):
    gender = -1
    stc = stc.split(" ")
    for i in stc:
        if(i in hindi_male_pronouns):
            gender = 1
    for i in stc:
        if(i in hindi_female_pronouns):
            if(gender == -1 or gender == 0):
                gender = 0
            else:
                gender = 2
    return gender

def GetCounts(target):
    male = 0
    female = 0
    neutral = 0
    
    for stc in sentences:
        #stc = stc.lower()
        if(target in stc):
            gender = GetHindiGender(stc)  # change the function here for changing the language
            if(gender == 1):
                male += 1
            elif(gender == 0):
                female += 1
            elif(gender == 2):
                neutral += 1
    return male, female, neutral

f = open("../data/hi/hi.tok.txt", "r")   # pass the correct file path for dataset

sentences = f.readlines()

english_professions_file = open('IdentityTerms/english_professions.txt', 'r', encoding = 'utf-8')

hindi_professions_file = open('IdentityTerms/hindi_professions.txt', 'r',  encoding = 'utf-8')

hindi_professions = hindi_professions_file.read().split('\n')

english_professions = english_professions_file.read().split('\n')

with open('IdentityTerms/hindi_male_gender_pronouns.txt', 'r',  encoding = 'utf-8') as f:
    hindi_male_pronouns = f.read().split("\n")
with open('IdentityTerms/hindi_female_gender_pronouns.txt', 'r',  encoding = 'utf-8') as f:
    hindi_female_pronouns = f.read().split("\n")

print(hindi_male_pronouns)

print(hindi_female_pronouns)

for profession in hindi_professions:
    male, female, neutral = GetCounts(profession + " ")
    if(female != 0):
        print(profession, " -- Male: ", male, " , Female: ", female, " , Neutral: ", neutral, " , Ratio: ", (male/female))
