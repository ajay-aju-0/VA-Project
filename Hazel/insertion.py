import sqlite3,random
            
conn = sqlite3.connect('Hazel.db')
mycursor=conn.cursor()

list1=['It is a night time.',
        "Night time code time!!",
        "This night is dark as your IDE's theme.",
        "Hey, Owl how is your work going?",
        "Night men are smart men.",
        "I like the night. Without the dark, we'd never see the stars.Night is to see dreams and day is to make them true.",
        "Nothing like a nighttime stroll to give you ideas..",
        "The darkest night produce the brightest stars.",
        "Night is beautiful when you are happy, calming when you are stressed and lonesome when you are missing someone.",
        "The nighttime of the body is the daytime of the soul.",
        "Night time is the time when our thinking and feeling gains it peakness!"
        ]

for i in list1:       
    mycursor.execute('insert into night(sentence) values (?)',(i,))

conn.commit()
conn.close()