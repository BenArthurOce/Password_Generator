
import random

#======================
#PART ONE - LIST DATA
#======================

# lists - Old Version. I'm not using these because I want shorter and more words that are easy to spell
colour_list = ['Red', 'Blue', 'Green', 'Orange', 'White', 'Black', 'Yellow', 'Purple', 'Silver', 'Brown', 'Gray', 'Pink', 'Olive', 'Maroon', 'Violet', 'Gold', 'Cyan', 'Tan', 'Rust', 'Indigo'] 
country_list = ['Russia', 'Canada', 'China', 'UnitedStates', 'Brazil', 'Australia', 'India', 'Argentina', 'Algeria', 'SaudiArabia', 'Mexico', 'Indonesia', 'Mongolia', 'Chad', 'Mali', 'Africa', 'Colombia', 'Ethiopia', 'Bolivia', 'Egypt',] 
Instrument_list = ['Triangle', 'Whistle', 'Piano', 'Kazoo', 'Harp', 'Viola', 'Oboe', 'Violin', 'Organ', 'Trombone', 'Spoons', 'Guitar', 'Vibraphone', 'Trumpet', 'Bongos', 'Ocarina', 'Clarinet', 'Ukulele', 'Cowbell', 'Drums'] 
bird_list = ['Penguin', 'Pigeon', 'Dove', 'Parrot', 'Seagull', 'Flamingo', 'Kingfisher', 'Toucan', 'Ostrich', 'Pelican', 'Eagle', 'Kiwi', 'Stork', 'Albatross', 'Blackbird', 'Turkey', 'Magpie', 'Robin', 'Heron', 'Hawk']
fruit_list = ['Apple', 'Banana', 'Grape', 'Strawberry', 'Pineapple', 'Peach', 'Mango', 'Watermelon', 'Blueberry', 'Honeydew', 'Passionfruit', 'Apricot', 'Mandarin', 'Avocado', 'Blackberry','Coconut','Cranberry','Raisin','Lemon','Nectarine'] 
vegetable_list = ['Sprouts', 'Chickpeas', 'Broccoli', 'Cabbage', 'Cauliflower', 'Celery', 'Kale', 'Lettuce', 'Spinach', 'Mushroom', 'Onion', 'Garlic', 'Carrot', 'Corn', 'Ginger', 'Parsnip', 'Zucchini', 'Turnip', 'Tomato', 'Beans']

# lists - New Version. Attempted to keep words under 6 characters, and easy to spell
maleNames_list = ['Alex', 'John', 'Ben', 'David', 'Steve', 'Randy', 'Kyle', 'Matt', 'Bart', 'Will', 'Adam', 'Graeme', 'Eric', 'Mark', 'Josh', 'Larry', 'Roger', 'Fred', 'Nick'] 
phonetic_list = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']
colour_list = ['Red', 'Blue', 'White', 'Black', 'Gray', 'Pink', 'Brown', 'Gold', 'Cyan', 'Pink']
fruit_list = ['Apple', 'Banana', 'Grape', 'Peach', 'Mango', 'Lemon']
number_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'] 
travel_list = ['Walk', 'Run', 'Stake', 'Drive', 'Jog', 'Fly', 'Tram', 'Train', 'Crawl']


#==========================
#PART TWO - CREATE PASSWORD
#==========================

# combine all elements of every list into a single list
list_of_all_elements = maleNames_list + phonetic_list + colour_list + fruit_list + number_list + travel_list

# shuffle all list elements (unrequired, but done for good measure)
random.shuffle(list_of_all_elements)

# select three elements to use for password
element01, element02, element03 = random.choices(list_of_all_elements, k = 3)

# combine three elements into a single password string, seperated by the underscore ('_') character
password_string = element01 + '_' + element02 + '_' + element03

# add a number between 10 and 99 to the end of the password string, seperated by the underscore ('_') character
password_string = element01 + '_' + element02 + '_' + element03 + '_' + str(random.randrange(10,99))


#============================
#PART THREE - ADJUST PASSWORD
#============================

adjusted_password_string = ''           # holds the new password which will have symbol adjustments

# create a dictionary that will swap a particular letter (Key) for a symbol (Value)
# if the partiular letter isn't found, then it will return the orginal letter
def fLetterstoCharacters(single_character):
    dict = {
        "s" : "$",
        "a" : "@",
        "o" : "0",
        "i" : "!",
        't' : "+",
    }

    # result is the corresponding symbol in the dictionary ONLY IF "single_character" exists in the dictionary
    # for example, the letter "z" isnt in the dictionary above so the result will be "z" (no adjustments)
    result = dict.get(single_character,single_character)
    return result


# loop through each INDIVIDUAL character in the password string and replace the letter with a symbol
# to be replaced, the letter must be found in the dictionary above
for each_character in password_string:
    str = fLetterstoCharacters(each_character)
    adjusted_password_string += str


#============================
#PART FOUR - DISPLAY PASSWORD
#============================

# print the password to the terminal
print("Unadjusted Password: {0:0}".format(password_string))
print("Adjusted Password:   {0:0}".format(adjusted_password_string))
print("Character Length:    {0:0}".format(len(adjusted_password_string)))

# print a warning message to the user
message = "\n" + \
          "Ensure that the generated password is over 15 characters and has at least one symbol\n" + \
          "If not, please run the code again"
print(message)
