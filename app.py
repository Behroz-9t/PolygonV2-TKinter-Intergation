import tkinter as tk
from Turtle.canvas import TKpanel
from Square_Class import Square
from Triangle_Class import Triangle
from Irreg_Polygon import IrregularPolygon
from Reg_Polygon import RegularPolygon


def draw_polygon_on_canvas(canvas:TKpanel, vertices):

    n = len(vertices)

    for i in range(n):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % n]
        canvas.add_line(p1, p2)


class App:
    def __init__(self):
    
        self.root = tk.Tk()
        self.root.title("Polygon Drawer by Behroz")
        self.canvas = TKpanel(self.root, width=900, height=1200)
        self.canvas.pack()
        self.list_of_coords=[]
        self.commanding()


    def commanding(self):

        print("(s) --> For giving Square's co-ordinates\n" \
        "(i) --> For giving irregular polygon's co-ordinates\n" \
        "(p) --> For giving regular polygon's co-ordinates\n" \
        "(t) --> For giving triangle's co-ordinates\n")


        self.command=input("Enter the alphabet from the list you want\n")
        if self.command=="s" :

            self.squareC()

        elif self.command=="i" :

            self.irregularPolyC()
       
        elif self.command=="p"  :

            self.regularPolyC()
       
        elif self.command=="t" :

            self.triangleC()

        else:
            print("Alphabet not found in the command list! ")


    def squareC(self):

        center_x=int(input("Enter the x coordinate for center: "))
        center_y=int(input("Enter the y coordinate for center: "))
        side=int(input("\nEnter the side length: "))
        square = Square((center_x,center_y),side)

        draw_polygon_on_canvas(self.canvas, square.vertices)

        suggestion=input("Would you like to calculate\n(a) --> area\n(p) --> perimeter\n")

        if suggestion=="a":
            print(square.area())
            suggestion_p=input("Now command (p) for perimeter or press enter to skip\n")
            if suggestion_p=="p":
                print(square.perimeter())
            else:
                print("\nThis command was not found or you skipped!\n")

        elif suggestion=="p":

            print(square.perimeter())
            suggestion_a=input("Now command (a) for area or press enter to skip\n")
            if suggestion_a=="a":
                print(square.area())
            else:
                print("\nThis command was not found or you skipped!\n")

        p=input("Would you like to continue y/n: ")
        if p=="y":
            self.commanding()

        else:
            print("\nProgram executed sucessfully!")




    def irregularPolyC(self):
        command="y"
        num=0
        c=1
        while command=="y":
            
            cords_x=int(input(f"Enter the x{c} coordinate: "))
            cords_y=int(input(f"Enter the y{c} coordinate: "))
            self.list_of_coords.append((cords_x,cords_y))


            num+=1 
            c+=1
            command=(input("\nDo you want to enter more coordinates for points y/n?: "))

        if num<4:
            print("\nPlease make sure the irregular polygon is of 4 or more sides\n")
            self.irregularPolyC()


        irreg = IrregularPolygon(self.list_of_coords)

        draw_polygon_on_canvas(self.canvas, irreg.vertices)

        suggestion=input("Would you like to calculate\n(a) --> area\n(p) --> perimeter\n")

        if suggestion=="a":
            print(irreg.area())
            suggestion_p=input("Now command (p) for perimeter or press enter to skip\n")
            if suggestion_p=="p":
                print(irreg.perimeter())
            else:
                print("\nThis command was not found or you skipped!\n")

        elif suggestion=="p":

            print(irreg.perimeter())
            suggestion_a=input("Now command (a) for area or press enter to skip\n")
            if suggestion_a=="a":
                print(irreg.area())
            else:
                print("\nThis command was not found or you skipped!\n")

        p=input("Would you like to continue y/n: ")
        if p=="y":
            self.list_of_coords.clear()
            self.commanding()

        else:
            print("\nProgram executed sucessfully!")   



    def triangleC(self):
        command="y"
        num=0
        c=1
        while command=="y":

            
            cords_x=int(input(f"Enter the x{c} coordinate: "))
            cords_y=int(input(f"Enter the y{c} coordinate: "))
            self.list_of_coords.append((cords_x,cords_y))

            num+=1 
            c+=1
            command=(input("\nDo you want to enter more coordinates for points y/n?: "))

        if num!=3:
            print("\nPlease make sure the triangle is of 3 sides only\n")
            self.triangleC()


        tri = Triangle(self.list_of_coords)

        draw_polygon_on_canvas(self.canvas, tri.vertices)

        suggestion=input("Would you like to calculate\n(a) --> area\n(p) --> perimeter\n")

        if suggestion=="a":
            print(tri.area())
            suggestion_p=input("Now command (p) for perimeter or press enter to skip\n")
            if suggestion_p=="p":
                print(tri.perimeter())
            else:
                print("This command was not found or you skipped!")

        elif suggestion=="p":

            print(tri.perimeter())
            suggestion_a=input("Now command (a) for area or press enter to skip\n")
            if suggestion_a=="a":
                print(tri.area())
            else:
                print("This command was not found or you skipped!")

        p=input("Would you like to continue y/n: ")
        if p=="y":
            self.list_of_coords.clear()
            self.commanding()

        else:
            print("Program executed sucessfully!")    
        

    def regularPolyC(self):

        no_of_side=int(input("\nEnter the number of sides: "))
        if no_of_side<5:
            print("The polygon should have more than 4 sides!")
            self.regularPolyC()
        center_xr=int(input("Enter the x coordinate for center: "))
        center_yr=int(input("Enter the y coordinate for center: "))

        radius=int(input("\nEnter the radius of the polygon: "))


        regpoly = RegularPolygon(no_of_side,radius,(center_xr,center_yr))

        draw_polygon_on_canvas(self.canvas, regpoly.vertices)

        suggestion=input("Would you like to calculate\n(a) --> area\n(p) --> perimeter\n")

        if suggestion=="a":
            print(regpoly.area())
            suggestion_p=input("Now command (p) for perimeter or press enter to skip\n")
            if suggestion_p=="p":
                print(regpoly.perimeter())
            else:
                print("\nThis command was not found or you skipped!\n")

        elif suggestion=="p":

            print(regpoly.perimeter())
            suggestion_a=input("Now command (a) for area or press enter to skip\n")
            if suggestion_a=="a":
                print(regpoly.area())
            else:
                print("\nThis command was not found or you skipped!\n")

        p=input("Would you like to continue y/n: ")
        if p=="y":
            self.commanding()

        else:
            print("\nProgram executed sucessfully!")

        self.root.mainloop()







