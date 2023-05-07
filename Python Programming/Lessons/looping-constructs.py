favorites = ["Chick-fil-A", "Chipotle",
             "Starbucks", "Panda Express", "Buc-ee's"]

# FOR LOOP
print("This is the for loop...")
for i in favorites:
    print("I love", i)

# WHILE LOOP
c = 0
print("This is the while loop...")
while c < len(favorites):
    print("I also love", favorites[c])
    c += 1
