# Read text file

file = open("files/text_file.txt", "r")
text = file.readlines()
EOS = "</s>"
SOS = "<s>"
processed_text = []
splitters = [".", "?", ":", "\n"]
mark_sos = False


def start_of_new_line(token, index):
    if index == 0 and token[index].isupper():
        return True


def end_of_sentence(token):
    for s in splitters:
        if s in token:
            return True


def is_abbreviation(token):
    # first letter capital and period at the end
    if token[0].isupper() and token[token.__len__() - 1] == ".":
        return True
    else:
        return False


for line in text:
    tokens = line.split(' ')

    for index, token in enumerate(tokens):

        if mark_sos:
            processed_text.append(SOS + token)
            mark_sos = False
        elif start_of_new_line(token, index):
            processed_text.append(SOS + token)
        elif end_of_sentence(token):
            if not is_abbreviation(token):
                processed_text.append(token + EOS)
                mark_sos = True
            else:
                processed_text.append(token)

        else:
            processed_text.append(token)

print("".join(processed_text))

# print(processed_text)
