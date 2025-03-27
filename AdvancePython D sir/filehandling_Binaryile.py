# # # 26/03/2025
# ## Working with Binary file
# #  working with binary fle : images , pdf , audio , video , etc

# f = open("/workspaces/Python_Practice_hub/AdvancePython D sir/mango.jpg",'rb')
# f2 = open("myMango.jpg",'wb')
# f2.write(f.read(15000))
# print("Mango is saved")



# if we open any file usiong with statement then that file wiil be closed atomaically after compliting with body  

# # The 'with' statement ensures the file is automatically closed when done.
# with open('f1.txt', "r+") as f:
#     print(f.read())
#     f.write('\n hello With')
#     print("kya ye file closed hai : ", f.closed)
# # Outside the 'with' block, checking the file's closed status. 
# # Since the file was automatically closed when the 'with' block ended, this will print True.
# print("kya ye file closed hai : ", f.closed)


# wap for read text in f1 . text file and check how many lines starts with a how many stats with b  , c , etc 

f = open ('f1.txt','r')
data = f.readlines()
a_count = 0
b_count = 0
c_count = 0

for line in data :
    if line.startswith('a'):
        a_count=a_count+1
    elif line.startswith('b'):
        b_count=b_count+1
    elif line.startswith('c'):
        c_count=c_count+1
    else:
        print("kya ye file closed hai : ", f.closed)

print("a_count : ", a_count)
print("b_count : ", b_count)    
print("c_count : ", c_count)