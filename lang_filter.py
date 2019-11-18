from better_profanity import profanity

# =============================================================================
# make sure to 
# * pip install better_profanity*
# before you proceeeeeeeed
# =============================================================================


# =============================================================================
# check 'https://pypi.org/project/better-profanity/' for more info
# =============================================================================

if __name__ == "__main__":
    profanity.load_censor_words()

    x = input("Enter a dirty sentence: ")
    output = profanity.censor(x);
    print(output)
    
    
# =============================================================================
#     you can also add custom badwords
# =============================================================================
    custom_badwords = ['duck', 'fish', 'banana']
    profanity.load_censor_words(custom_badwords)

    print(profanity.censor("Shut the duck up!"))
    # Fuck you

    print(profanity.censor("Have a banana ! :)"))
    # Have a ****! :)

    print(profanity.censor("What the fish"))
    # What the ****