import sys
import re

with open('data\\ruliweb_target.txt', encoding='utf-8') as in_file:
    with open('data\\ruliweb_output.txt', 'w', encoding='utf-8') as out_file:
        for line in in_file:
            line = line.replace('width: 1200px', 'width: 900px')
            line = line.replace('width="1200"', 'width="900"')
            line = line.replace('height: 800px', 'height: 600px')
            line = line.replace('height: 817.87px', 'height: 613.40px')

            line = re.sub(r'(ILCE-6000|[0-9]+/[0-9]+sec|F/[0-9]+\.?[0-9]*|ISO-[0-9]+|[0-9]+\.?[0-9]*mm|\s\|\s)', r'', line)

            if '<br /></p>' in line:
                pass
            elif '</p>' in line:
                if len(line) != len('</p>\n'):
                    continue


            out_file.write(line)
