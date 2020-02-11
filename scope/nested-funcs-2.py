def echo(n):

    def inner_echo(word1):
        echo_word = word1 * n
        return echo_word

    return inner_echo

twice = echo(2)
thrice = echo(3)
print(twice('hello '), thrice('hey there '))
