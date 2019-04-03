def weight_on_planets():
    weight = float(input("What do you weigh on earth? ")) 
    mweight = .38 * weight
    jweight = 2.34 * weight
    print("\nOn Mars you would weigh {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format(mweight, jweight))

if __name__ == '__main__':
   weight_on_planets()
