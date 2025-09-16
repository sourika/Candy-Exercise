# friend_favorites = [
#         ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
#         [ "Bob", ["milky way", "licorice", "lollipop"]],
#         [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
#         [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
#     ]

def get_friends_favorite_candy_count(favorites):
    candy_names = {}
    
    for person in favorites:
        for candy in person[1]:
            if candy_names[candy] in candy_names:
                candy_names[candy] += 1
            else:
                candy_names[candy] = 1    
    
    return candy_names



def create_new_candy_data_structure(data):
    specific_candy_dict = {}
    for person in data:
        name = person[0]       
        candies = person[1]
        for candy in candies:
            if candy in specific_candy_dict:
                specific_candy_dict[candy].append(name)
            else:
                specific_candy_dict[candy] = [name]
    
    return specific_candy_dict              



def get_friends_who_like_specific_candy(data, candy_name):
    pass

def create_candy_set(data):
    pass 


