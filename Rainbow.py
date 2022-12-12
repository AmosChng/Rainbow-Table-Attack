import string
#definitions
possible_passwords_list = []
hash_password_list = []
reduction_function_list = []
rainbow_dict = {}
usedPwlist = []
unusedPwlist = []
used_hash_pw_list = []
unused_hash_pw_list = []
indexlist = []
password = 'Password'
hashValue = 'Hash Value'
reductionValue = 'Reduction Function'
index = 'Index'
for i in range(1, 1001):
    indexlist.append(i)
#Rainbow_file_path = "C:/Users/Amos Chng/PycharmProjects/CSCI262_A1/Rainbow.txt"
#possible_passwords_path = "C:/Users/Amos Chng/PycharmProjects/CSCI262_A1/Wordlist.txt"

def reduction(hash_digest):  #reduction method
    hex_to_int = int(hash_digest, 16)
    return hex_to_int % len(possible_passwords_list) + 1

def hash_function(string_to_be_hashed): #hashing method
    import hashlib
    result = hashlib.md5(string_to_be_hashed.encode())
    return result.hexdigest()

def get_num_of_password(): #get the number of password available
    count = 0
    with open("Wordlist.txt") as possible_passwords:
        while True:
            line = possible_passwords.readline()
            line1 = line.replace('\n', '')
            if line != "":
                count += 1
                possible_passwords_list.append(line1)
                unusedPwlist.append(line1)
            else:
                break
    print(f'Number of possible passwords = {count} \n')
    return count

def hash_list():
    for i in range(0, len(possible_passwords_list)):
        hash_value = hash_function(possible_passwords_list[i])
        hash_password_list.append(hash_value)
        unused_hash_pw_list.append(hash_value)

    return hash_password_list


def reduction_list():
    for i in range(0, len(hash_password_list)):
        reduction_value = reduction(hash_password_list[i])
        reduction_function_list.append(reduction_value)
    return reduction_function_list


def createHashChain():
    for i in range(0, len(possible_passwords_list)):
        #for each unused password
        if possible_passwords_list[i] not in usedPwlist and possible_passwords_list[i] in unusedPwlist:
            usedPwlist.append(possible_passwords_list[i])
            #if len(unusedPwlist) > 1:
            unusedPwlist.remove(possible_passwords_list[i])
            reduction_value = reduction(hash_function(possible_passwords_list[i]))
            pw_result = possible_passwords_list[reduction_value-1]
            if pw_result in unusedPwlist:
                usedPwlist.append(pw_result)
                if len(unusedPwlist) > 1:
                    unusedPwlist.remove(pw_result)
            reduction_value2 = reduction(hash_function(pw_result))
            pw_result2 = possible_passwords_list[reduction_value2 - 1]
            if pw_result2 in unusedPwlist:
                usedPwlist.append(pw_result2)
                #if len(unusedPwlist) > 1:
                unusedPwlist.remove(pw_result2)
            reduction_value3 = reduction(hash_function(pw_result2))
            pw_result3 = possible_passwords_list[reduction_value3 - 1]
            if pw_result3 in unusedPwlist:
                usedPwlist.append(pw_result3)
                #if len(unusedPwlist) > 1:
                unusedPwlist.remove(pw_result3)
            reduction_value4 = reduction(hash_function(pw_result3))
            pw_result4 = possible_passwords_list[reduction_value4 - 1]
            if pw_result4 in unusedPwlist:
                usedPwlist.append(pw_result4)
                #if len(unusedPwlist) > 1:
                unusedPwlist.remove(pw_result4)


    for i in range(0, len(hash_password_list)):
        if hash_password_list[i] not in used_hash_pw_list and hash_password_list[i] in unused_hash_pw_list:
            unused_hash_pw_list.remove(hash_password_list[i])
            used_hash_pw_list.append(hash_password_list[i])
            reduction_value = reduction(hash_function(possible_passwords_list[i]))
            hash_result = hash_password_list[reduction_value - 1]
            if hash_result in unused_hash_pw_list:
                used_hash_pw_list.append(hash_result)
                unused_hash_pw_list.remove(hash_result)
            reduction_value2 = reduction(hash_result)
            hash_result2 = hash_password_list[reduction_value2 - 1]
            if hash_result2 in unused_hash_pw_list:
                used_hash_pw_list.append(hash_result2)
                unused_hash_pw_list.remove(hash_result2)
            reduction_value3 = reduction(hash_result2)
            hash_result3 = hash_password_list[reduction_value3 - 1]
            if hash_result3 in unused_hash_pw_list:
                used_hash_pw_list.append(hash_result3)
                unused_hash_pw_list.remove(hash_result3)
            reduction_value4 = reduction(hash_result3)
            hash_result4 = hash_password_list[reduction_value4 - 1]
            if hash_result4 in unused_hash_pw_list:
                used_hash_pw_list.append(hash_result4)
                unused_hash_pw_list.remove(hash_result4)
    #print(usedPwlist)
    #x = 5
    #hash_chain_list = [usedPwlist[i:i + x] for i in range(0, len(usedPwlist), x)]
    #hash_chain_list2 = [used_hash_pw_list[i:i + x] for i in range(0, len(used_hash_pw_list), x)]

def generate_rainbow_table():
    # populate rainbow table
    for i in range(0, len(usedPwlist), 5):
        rainbow_dict[usedPwlist[i]] = used_hash_pw_list[i+4]


def generate_password_hash_reduction_function_table():
    print(f'{index:<0}{password:^25}{hashValue:^30}{reductionValue:>22}')
    for i in range(0, len(possible_passwords_list)):
        print(f'{indexlist[i]:<13} {possible_passwords_list[i]:<12}  {hash_password_list[i]:^10} {reduction_function_list[i]:>18}')

def write_rainbow_table_to_file():
    no_of_lines_rainbow_table = 0
    with open("Rainbow.txt", 'w') as f:
        for key, value in rainbow_dict.items():
            f.write('%s:%s\n' % (key, value))
            no_of_lines_rainbow_table += 1
        f.write(f'\nNumber of lines = {no_of_lines_rainbow_table}')
    #print(f'Number of lines = {no_of_lines_rainbow_table}')
    return no_of_lines_rainbow_table

def finding_pre_image():
    #or
    hexadecimal_length = 32
    check = True
    count = 0
    hash_input = input('\nEnter a 32 hexadecimal hash value: ')
    corresponding_pw = ''
    counter = 0
    rainbow_list = []
    successful_break = False
    index_no = 0
    loop_counter = 0
    while True:
        if (len(hash_input) != hexadecimal_length) or all(hex in string.hexdigits for hex in hash_input) == False:
            hash_input = input("Invalid hexadecimal, please enter only 32 digit hexadecimal: ")
        else:
            break

    if hash_input in rainbow_dict.values():
        print("Hexadecimal found in rainbow table")
        rainbow_list = list(rainbow_dict.keys())
        corresponding_pw = list(rainbow_dict.keys())[list(rainbow_dict.values()).index(hash_input)]
        index_no = rainbow_list.index(corresponding_pw)
        if index_no == 199:
            index_no = -1

    elif hash_input not in rainbow_dict.values():
        while count < write_rainbow_table_to_file():
            if check:
                reduction_val = reduction(hash_input)
            result = possible_passwords_list[reduction_val - 1]
            if hash_function(result) in rainbow_dict.values():
                corresponding_pw = list(rainbow_dict.keys())[list(rainbow_dict.values()).index(hash_function(result))]
                rainbow_list = list(rainbow_dict.keys())
                index_no = rainbow_list.index(corresponding_pw)
                print(f"hexadecimal found in rainbow table, {corresponding_pw}:{hash_function(result)}")
                break
            else:
                reduction_val = reduction(hash_function(result))
                check = False
                count += 1
                if count == write_rainbow_table_to_file():
                    print("Something went wrong, unable to find a match from the rainbow table")
                    break


    if hash_function(corresponding_pw) == hash_input:
        print(f"Pre-image of {hash_input} is {corresponding_pw}")
        #print(corresponding_pw)
    else:
        reduction_val = reduction(hash_function(corresponding_pw))
        while True:
            while counter < 201:
                point = possible_passwords_list[reduction_val-1]
                #print(f'{point} --Hash-> {hash_function(point)} Reduce ↙ ')
                if hash_function(point) == hash_input:
                    print(f"Pre-image of {hash_input} is {point}")
                    successful_break = True
                    break

                else:
                    reduction_val = reduction(hash_function(point))
                    counter+=1
                    if counter == 201:
                        loop_counter += 1
            if successful_break == True:
                break

            #print(f'index no: {index_no}')
            if hash_function(point) != hash_input and hash_function(rainbow_list[index_no+1]) == hash_input:
                print(f"Pre-image of {hash_input} is {rainbow_list[index_no+1]}")
                break
            else:
                reduction_val = reduction(hash_function(rainbow_list[index_no+1]))
                if index_no < len(rainbow_list)-2:
                    index_no+=1
                else:
                    index_no = 0
                    #index_no+=1
            counter = 0
            if loop_counter == write_rainbow_table_to_file():
                print('However, no pre-image matched after hash and reduce multiple times. Please try another hex digest ')
                break

def main():
    get_num_of_password()
    hash_list()
    reduction_list()
    generate_password_hash_reduction_function_table()
    createHashChain()
    generate_rainbow_table()
    write_rainbow_table_to_file
    finding_pre_image()

if __name__ == '__main__':
    main()
