def shout_echo(word1, echo=1):
    if echo < 0:
        raise ValueError('echo must be greater than or equal to 0')

    echo_word = word1 * echo
    shout_word = echo_word + '!!!'

    return shout_word

shout_echo("particle", echo=5)
