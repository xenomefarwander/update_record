#Given a specified file, program creates instance of Student class, updates 
#'courses' attribute of instance, and uses 'update_record' method to replace 
#courses in text file database.

class Student:

    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses

    def update_record(self, filename):
        filedata = ''
        with open(filename, "r") as file:
            for line in file:
                if line.startswith(self.first_name+','+self.last_name):
                    replacement = str(self.first_name+','+self.last_name+':'+','.join(self.courses))
                    filedata = filedata + replacement
                else:
                    filedata = filedata + line
        with open(filename, "w") as file:
            file.write(filedata)
        return "Updated"
        
file_name = "data.txt"
courses = ["python","ruby","javascript"]
jane = Student("jane","doe",courses) #creates instance of 'jane' instance of Student class with mentioned attributes
print(jane) #shows content of jane after activtation
new_courses = ["singing", "dancing", "swimming"]
#jane.courses = new_courses #demonstrates 
print(jane.update_record(file_name))

#print(jane.sport)
#print(isinstance(jane, Student)) # This will test whether Jane is an object of the Student class
