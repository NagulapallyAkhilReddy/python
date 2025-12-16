student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
alphabets=pandas.read_csv("nato_phonetic_alphabet.csv")
# print(alphabets)
alphabets_dict={row.letter:row.code for (index,row) in alphabets.iterrows()}
# alphabets_dict=alphabets.to_dict()
# print(alphabets_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
go_on=True
while go_on:
    user_input = input("please enter your word : ")
    user_list=[]
    for x in user_input:
        # print(alphabets_dict[f"{x}"])
        user_list.append(alphabets_dict[f"{x.upper()}"])
    if user_input.lower()=="exit":
        go_on=False

    print(user_list)

