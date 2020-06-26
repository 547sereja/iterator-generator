from hashlib import md5




def hash_time(file):
    with open(file, 'r', encoding='utf8') as opened_file:
        lines = opened_file.readlines()
        for line in lines:
            yield md5(line.strip().encode()).hexdigest()

# print(hash_time('stars.txt'))
# s = hash_time('stars.txt')
# print(next(s))

for line in hash_time('stars.txt'):
    print(line)



