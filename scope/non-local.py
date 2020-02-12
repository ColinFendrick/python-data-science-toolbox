def echo_shout(word):
    echo_word = word + word

    print(echo_word)

    def shout():
        """Alter a variable in the enclosing scope"""
        # Use echo_word in nonlocal scope
        nonlocal echo_word

        echo_word = echo_word + '!!!'

    shout()

    print(echo_word)


echo_shout('hello')
