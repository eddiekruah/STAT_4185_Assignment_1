encrypted_file = open("/Users/eddiekruah/Downloads/STAT 4188/HW1/STAT_4185_Assignment_1/encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
char_list = list(encrypted_message)
decrypted = ''

p1 = 1
p2 = len(encrypted_message) - 2

while p1 < p2:
    char_list[p1], char_list[p2] = char_list[p2], char_list[p1]

    p1 += 2
    p2 -= 2

for char in char_list:
    decrypted += char

print(decrypted)


