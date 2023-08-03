def cubic_roots(coefficients):
    a, b, c, d = coefficients
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)
    discriminant = q**2 / 4 + p**3 / 27

    if discriminant > 0:
        u = (-q/2 + discriminant**0.5)**(1/3)
        v = (-q/2 - discriminant**0.5)**(1/3)
        real_root = u + v - b / (3*a)
        return [real_root]
    elif discriminant == 0:
        real_root = -2 * (q/2)**(1/3) - b / (3*a)
        complex_root = (q/2)**(1/3) - b / (3*a)
        return [real_root, complex_root, complex_root]
    else:
        r = (-p**3 / 27)**0.5
        theta = acos(-q / (2*r))
        roots = []
        for k in range(3):
            root = 2 * r**(1/3) * cos((theta + 2*k*pi) / 3) - b / (3*a)
            roots.append(root)
        return roots

def main():
    print("Enter the coefficients of the cubic equation ax^3 + bx^2 + cx + d = 0:")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    d = float(input("d: "))
    coefficients = [a, b, c, d]

    roots_formula = cubic_roots(coefficients)

    print("\nRoots using Cardano's formula:", roots_formula)

if __name__ == "__main__":
    main()
