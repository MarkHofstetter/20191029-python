def get_user_number_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input == 'q':
            raise Exception('user requested stop - please handle me')
        try:
            user_input = int(user_input)
            break
        except ValueError:
            print("falsche eingabe")                
    return user_input