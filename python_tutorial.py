mode_select = 3

# Problem No.1
if mode_select == 1:
    user_name = input("Enter your username please: ")
    password = input("Enter your password please: ")

    passowrd_length = len(password)
    password_encryption = ""

    for i in range(len(password)):
        password_encryption += password[i].replace(password[i],'*')

    print(f"Hey {user_name}, your password ({password_encryption}) is {passowrd_length} letters long!")

# Problem No.2
if mode_select == 2:
    picture = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
    ]

    picture_row_size = len(picture)
    picture_col_size = len(picture[0])

    print("\n")

    for x in range(picture_row_size):
        print(*picture[x][:], sep = ' ')

    print("\n")

    fill = '*'
    empty = ' '
    for i in range(picture_row_size):
        for j in range(picture_col_size):
            if picture[i][j] == 0:
                picture[i][j] = empty
            elif picture[i][j] == 1:
                picture[i][j] = fill

    for x_new in range(picture_row_size):
        print(*picture[x_new][:], sep = ' ')            

# Problem No.3
if mode_select == 3:
    alphabet_list = ['f', 'a', 'e', 'g', 'd', 'e', 'g', 'd', 'c', 'e', 'b']
    alphabet_list.sort()

    alphabet_list_element_count = []
    element_count_more_than_once = []
    final_repeated_elements_list = []
    final_repeated_elements_count = []


    for i in range(len(alphabet_list)):
        alphabet_list_element_count.append(alphabet_list.count(alphabet_list[i]))
        if alphabet_list.count(alphabet_list[i]) > 1:
                element_count_more_than_once.append(alphabet_list[i])


    # for i in range (1, len(element_count_more_than_once)):
    #     if element_count_more_than_once[i - 1] == element_count_more_than_once[i]:
    #         final_repeated_elements_list.append(element_count_more_than_once[i])
    #         final_repeated_elements_count.append(element_count_more_than_once.count(element_count_more_than_once[i]))

        
    print("Given alphabet list = ", *alphabet_list, sep = ' ')
    print("Counted element(s) of the list = ", *element_count_more_than_once, sep = ' ')
    # print("Times counted for each element = ", *final_repeated_elements_count, sep = ' ')

    
