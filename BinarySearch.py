import random

def main():
    returned_list = generate_random_list()
    halve_list(returned_list)   


def generate_random_list():
    randomlist = []
    n = random.randint(0,100)
    for i in range(0,20):
        n = (n + 2)
        randomlist.append(n)
    return (randomlist)

def halve_list(list_passed):
    new_list = (list_passed)
    while len(new_list) > 1:
        print (new_list)
        cut = input("Enter a number: ")
        cut = int(cut)
        list_length = (len(new_list))
        middle_index = list_length//2
        first_half = new_list[:middle_index]
        second_half = new_list[middle_index:]
        if cut in first_half:
            new_list = first_half
            if len(new_list) < 2:
                print (new_list)
            else:
                continue
        elif cut in second_half:
            new_list = second_half
            if len(new_list) < 2:
                print (new_list)
            else:
                continue
        else:
            print ("Number not in any list")

main()