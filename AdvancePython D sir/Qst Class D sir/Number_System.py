a = 1234
print(type(a))
print(a)











a = 0o1234567
print(a)
print(type(a))

a=0x123face
print(a)
print(type(a))

# base conversion function
#  # bin(): to convert any base to binary base

print(bin(123))
print(bin(0o123))
print(bin(0xface123))

#  # oct(): to convert any base to octal base

print(oct(123))
print(oct(0b1010))
print(oct(0xface123))
#  # hex(): to convert any base to hexadecimal base

print(hex(123))
print(hex(0b1010))
print(hex(0o123))

a= 10.5
print(a)
print(type(a))

# for fload data type only decimal number system is allowed
# a=0b1010.0b1010
# print(a)
# print(type(a))

a = 10+20j
print(a)
print(type(a))

a = 10+20j
print(a)
print(type(a))

# a = 10+20d
# print(a)
# print(type(a))
# its give an error because variable change j to d

# for real part any number system is allowded

a=0b101010+20j
print(a)
print(type(a))

# for imaginary part only decimal system is allowded
# a= 10+0b1011j
# print(a)
# print(type(a))

a=10+20j
b=30+40j
print(a+b)
print(a-b)
print(a*b)
print(a/b)
# print(a%b) type error :cannot mode complex number


a=10+20j
print(a.real)
print(a.imag)

a= True+10j
print(a)

# a= true + 10j
# print(a)
# error

# bool
a=True
print(a)
print(type(a))

a=False
print(a)
print(type(a))

# a = true NameError: name 'true' is not defined
# print(a)
# print(type(a))

print(True+True)
print(True+False)
print(False+True)
print(False+False)
print(True-False)
print(False-5)

name = 'John'
print(name)
print(type(name))


name= 'V'
print(name)
print(type(name))

name = "Vishal"
print(name)
print(type(name))

name=''' hello everyone 
        good morning
        we learn python
        in today's class
        
        '''
print(name)
print(type(name))
