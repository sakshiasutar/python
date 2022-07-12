class emp:
    empcount=0
    malecount=0
    femalecount=0
    malecount=0
    designcount=0
    salarycount=0
    def __init__(self,en,eg,ed,ej,es):
        self.n=en
        self.g=eg
        self.d=ed
        self.j=ej
        self.s=es
        emp.empcount+=1
        if self.g=="MALE":
            emp.malecount+=1
        else:
            emp.femalecount+=1
        if self.d=="AM":
             emp.designcount+=1
        if self.s>10000:
              emp.salarycount+=1
    def display(self):
         print("name of emp=",self.n)
         print("gender=",self.g)
         print("designation",self.d)
         print("DOJ=",self.j)
         print("salary",self.s)
e1=emp("ab","FEMALE","AM","12-jan",30000)
e1.display()
e2=emp("dj","MALE","AP","15-jan",5000)
e2.display()
e3=emp("maya","FEMALE","AM","21-june",10000)
e3.display()
print("Total no of emp=",emp.empcount)
print("Total male emp=",emp.malecount)
print("Total female emp=",emp.femalecount)
print("Total num of emp with designation asst managar=",emp.designcount)
print("Total number of emp with salary more than 10000=",emp.salarycount)
         
