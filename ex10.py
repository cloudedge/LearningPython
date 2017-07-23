tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print "\t \n \" %r " % tabby_cat
print "\t \n \" %s" % tabby_cat
print backslash_cat
print fat_cat
