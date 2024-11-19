print(*{herb for herbs in [[input() for _ in range(int(input()))] 
                           for _ in range(int(input()))] for herb in herbs}, sep='\n')