import re

# Constants
G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
c = 3e8  # speed of light in m/s
hbar = 1.0545718e-34  # reduced Planck constant in J·s
g0 = 9.81  # Earth's gravity in m/s^2 (1g)

# Mass constants (kg)
M_EARTH = 5.972e24  # Mass of the Earth in kg
M_SUN = 1.989e30    # Mass of the Sun in kg

# Tsar Bomba's data
TSAR_BOMBA_YIELD = 50e3 * 4.184e9  # Tsar Bomba yield in Joules (50 Megatons of TNT)

# Function to convert user input mass to kilograms
def convert_mass_to_kg(mass_input):
    match = re.match(r"(\d+\.?\d*)\s*(grams?|kilograms?|tons?|earths?|suns?)", mass_input.lower())
    
    if not match:
        raise ValueError("Invalid mass input. Please use a valid format (In grams, kilograms, metric tons, Earths or Suns).")
    
    number = float(match.group(1))
    unit = match.group(2)
    
    # Conversion factors
    if unit in ['gram', 'grams']:
        return number / 1000  # grams to kilograms
    elif unit in ['kilogram', 'kilograms']:
        return number  # already in kg
    elif unit in ['ton', 'tons']:
        return number * 1000  # tons to kilograms
    elif unit in ['earth', 'earths']:
        return number * M_EARTH  # earth masses to kilograms
    elif unit in ['sun', 'suns']:
        return number * M_SUN  # sun masses to kilograms
    else:
        raise ValueError("Unrecognized unit. Please input a valid unit.")

# Function to convert to appropriate units for Schwarzschild radius
# Function to convert to appropriate units for Schwarzschild radius
def convert_units(value):
    def sci_not(val):
        mantissa, exponent = f"{val:.3e}".split('e')
        exponent = int(exponent)
        return f"{mantissa} * 10^{exponent}"

    if value < 1e-3:
        return f"{sci_not(value * 1e3)} millimeters"
    elif value < 1:
        return f"{sci_not(value * 1e2)} centimeters"
    elif value < 1e3:
        return f"{sci_not(value)} meters"
    elif value < 1e6:
        return f"{sci_not(value * 1e-3)} kilometers"
    elif value < 9.461e15:
        return f"{sci_not(value / 9.461e15)} light years"
    else:
        return f"{sci_not(value)} meters"

# Formatting scientific notation to "mantissa * 10^exponent"
def custom_scientific_notation(value):
    mantissa, exponent = f"{value:.3e}".split('e')
    exponent = int(exponent)  # Convert exponent to an integer for better formatting
    return f"{mantissa} * 10^{exponent}"

# Convert gravitational pull to Earth's gravity (g)
def gravitational_pull_in_g(g_pull):
    g_in_g = g_pull / g0  # Divide by Earth's gravity (9.81 m/s^2)
    return custom_scientific_notation(g_in_g)  # Format to show result in scientific notation

# Function to calculate energy released during black hole evaporation
def energy_released(mass):
    return mass * (c**2)  # Energy = mass * c^2

# Convert the energy to kilotons, Hiroshima bombs, and Tsar Bombas
def convert_energy(energy):
    # Kilotons of TNT
    kilotons = energy / (4.184e12)  # 1 kiloton of TNT = 4.184 * 10^9 Joules
    
    # Hiroshima bombs (15 kilotons each)
    hiroshima_bombs = kilotons / 15  # 1 Hiroshima bomb is 15 kilotons
    
    # Tsar Bombas (50 Megatons each)
    tsar_bombas = energy / TSAR_BOMBA_YIELD  # Tsar Bomba yield in Joules
    
    return kilotons, custom_scientific_notation(energy), hiroshima_bombs, tsar_bombas

# Input: Mass of the black hole in various units
mass_input = input("Enter the mass of the black hole (In grams, kilograms, metric tons, Earths or Suns): ")

# Convert mass to kilograms
M = convert_mass_to_kg(mass_input)

# Ensure the mass is not too small or too large (realistic black hole mass)
if M < 1e-3:
    print("Warning: The black hole mass is extremely small, which may produce unrealistic results.")
elif M > 1e50:
    print("Warning: The black hole mass is extremely large, which may produce unrealistic results.")

# Calculate Schwarzschild radius
r_s = (2 * G * M) / (c**2)

# Convert Schwarzschild radius to appropriate units
r_s_converted = convert_units(r_s)

# Gravitational pull (acceleration) at Schwarzschild radius
g = (G * M) / (r_s**2)

# Calculate the lifetime of the black hole
tau = (5120 * 3.14159 * G**2 * M**3) / (hbar * c**4)

# Convert the lifetime from seconds to years for easier interpretation
tau_years = tau / (60 * 60 * 24 * 365.25)

# Calculate the energy released and convert to various units
energy = energy_released(M)
kilotons, energy_sci_not, hiroshima_bombs, tsar_bombas = convert_energy(energy)

# Print the results
print(f"The Schwarzschild radius is {r_s_converted}.")
print(f"The gravitational pull at the Schwarzschild radius is {gravitational_pull_in_g(g)} G's (Earth's gravity is 1G).")
print(f"The lifetime in seconds is {custom_scientific_notation(tau)} seconds.")
print(f"The lifetime in years is {custom_scientific_notation(tau_years)} years.")
print(f"\nThe energy released by the evaporation of the black hole is:")
print(f"- {kilotons:.3f} kilotons of TNT,")
print(f"- Equal to {energy_sci_not} Joules,")
print(f"- Which is equivalent to {hiroshima_bombs:.3f} Hiroshima bombs,")
print(f"- Or {tsar_bombas:.3f} Tsar Bombas.\n")
print("The Tsar Bomba's area of destruction is approximately 1,521 square miles.")
print("A single Tsar Bomba would be more than enough to completely wipe out New York City, Los Angeles, Houston, and many other major cities.")
