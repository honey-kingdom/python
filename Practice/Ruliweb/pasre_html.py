import sys

with open('in.txt', encoding='utf-8') as in_file:
    with open('out.txt', 'w', encoding='utf-8') as out_file:
        for line in in_file:
            line = line.replace('width: 1200px', 'width: 900px')
            line = line.replace('width="1200"', 'width="900"')
            line = line.replace('height: 800px', 'height: 600px')
            line = line.replace('height: 817.87px', 'height: 613.40px')

            if '<br /></p>' in line:
                pass

            elif '</p>' in line:
                if len(line) != len('</p>\n'):
                    continue

            out_file.write(line)
