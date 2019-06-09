def merge_the_tools(string, k):

    for i, character in enumerate(string):
        if i % k == 0:
            sub_set = set()
            sub_string = ''

        if character not in sub_set:
            sub_set.add(character)
            sub_string += character

        if i % k == k - 1:
            print(sub_string)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
