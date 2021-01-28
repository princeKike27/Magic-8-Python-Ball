"""
MAGIC 8-PYTHON-BALL

The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.
It was invented in 1950 by Albert C. Carter and Abe Bookman and is currently manufactured by Mattel.
The user asks a yes–no question to the ball, then turns it over to reveal an answer in a window on the ball. 
"""
from random import choice

# list to store answers of magic ball
answers_list = [
                'Yes - definitely.',
                'It is decidedly so.',
                'Without a doubt.',
                'The Words are the Process. The Process must continue. The Goal is the end of the Process.',
                'Ask again later.',
                'Better not tell you now.',
                'My sources say no.',
                'The Outlook is not so good, you are not ready child.',
                'Very doubtful.'
                ]

# Welcome Message
welcome_mess = 'Welcome to MAGIC 8-BALL, the Artifact that can answer all your existential questions....'
print('\n************** MAGIC 8-BALL **************\n')
print(welcome_mess, '\n')
print('Let\'s Begin...', '\n')


# GAME MECHANIC
# variable to check if cx wants to ask another question
is_playing = True
# store name of truth seeker
name = input('What is thy name fortune seeker? ')
# store question of truth seeker
question = input('What mystery of the universe do you wish to have insight? \n')

while is_playing == True:

    # print cx name and question
    if name != '':
        print(f'\nMagic Ball let us know the answer to {name}\'s question:\n{question}?')
    else:
        print(f'\nMagic Ball let us know the answer to the truth seeker\'s question:\n{question}?')
    print('\n************** The Great One has Spoken **************\n')

    # select a random answer from answers_list
    answer = choice(answers_list)
    print('Hear Star Child ....... The Truth has been revealed!')
    print(answer, '\n')

    # Ask cx if they have another question
    another_question = input('Do you seek another Truth Sight Seer (Yes/No)? ')
    if another_question.lower() == 'yes':
        # store question of cx
        question = input('What mystery of the universe do you wish to have insight? ')
    else:
        print('\nSee you on the Door that never closes...\n')
        break
