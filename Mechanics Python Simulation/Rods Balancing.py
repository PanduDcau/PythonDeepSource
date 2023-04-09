# H_S_about_0_magnitude = L_A + L_B + L_C
#
# H_S_about_0_magnitude = (1/3) * m * l^2 * ω + (1/3) * m * l^2 * ω + (1/3) * m * l^2 * ω
#
# Simplifying the expression:
# H_S_about_0_magnitude = m * l^2 * ω

# Get inputs from users
# Get inputs from users
n = int(input("Enter the number of rods in the system: "))
m_values = []
l_values = []
w_values = []

for i in range(n):
    m = float(input("Enter the mass of rod {} (in kg): ".format(i + 1)))
    m_values.append(m)

    l = float(input("Enter the length of rod {} (in meters): ".format(i + 1)))
    l_values.append(l)

    w = float(input("Enter the angular velocity of rod {} (in radians/second): ".format(i + 1)))
    w_values.append(w)

# Calculate the angular momentum for each rod
L_values = []
for i in range(n):
    L = (1 / 3) * m_values[i] * (l_values[i] ** 2) * w_values[i]
    L_values.append(L)
    print("The angular momentum of rod {} is {:.2f} kg.m^2/s.".format(i + 1, L))

# Calculate the total angular momentum of the system
H_S_about_0_magnitude = sum(L_values)

# Display the result
print("The magnitude of the angular momentum of the system of rods about point O is {:.2f} kg.m^2/s.".format(
    H_S_about_0_magnitude))
