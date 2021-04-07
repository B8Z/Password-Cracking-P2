from time import perf_counter
import hashlib

#First, get the hash from the user to get the sha1 hash to crack
sha1hash = input("Please input the hash to crack, make sure to include quotation marks.\n>")

#Second, we'll open a file full of 6 character password guesses
f = open("eight_character_passwords.txt")

LIST_OF_COMMON_PASSWORDS = str(f.read())

#Create a timer to store the total time elapsed in seconds, start timer
time_for_total_comparisons_start = perf_counter()

#Third, we'll take a guess from the list of passwords we opened, and split it by line
for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):

#Fourth, we'll hash the guess we took from the password list so we can compare it to the hash the user gave us
    hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()

#Fifth, we'll compare the hash the user gave us to the hashed version of the password guess and determine if they are equal
    if hashedGuess == sha1hash:

#Sixth, we'll tell the program what to do if the password guess matches, which is to print the current guess and quit the program.
#We'll also tell the program what to do if the password guess don't match, which is to return to step 3 to get a new password from the list
        print("The password is ", str(guess))
        quit()
    elif hashedGuess != sha1hash:
        print("Password guess ",str(guess)," does not match, trying next...")

#Now store the ending time
time_for_total_comparisons_stop = perf_counter()

#Calculate the total time
time_for_total_comparisons = time_for_total_comparisons_stop-time_for_total_comparisons_start

#In the seventh and final step, we'll tell the program what to do if we get all the way through the password list without finding a match.
print("Password not in database, we'll get them next time.")

print("Time taken for all comparisons: ", time_for_total_comparisons)
