print "How to say \"Hello World!!\""
print "\n"

print ">>> print \"Hello World!!\""
print "\n"
print "Hello World!!"

print "\n"
print "How to print out 10 times:\n"

print ">>> hello = list(\"Hello World!!\")"
print ">>> for i in range(0,10):"
print "...     print \"Hello World!!\""
print "\n"

hello = list("Hello World!!")
for i in range(0,10):
    print "Hello World!!"

print "\n"
print "How to print out \"Hello World!!\" for the number of characters in the string and remove the trailing character each iteration:\n"


print "The following does not finish, why not?"
print "There is a prize for the right answer!!"
print "\n"

print ">>> hello = list(\"Hello World!!\")"
print ">>> for i in hello:"
print "...     if i != hello[0]:"
print "...         del hello[-1]"
print "...     print ''.join(hello)"
print "\n"

hello = list("Hello World!!")
for i in hello:
    if i != hello[0]:
        del hello[-1]
    print ''.join(hello)

print "\n"
print "The following does work..."
print "\n"

print ">>> hello = list(\"Hello World!!\")"
print ">>> strLth = len(hello)"
print ">>> for i in range(0,strLth):"
print "...     if i != hello[0]:"
print "...         del hello[-1]"
print "...     print ''.join(hello)"
print "\n"

hello = list("Hello World!!")
strLth = len(hello)
for i in range(0,strLth):
    if i != 0:
        del hello[-1]
    print ''.join(hello)