###########################################################################################
# Name: William Wilson
# Date: 
# Description: 
###########################################################################################

# the algorithm implemented iteratively
def passSomeBeers(bottles):
        if (bottles > 1):
                print(str(bottles) + " bottles of beer on athe wall.")
                print(str(bottles) + " bottles of beer.")
                print("Take one down, pass it around.")
                bottles = bottles - 1
                print(str(bottles) + " bottles of beer on the wall.")
                print()
                passSomeBeers(bottles)

        else:
                bottles == 1
                print(str(bottles) + " bottle of beer on the wall.")
                print(str(bottles) + " bottle of beer.")
                print("Take one down, pass it around.")
                bottles = bottles -1
                print(str(bottles) + " bottles of beer on the wall.")
                print()

###############################################
# MAIN PART OF THE PROGRAM
###############################################
passSomeBeers(99)

