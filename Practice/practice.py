
with open('data\\raw_youtube.copy', 'r') as r_file:
    with open('data\\playlist.txt', 'w') as w_file:
        i = 0
        for line in r_file:
            if line != '\n' and line != 'Corey Schafer\n':
                if i % 3 == 2:
                    w_file.write(f'{(i + 1) // 3}\t {line}')
                i += 1
