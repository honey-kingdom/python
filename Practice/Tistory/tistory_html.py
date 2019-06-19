
with open('data\\tistory_target.txt', encoding='utf-8') as target:
    with open('data\\tistory_output.txt', 'w', encoding='utf-8') as output:
        for line in target:
            output.write(
                '<p style="text-align: center; clear: none; float: none;"><br /></p>\n')
            output.write(
                '<p style="text-align: center; clear: none; float: none;"><br /></p>\n')
            output.write(
                '<p style="text-align: center; clear: none; float: none;"><br /></p>\n')
            output.write(line)
        output.write(
            '<p style="text-align: center; clear: none; float: none;"><br /></p>\n')
        output.write(
            '<p style="text-align: center; clear: none; float: none;"><br /></p>\n')
        output.write(
            '<p style="text-align: center; clear: none; float: none;"><br /></p>\n')
