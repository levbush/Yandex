def solve(*coefficients):
    match len(coefficients):
        case 1:
            return [] if coefficients[0] != 0 else ['all']
        case 2:
            b, c = coefficients
            return [-c / b] if b != 0 else solve(c)
        case 3:
            a, b, c = coefficients
            if a == 0:
                return solve(b, c)
            D = b**2 - 4 * a * c
            if D < 0:
                return []
            if D == 0:
                return [-b / (2 * a)]
            return [(-b - D**0.5) / (2 * a), (-b + D**0.5) / (2 * a)]