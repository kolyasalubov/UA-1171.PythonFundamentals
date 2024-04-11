def count_sheeps(sheep):
    result=0
    for i in sheep:
        if i==True:
            result+=1
    return result

array1 = [True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ]
        
result = count_sheeps(array1)
print(f"There are {result} sheeps in total")