nums = (3, 4, 6)

num1, num2, num3 = nums

even_nums = (2, num2, num3)


def shout_all(word1, word2):

    shout1 = word1 + '!!!'
    shout2 = word2 + '!!!'
    shout_words = (shout1, shout2)
    return shout_words


yell1, yell2 = shout_all('congratulations', 'you')

print(yell1)
print(yell2)
