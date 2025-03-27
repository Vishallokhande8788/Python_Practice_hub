# # 26/03/2025
## Working with Binary file
#  working with binary fle : images , pdf , audio , video , etc

f = open("/workspaces/Python_Practice_hub/AdvancePython D sir/mango.jpg",'rb')
f2 = open("myMango.jpg",'wb')
f2.write(f.read(15000))
print("Mango is saved")