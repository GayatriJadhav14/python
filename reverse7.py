def rev(s):
    s_list = list(s)
    start = 0
    end = len(s) - 1
    while start < end:
        s_list[start], s_list[end] = s_list[end], s_list[start]
        start += 1
        end -= 1
    return ''.join(s_list)   
a=input("enter name")
print("the original string:",a)
print("the reverse string:",rev(a))