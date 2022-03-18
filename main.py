def end_of_sentence(word):
    letters = []
    letters[:] = word
    last_letter = letters.pop()
    return (last_letter == "!") | (last_letter == "?") | (last_letter == ".")


def needed_sentence(last_word):
    letters = []
    letters[:] = last_word
    last_letter = letters.pop()
    return (last_letter == "!") | (last_letter == "?")


def to_string(sentence):
    string = ""
    for word in sentence:
        string.join(word)


def solution(text):
    words = text.split(" ")
    curr_sentence = []
    result = []
    for word in words:
        if end_of_sentence(word):
            if needed_sentence(word):
                curr_sentence.append(word)
                result.append("".join(curr_sentence.copy()))
            curr_sentence.clear()
        else:
            curr_sentence.append(word)
            curr_sentence.append(" ")
    return result


if __name__ == '__main__':
    txt = str(input("Enter text: "))
    sentences = solution(txt)
    print(sentences)
