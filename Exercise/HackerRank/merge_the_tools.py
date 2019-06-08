def merge_the_tools(string, k):

    index = 0
    for i in string:
        if index % k == 0:
            sub_set = set()
            sub_string = ''

        if i not in sub_set:
            sub_set.add(i)
            sub_string += i

        if index % k == k - 1:
            print(sub_string)

        index += 1


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
