def Longest_stable_sub_array(input_str):
    list_of_input_str=list(input_str.split())#when we do list(input)-- this will split
    #into individual characters eg: "1 23 40 5" --> "1"," ","2","3"," ","4","0"," ","5"
    #this was the reason for wrong o/p -- it is fixed when used .split() -- which will
    # split it by space
    k=int(list_of_input_str[0])
    # print(k)
    sub_arry=list_of_input_str[1:]
    # for _ in sub_arry:
    #     if " " in sub_arry:#this was the issue before
    #         sub_arry.remove(" ")
    length=len(sub_arry)
    for i in list(set(sub_arry)):
        count_n=sub_arry.count(i)
        if count_n>k:
            length=length-(count_n-k)
    return length






print(Longest_stable_sub_array("3 10 10 10 20 20 30 30 30 30"))