"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

MARS_MULTIPLE = 0.378

def main():
    earth_weight = float(input('Enter a weight on Earth: '))
    mars_weight = earth_weight * MARS_MULTIPLE
    print('The equivalent weight on Mars: ' + str(mars_weight))

if __name__ == '__main__':
    main()
