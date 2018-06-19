adjective1 = raw_input("Please Enter An Adjective")
name1 = raw_input("Please Enter A Name")
verb1 = raw_input("Please Enter A Verb")
place1 = raw_input("Please Enter A Place")
verb2 = raw_input("Please Enter A Verb")
noun1 = raw_input("Please Enter A Noun")
verb3 = raw_input("Please Enter A Verb")
noun2 = raw_input("Please Enter A Noun")
verb4 = raw_input("Please Enter A Verb")
place2 = raw_input("Please Enter A Place")
name2 = raw_input("Please Enter A Name")
verb5 = raw_input("Please Enter A Verb")
ending_phrase = raw_input("Please Enter Whatever You Want")

madlibs = ("""One %s day, %s was walking down the %s. They were going to %s their %s.
As they were %s, they saw a %s not far from where they stand. 
They %s towards the %s, and see their good friend %s. %s greets %s, and %s them. %s!""")
print(madlibs %(adjective1,name1,verb1,place1,verb2,noun1,verb3,noun2,verb4,place2,name1,name2,verb5,ending_phrase))
