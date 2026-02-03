import math
class Vector:
    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y
    
    def __str__(self):
        return '({},{})'.format(self.x_cod, self.y_cod)

    #for magnitude => |v| = √(x2 + y2)
    def magnitude(self):
        m = (self.x_cod**2 + self.y_cod**2)**0.5
        return m
    
    #for vector addition (x1, y1), (x2, y2) => (x1+x2 , y1+y2)
    def vector_addition(self, another):
        v = (self.x_cod + another.x_cod , self.y_cod + another.y_cod)
        return v
    
    #for vector subtraction (x1, y1), (x2, y2) => (x1-x2 , y1-y2)
    def vector_subtraction(self, another):
        v = (self.x_cod - another.x_cod , self.y_cod - another.y_cod)
        return v
    
    #for scalar multiplication (x * k, y * k), (x,y) is a vector where k is a scalar (real number)
    def scalar_multiplication(self, another):
        v = (self.x_cod * another, self.y_cod * another)
        return v

    #for dot product => (x1 * x2) + (y1 * y2) - this returns a scalar not a vector
    def dot_product(self, another):
        d = (self.x_cod * another.x_cod) + (self.y_cod * another.y_cod)
        return d
    
    #for unit vector û = V / |V| = (x / |V|, y / |V|), V is the vector (x,y), |V| is the magnitude: √(x² + y²)
    def unit_vector(self):
        v_mag = self.magnitude()
        if v_mag == 0: return (0.00, 0.00)
        x1 = self.x_cod / v_mag
        y1 = self.y_cod / v_mag
        return x1,y1

    #for angle bw vectors cos_theta = (Dot Product)(A.B) / (|A| * |B|)
    #angle = acos(cos_theta)
    def angle_bw_vectors(self, another):
        dp_num = self.dot_product(another)
        x = self.magnitude()
        y = another.magnitude()
        dp_den = x * y
        c = dp_num / dp_den
        angle_in_rad = math.acos(c) #in radians
        # angle_in_deg = math.degrees(angle_in_rad) #convert it into degree
        return angle_in_rad
    
    #for Orthogonality Check A . B = 0
    def orthogonal(self, another):
        if self.dot_product(another) < 0.0001:
            return "Vectors are Orthogonal"
        else:
            return "Vectors are not Orthogonal"
    
    #for vector projection = ( (A . B) / |B|² ) * B, B(x,y)
    def vector_projection(self, another):
        dp_num = self.dot_product(another)
        mag_den = (another.magnitude())**2
        if mag_den == 0: return (0.00, 0.00)
        div = dp_num / mag_den
        resultant = (div * another.x_cod, div * another.y_cod)
        return resultant
    

while True: 
    print("==============CHOOSE OPERATION===============")
    user_input = input("""
Enter 1 for Magnitude.
Enter 2 for Vector Addition.
Enter 3 for Vector Substraction.
Enter 4 for Dot Product.
Enter 5 for Scalar Multiplication.
Enter 6 for Unit Vector.
Enter 7 for Angle Between Vectors 
Enter 8 for Orthogonality Check. 
Enter 9 for Vector Projection. 
Enter 10 to exit.                                                                                                                                                              
Select: """)
    try:
        if user_input == '1':
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: ")) 
            mag = Vector(x1, y1)
            print("===========MAGNITUDE============")
            print(f"Magnitude of {mag} is: {mag.magnitude():.2f}")
    
        elif user_input == '2':
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: "))
            x2 = int(input("Enter x2: "))
            y2 = int(input("Enter y2: "))
            mag1 = Vector(x1, y1)
            mag2 = Vector(x2, y2)
            print("===========VECTOR ADDITION============")
            print(f"Vector Addition of {mag1} and {mag2} is: {mag1.vector_addition(mag2)}")
    
        elif user_input == '3':
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: "))
            x2 = int(input("Enter x2: "))
            y2 = int(input("Enter y2: "))
            mag1 = Vector(x1, y1)
            mag2 = Vector(x2, y2)
            print("===========VECTOR SUBTRACTION============")
            print(f"Vector Addition of {mag1} and {mag2} is: {mag1.vector_subtraction(mag2)}")
            
        elif user_input == '4':
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: "))
            x2 = int(input("Enter x2: "))
            y2 = int(input("Enter y2: "))
            mag1 = Vector(x1, y1)
            mag2 = Vector(x2, y2)
            print("===========DOT PRODUCT============")
            print(f"Dot Product of {mag1} and {mag2} is: {mag1.dot_product(mag2)}")
        
        elif user_input == '5':
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: ")) 
            mag = Vector(x1, y1)
            scalar_value = float(input("Enter the scalar value: "))
            print("===========SCALAR MULTIPLICATION============")
            print(f"Scalar Multiplication of {mag} using scalar value {scalar_value} is: {mag.scalar_multiplication(scalar_value)}")

        elif user_input == '6':
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: ")) 
            mag = Vector(x1, y1)
            ux, uy = mag.unit_vector()
            print("===========UNIT VECTOR============")
            print(f"Unit Vector of {mag} is: ({ux:.2f}, {uy:.2f})")
        
        elif user_input == '7':
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: "))
            x2 = int(input("Enter x2: "))
            y2 = int(input("Enter y2: "))
            mag1 = Vector(x1, y1)
            mag2 = Vector(x2, y2)
            print("===========ANGLE BETWEEN VECTORS============")
            print(f"Angle b/w Vector{mag1} and Vector{mag2} is: {mag1.angle_bw_vectors(mag2):.2f} rad")
            ch = input("Want to convert it into Degrees? (y/n): ").lower()
            if ch == 'y':
                deg = mag1.angle_bw_vectors(mag2)
                resultant = math.degrees(deg)
                print(f"In degrees: {resultant:.2f} deg")
            else:
                pass
        
        elif user_input == '8':
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: "))
            x2 = int(input("Enter x2: "))
            y2 = int(input("Enter y2: "))
            mag1 = Vector(x1, y1)
            mag2 = Vector(x2, y2)
            print("===========ORTHOGONALITY CHECK============")
            print(f"For a Vector {mag1} and Vector {mag2}, we can say that\n{mag1.orthogonal(mag2)}")
        
        elif user_input == '9':
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: "))
            x2 = int(input("Enter x2: "))
            y2 = int(input("Enter y2: "))
            mag1 = Vector(x1, y1)
            mag2 = Vector(x2, y2)
            ux, uy = mag1.vector_projection(mag2)
            print("===========VECTORS PROJECTION============")
            print(f"Vector Projections are : ({ux:.2f}, {uy:.2f})")
        
        elif user_input == '10':
            print("Exiting...Done")
            break

        else: 
            print("ERROR: Invalid Input!")

    except(ValueError, IndexError):
        print("ERROR: Pls enter a valid input! (integers)")