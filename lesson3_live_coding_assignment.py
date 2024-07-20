max_stars = 5
min_stars = 1
star = "* "

while min_stars <= max_stars:
    print(star * min_stars)
    min_stars += 1

max_stars -= 1

while max_stars > 0:
    print(star * max_stars)
    max_stars -= 1
