watch_url = input('Enter original URL : ')

video_code = watch_url.split('watch?v=')[1]


embed_url = f'<p style="text-align: center; clear: none; float: none;"><iframe src="https://www.youtube.com/embed/{video_code}?autoplay=1&controls=0" width="200" height="113" frameborder="0" allowfullscreen=""></iframe></p>'

print(embed_url)
