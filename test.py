while True:
    user_input = str(input("Enter a Phrase: "))
    text = user_input.split()
    phrase = " "
    for i in text:
        phrase = phrase+str(i[0]).upper()
    print(phrase)