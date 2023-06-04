global a
global c, t, ind

def sorting_data():
    lit_of_sort_data = list()
    with open("avilblst.txt") as red:
        for i in red:
            lit_of_sort_data.append(i)
        lit_of_sort_data.sort()
    with open("avilblst.txt", "w") as red:
        red.writelines(lit_of_sort_data)
        red.close()


def book_code_inp():
    c = 0
    a = 0
    book_code = input("\n-----> ")
    for code in avil_data:
        if book_code in code:
            a = 1
            c = c + 1
            break
        else:
            c = c + 1
            continue
    if a == 0:
        print("\t\t___ERROR___ ---> Code Invalid!! or Book Does Not Exists")
        book_code_inp()
    else:
        print("You Have Selected For Book --> ")
        print(avil_data[c - 1])
        gs(c)


def vist_P():
    print("\n \t\t\t\t \t\t\t\t****Visit Again****")
    sorting_data()


def gs(c):
    print(" Do You Want To Confirm It(Y/N)? --> ")
    confirm = input()
    if (confirm.lower() == "y") or (confirm.lower() == "yes"):
        with open("reurnlist.txt", "a") as g:
            g.writelines(avil_data[c - 1])
        avil_data.remove(avil_data[c - 1])
        with open("avilblst.txt", "w") as f:
            for data in avil_data:
                f.writelines(data)
            f.close()
        vist_P()
        print("\n \t\t\t\t\t\t Thank You For Borrowing The Book")
        exit()
    if (confirm.lower() == "n") or (confirm.lower() == "no"):
        vist_P()
        exit()
    else:
        print("Select only Y/N")
        gs(c)


def retun_book_inp():
    ret_bookcode = input("\n \tEnter the Book Code To Return It --> ")
    return_gs1(ret_bookcode)


def return_gs1(ret_bookcode):
    t = 0
    ind = 0
    with open("reurnlist.txt", "r") as f:
        ret_book_data = f.readlines()
        for i in ret_book_data:
            if ret_bookcode in i:
                t = 1
                ind = ind + 1
                break

            else:
                ind = ind + 1

    if t == 0:
        print("___ERROR___ ---> Code Invalid!! or Book Does Not Exists in Return List")
        retun_book_inp()

    else:
        if len(ret_bookcode) < 3:
            print("___ERROR___ ---> Code Invalid!! or Book Does Not Exists in Return List")
            retun_book_inp()
        else:

            with open("avilblst.txt", "a") as r:
                r.writelines(ret_book_data[ind - 1])
                ret_book_data.remove(ret_book_data[ind - 1])
                with open("reurnlist.txt", "w") as r1:
                    r1.writelines(ret_book_data)
            print(" \t\t\t\t\t\tThank You For Returning The Book! \n")
            sorting_data()
            exit()


print("\t\t**********************Welcome To GS Library********************** \n\n|--Select --|")
print("[1] --> To Barrow BOOK")
print("\n[2] --> To Return  BOOK")
print("\n[3] --> To Quit")


while True:
    try:
        opt = int(input("\n -------> "))
    except Exception as e:
        print("  *", e, "*")
        continue
    if opt == 1:
        with open("avilblst.txt", "r") as f:
            avil_data = f.readlines()
        print("\n\tAvailable Books In GS Library\n")
        for book in avil_data:
            print(book, end="\n")
        print("\nEnter the Book Code")
        book_code_inp()
# returning the book
    if opt == 2:
        t = 0
        ind = 0
        retun_book_inp()
    # exit Loop
    if opt == 3:
        vist_P()
        exit()
    if (opt != 1) and (opt != 2) and (opt != 3):
        print("\t\tWARNING: Select (1 or 2 or 3 only) From The Above Choices")
        continue
