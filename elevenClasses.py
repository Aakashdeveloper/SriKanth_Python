
class databases:
    def insert(self, table, fields):
        out = "insert "+ fields + " in " + table
        print(out)
    
    def get(self, table, fields):
        out = "select "+fields+ " in " + table
        print(out)


# creating object
myfile = databases()
myfile.insert('Student', 'name')


newStudent = databases()