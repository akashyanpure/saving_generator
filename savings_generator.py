import random
# random number generator from 1 to 100
flag = True


# run while loop until the number is not in the file
# generate number
# check if the number is in the file or not
# append the number to the file


def random_number_generator():
    num = random.randint(1,30)
    return num

# check if the number is in the file or not
def check_number_in_file(num):
    with open('numbers.txt', 'r') as f:
        
        # read file content as a list
        with open('numbers.txt', 'r') as f:
            file_content = f.read().splitlines()
            print("file content is: ", file_content)
            if str(num) not in file_content:
                append_number_to_file(num)
                print("file content updated")
                return False
            else:
                print("number already in file")
                return True
        
        
# append the number to the list in file 
def append_number_to_file(num):
    with open('numbers.txt', 'a') as f:
        f.write(str(num) + '\n')       

if __name__ == "__main__":
    while(flag):
        num = random_number_generator()
        print("generated number is: ", num)
        flag = check_number_in_file(num)
        