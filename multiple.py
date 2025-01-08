class multiplefunctions():
    def Subfields():
        print("Subfields in AI are")
        print("Machine Learning")
        print( "Neural Networks")
        print ( "Vision")
        print("Robotics")
        print("Speech Processing")
        print( "Natural Language Processing")
    def OddEven(num):
        if (num%2==0):
            print(num," is even number")
        else:
            print(num, "is odd number")

    def Eligible(gender,age):
        if(gender=="Male"):
            if(age>=21):
                return "ELIGIBLE"
            else:
                return "NOT ELIGIBLE"
        if(gender=="Female"):
            if(age>=18):
                return "Eligible"
            else:
                return "Not Eligible"

    def percentage(Subject1,Subject2,Subject3,Subject4,Subject5):
        total=(Subject1+Subject2+Subject3+Subject4+Subject5)
        print("total=",total)
        percent=(total/500)*100
        print("Percentage=",percent)
   
    
    def triangle(h,b,h1,h2,b1):
        
        area=(h*b)/2
        print("Area formula:(Height*Breadth)/2")
        print("Area of triangle:",area)
        
        print("Perimeter formula:Height1+Height2+Breadth")
        peri=h1+h2+b1
        print("Perimeter of triangle:",peri)