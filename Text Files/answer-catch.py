user_answer = input("Why do you like programming? ")


with open("answer.txt", "a") as file_object:  # append mode
    file_object.write(f"\n{user_answer}")
