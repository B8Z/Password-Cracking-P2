import string
###                                               ###
## Uncomment to generate correct 6 & 8 pass list   ##
###                                               ###
# from urllib.request import urlopen
#
# LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
#
# f = open("six_character_passwords.txt", "a")
# t = open("eight_character_passwords.txt", "a")
#
# #ONLY RUN ONCE AND CLEAR TEXT FILE BEFORE RUNNING
# for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
#     if(len(guess) == 8):
#         t.write(guess + '\n')
#     if((len(guess) == 6 ) and not(any(x.isupper() for x in guess)) and not(any(x.isdigit() for x in guess)) and (any(x.isalnum() for x in guess))):
#         f.write(guess + '\n')
#
# f.close()
# t.close()
#

###                                               ###
## Uncomment to generate 3 uppercase letters list  ##
###                                               ###
# p1_file = open("three_uppercase_letters.txt", "a")
#
# uppercase_string = string.ascii_uppercase
# uppercase_string_2 = string.ascii_uppercase
# uppercase_string_3 = string.ascii_uppercase
#
# for letter in uppercase_string:
#     for letter_2 in uppercase_string_2:
#         for letter_3 in uppercase_string_3:
#             three_letter_word = letter + letter_2 + letter_3 + '\n'
#             p1_file.write(three_letter_word)


###                                               ###
## Uncomment to generate 5 lowercase letters list  ##
###                                               ###
# p2_file = open("five_lowercase_letters.txt", "a")
#
# lowercase_string = string.ascii_lowercase
# lowercase_string_2 = string.ascii_lowercase
# lowercase_string_3 = string.ascii_lowercase
# lowercase_string_4 = string.ascii_lowercase
# lowercase_string_5 = string.ascii_lowercase
#
#
# for letter in lowercase_string:
#     for letter_2 in lowercase_string_2:
#         for letter_3 in lowercase_string_3:
#             for letter_4 in lowercase_string_4:
#                 for letter_5 in lowercase_string_5:
#                     five_letter_word = letter + letter_2 + letter_3 + letter_4 + letter_5 + '\n'
#                     p2_file.write(five_letter_word)


###                                               ###
## Uncomment to generate part 3 of part 4          ##
###                                               ###
p2_file = open("part_four_list_6.txt", "a")

uppercase_string = string.ascii_uppercase
lowercase_string_2 = string.ascii_lowercase
lowercase_string_3 = string.ascii_lowercase
lowercase_string_4 = string.ascii_lowercase
lowercase_string_5 = string.ascii_lowercase
lowercase_string_6 = string.ascii_lowercase
lowercase_string_7 = string.ascii_lowercase
lowercase_string_8 = string.ascii_lowercase

#uhh definitely the best way to do this
for letter in uppercase_string:
    for letter_2 in lowercase_string_2:
        # p2_file.write(letter + letter_2 + '\n')
        # p2_file.write(letter_2 + letter + '\n')
        for letter_3 in lowercase_string_3:
            # p2_file.write(letter + letter_2 + letter_3 + '\n')
            # p2_file.write(letter_2 + letter + letter_3 + '\n')
            # p2_file.write(letter_3 + letter_2 + letter + '\n')
            for letter_4 in lowercase_string_4:
                # p2_file.write(letter + letter_2 + letter_3 + letter_4 + '\n')
                # p2_file.write(letter_2 + letter + letter_3 + letter_4 + '\n')
                # p2_file.write(letter_2 + letter_3 + letter + letter_4 + '\n')
                # p2_file.write(letter_2 + letter_3 + letter_4 + letter + '\n')
                for letter_5 in lowercase_string_5:
                    # p2_file.write(letter + letter_2 + letter_3 + letter_4 + letter_5 + '\n')
                    # p2_file.write(letter_2 + letter + letter_3 + letter_4 + letter_5 + '\n')
                    # p2_file.write(letter_2 + letter_3 + letter + letter_4 + letter_5 + '\n')
                    # p2_file.write(letter_2 + letter_3 + letter_4 + letter + letter_5 + '\n')
                    # p2_file.write(letter_2 + letter_3 + letter_4 + letter_5 + letter + '\n')
                    for letter_6 in lowercase_string_6:
                        p2_file.write(letter + letter_2 + letter_3 + letter_4 + letter_5 + letter_6 + '\n')
                        p2_file.write(letter_2 + letter + letter_3 + letter_4 + letter_5 + letter_6 + '\n')
                        # p2_file.write(letter_2 + letter_3 + letter + letter_4 + letter_5 + letter_6 + '\n')
                        # p2_file.write(letter_2 + letter_3 + letter_4 + letter + letter_5 + letter_6 + '\n')
                        # p2_file.write(letter_2 + letter_3 + letter_4 + letter_5 + letter + letter_6 + '\n')
                        # p2_file.write(letter_2 + letter_3 + letter_4 + letter_5 + letter_6 + letter + '\n')
                        # for letter_7 in lowercase_string_7:
                        #     p2_file.write(letter + letter_2 + letter_3 + letter_4 + letter_5 + letter_6 + letter_7 + '\n')
                        #     p2_file.write(letter_2 + letter + letter_3 + letter_4 + letter_5 + letter_6 + letter_7 + '\n')
                        #     p2_file.write(letter_2 + letter_3 + letter + letter_4 + letter_5 + letter_6 + letter_7 + '\n')
                        #     p2_file.write(letter_2 + letter_3 + letter_4 + letter + letter_5 + letter_6 + letter_7 + '\n')
                        #     p2_file.write(letter_2 + letter_3 + letter_4 + letter_5 + letter + letter_6 + letter_7 + '\n')
                        #     p2_file.write(letter_2 + letter_3 + letter_4 + letter_5 + letter_6 + letter + letter_7 + '\n')
                        #     p2_file.write(letter_2 + letter_3 + letter_4 + letter_5 + letter_6 + letter_7 + letter + '\n')
                            # for letter_8 in lowercase_string_8:
                            #     p2_file.write(letter + letter_2 + letter_3 + letter_4 + letter_5 + letter_6 + letter_7 + letter_8 + '\n')
                            #     p2_file.write(letter_2 + letter + letter_3 + letter_4 + letter_5 + letter_6 + letter_7 + letter_8 + '\n')
                            #     p2_file.write(letter_2 + letter_3 + letter + letter_4 + letter_5 + letter_6 + letter_7 + letter_8 + '\n')
                            #     p2_file.write(letter_2 + letter_3 + letter_4 + letter + letter_5 + letter_6 + letter_7 + letter_8 + '\n')
                            #     p2_file.write(letter_2 + letter_3 + letter_4 + letter_5 + letter + letter_6 + letter_7 + letter_8 + '\n')
                            #     p2_file.write(letter_2 + letter_3 + letter_4 + letter_5 + letter_6 + letter + letter_7 + letter_8 + '\n')
                            #     p2_file.write(letter_2 + letter_3 + letter_4 + letter_5 + letter_6 + letter_7 + letter + letter_8 + '\n')
                            #     p2_file.write(letter_2 + letter_3 + letter_4 + letter_5 + letter_6 + letter_7 + letter_8 + letter + '\n')
