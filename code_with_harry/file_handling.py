# STEP 1: CREATE THE FILE FIRST (if not exists)
with open('myfile.txt', 'a') as f:
    pass   # just creates the file safely


# STEP 2: READ THE FILE
with open('myfile.txt', 'r') as f:
    text = f.read()
    print(text)


# STEP 3: WRITE / APPEND TO THE FILE
with open('myfile.txt', 'a') as f:
    f.write('\nHello, world!')


# STEP 4: APPEND USING with (BEST PRACTICE)
with open('myfile.txt', 'a') as f:
    f.write('\nHey, I am inside with')

# FILE NAME
filename = "myfile.txt"

# 1️⃣ CREATE FILE (if not exists)
with open(filename, 'a') as f:
    pass


# 2️⃣ WRITE MODE ('w') → overwrite file
with open(filename, 'w') as f:
    f.write("This is WRITE mode\n")


# 3️⃣ READ MODE ('r')
with open(filename, 'r') as f:
    print("READ MODE:")
    print(f.read())


# 4️⃣ APPEND MODE ('a')
with open(filename, 'a') as f:
    f.write("This is APPEND mode\n")


# 5️⃣ READ + WRITE ('r+')
with open(filename, 'r+') as f:
    print("R+ MODE:")
    print(f.read())
    f.write("Written using r+ mode\n")


# 6️⃣ WRITE + READ ('w+')
with open(filename, 'w+') as f:
    f.write("Written using w+ mode\n")
    f.seek(0)
    print("W+ MODE:")
    print(f.read())


# 7️⃣ APPEND + READ ('a+')
with open(filename, 'a+') as f:
    f.write("Written using a+ mode\n")
    f.seek(0)
    print("A+ MODE:")
    print(f.read())


# 8️⃣ READ LINE BY LINE
with open(filename, 'r') as f:
    print("READLINES:")
    for line in f:
        print(line.strip())


# 9️⃣ CHECK FILE POINTER POSITION
with open(filename, 'r') as f:
    print("Pointer position:", f.tell())


# 🔟 MOVE POINTER (seek)
with open(filename, 'r') as f:
    f.seek(5)
    print("After seek:", f.read())


# 1️⃣1️⃣ CLOSE FILE (automatic with 'with')
print("File handling completed successfully.")
