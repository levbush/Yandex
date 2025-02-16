def find_farthest_orbit(list_of_orbits):
    return max(list_of_orbits, key=lambda x: x[0] * x[1] if x[0] != x[1] else 0)