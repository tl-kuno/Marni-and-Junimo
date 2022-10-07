import spacy
sp = spacy.load('en_core_web_sm')


def process_input(user_input):
    """
    Accepts input and prints a list of lemmatized verbs and nouns

    Args:
        user_input (string): commnd input from the user
    """
    user_sp = sp(user_input)

    # find verbs given by user
    verbs = []
    for word in user_sp:
        if word.pos_ == "VERB":
            verbs.append(word.lemma_)

    # find objects given by user
    objects = []
    for word in user_sp:
        if word.pos_ == "NOUN":
            objects.append(word.lemma_)

    print(verbs)
    print(objects)


def main():
    """
    Continuously requests user input and destructures it to a command
    """
    while True:
        print("What should I do next:  ")
        user_command = input()
        process_input(user_command)


if __name__ == '__main__':
    main()
