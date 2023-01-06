import math

# Constants
PI = math.pi
EARTH_MASS = 5.972E+24    # kg
EARTH_RADIUS = 6.371E+6    # meters
SOLAR_RADIUS = 6.975E+8    # radius of star in meters
AU = 1.496E+11             # distance earth to sun in meters
PARSEC_LY = 3.262


def open_file():  # allows the file to be opened and if not it creates an error
    """
    Attempts to open the file inputted by the user and returns false if the file 
    can't be opened and requests to open a valid file
    """
    filename = input("Input data to open: ")
    while True:
        try:
            # opens the filename with .csv
            file_pointer = open(filename + ".csv")
            break
        except FileNotFoundError:
            print("\nError: file not found.  Please try again.")  # if error
            # then asks again for a proper file to open
            filename = input("Enter a file name: ")
    return file_pointer  # returns the file to be read


def make_float(s):  # attempts to make the input into a float and if not return -1
    """
    Makes the input into a flaot and accepts it 
    otherwise if it's not a float then it returns -1
    """
    try:
        float(s)
        return float(s)
    except ValueError:
        return -1


def get_density(mass, radius):  # fidns the density based on radius and mass
    """
    Finds the density based on radius and mass
    and based on a certain condition it returns the following output
    """
    mass = float(mass)
    rel_mass = mass*EARTH_MASS  # calcs the relative mass based on mass and earth mass
    radius = float(radius)
    rel_radius = radius*EARTH_RADIUS  # calcs the relative radisu based on the
    # radius and earh radius
    if mass > 0 and radius > 0:  # if the mass and radisu > 0 then it returns
        # the following output
        return 3 * (rel_mass) / (4 * PI * rel_radius ** 3)
    else:
        return -1.0


def temp_in_range(axis, star_temp, star_radius, albedo, low_bound, upp_bound):
    # determines the temp and also lets you know what planets are habitable in it
    """
    Finds the suitable temp. to host habitable planets
    and also makes all the paramters into flaots
    and based on certain conditions it returns False or True based on it
    """
    star_radius = make_float(star_radius * SOLAR_RADIUS)
    axis = make_float(axis * AU)
    star_temp = make_float(star_temp)
    albedo = make_float(albedo)
    low_bound = make_float(low_bound)
    upp_bound = make_float(upp_bound)
    # make all the paramters into floats
    planet_temp = star_temp*(star_radius/(2 * axis))**0.5 * (1 - albedo)**0.25
    if star_radius > 0 and axis > 0 and star_temp > 0 and albedo > 0 and low_bound > 0 and upp_bound > 0:
        # if they are greater than 0 then it prints out false or true based on the input
        if planet_temp <= upp_bound and planet_temp >= low_bound:
            return True
        else:
            return False
    else:
        return False


def get_dist_range():  # input the distance fomr earth and
    # returns error if distance
    # isn't a float or less than 0
    """
    Input a distance of light years and then prints out output
    based on input and gives an error if not a float and 
    distance lower than 0
    """
    j = input("\nEnter maximum distance from Earth (light years): ")
    counter = 0
    while True:
        try:
            counter = float(j)
        except ValueError:
            print("\nError: Distance needs to be a float.")
            j = input("\nEnter maximum distance from Earth (light years): ")
            continue
        if counter > 0:
            break
        else:
            print("\nError: Distance needs to be greater than 0.")
            j = input("\nEnter maximum distance from Earth (light years): ")
    return counter


def main():
    """
    calculates all of the masses, planets, stars etc.
    based on the input and uses condiotnals to determine the
    output
    """
    print('''Welcome to program that finds nearby exoplanets '''
          '''in circumstellar habitable zone.''')
    file_pointer = open_file()  # opens the file requested by user
    f = get_dist_range()
    pc = f / PARSEC_LY  # units conversion
    low_bound = 200
    upp_bound = 350
    albedo = 0.5
    max_numstar = 0
    max_numplanets = 0
    counter = 0
    cumulative = 0
    distancerocky = 100000000000000000
    habitatcounter = 0
    distancegassy = 100000000000000000
    # all variables are counters and they are used to calc planets etc.
    file_pointer.readline()
    for line in file_pointer:
        planetname = line[:25].strip()
        distance = make_float(line[114:])
        pmass = line[86:96]
        pradius = line[78:85]
        star_radius = line[106:113]
        star_temp = line[97:105]
        paxis = line[66:77]
        pmass = make_float(pmass)
        pradius = make_float(pradius)
        star_temp = make_float(star_temp)
        paxis = make_float(paxis)
        star_radius = make_float(star_radius)
        # all above liones converrts it into floats and pulls out the data using
        # string slicing
        if 0 < distance < pc:
            if int(line[58:65]) > max_numplanets:
                max_numplanets = int(line[58:65])
                # if the line is greater than the # of plents it sets it to
                # that variable
            if max_numstar < int(line[50:57]):
                max_numstar = int(line[50:57])
                # if the line is greater than the # of plents it sets it
                # to that variable
            if pmass != -1:  # if pmass is not equal to -1 then it it adds
                # on the counter and
                # finds the average mass
                counter += 1
                cumulative += pmass
                z = cumulative / counter
                s = round(z, 2)  # rounds the counter to 2 decimal points
            pdensity = get_density(pmass, pradius)
            if temp_in_range(paxis, star_temp, star_radius, albedo, low_bound, upp_bound):
                habitatcounter += 1
                if 0 < pmass < 10 or 0 < pradius < 1.5 or pdensity > 2000:  # determines
                    # if rocky or gaseous
                    if distance < distancerocky:
                        distancerocky = distance
                        nearestrocky = planetname
                else:
                    if distance < distancegassy:
                        distancegassy = distance
                        neargassy = planetname

    print("\nNumber of stars in systems with the most stars: {:d}.".format(
        max_numstar))
    print("Number of planets in systems with the most planets: {:d}.".format(
        max_numplanets))
    print("Average mass of the planets: {:.2f} Earth masses.".format(s))
    print("Number of planets in circumstellar habitable zone: {:d}.".format(
        habitatcounter))
    if distancerocky != 100000000000000000:
        print("Closest rocky planet in the circumstellar habitable zone {} is {:.2f} light years away.".format(
            nearestrocky, distancerocky * PARSEC_LY))
    else:
        print("No rocky planet in circumstellar habitable zone.")
    if distancegassy != 100000000000000000:
        print("Closest gaseous planet in the circumstellar habitable zone {} is {:.2f} light years away.".format(
            neargassy, distancegassy * PARSEC_LY))
    else:
        print("No gaseous planet in circumstellar habitable zone.")
