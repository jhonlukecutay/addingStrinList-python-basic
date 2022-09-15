dic = []

print("To show the list, type 'showlist'.")

ask = True

while ask:
    inDic = input("Please add a Word: ")
    dic.append(inDic)

    if inDic == 'showlist':
        dic.remove('showlist')
        print("The elements contained in the list are: ", dic)
        

    for i in range(1):
        print("Do you want to add again? y/n")
        tryAgain = input()
        
        if tryAgain == 'n':
            ask = False
