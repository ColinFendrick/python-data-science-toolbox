def shout_echo(word1, echo=1, intense=False):
    echo_word = word1 * echo

    if intense is True:
        echo_word_new = echo_word.upper() + '!!!'
    else:
        echo_word_new = echo_word + '!!!'

    return echo_word_new


with_big_echo = shout_echo('Hey', echo=5, intense=True)

big_no_echo = shout_echo(word1='Hey', intense=True)
misorder = shout_echo(intense=False, echo=3, word1="Hoo")

print(with_big_echo)
print(big_no_echo)
print(misorder)
