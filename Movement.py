
def Hoover_finalPosition(direction):
    d = len(direction)

    #Enter X coordinate
    countEast=int(input("Enter X co-ordinate of the hoover initial possition \n"))
    #Enter Y coordinate
    countNorth=int(input("Enter Y co-ordinate of the hoover initial possition \n"))

    countWest = 0
    countSouth = 0

    print("Traversed co-ordinates are ")
    for i in range(d):

        #for each direction N/S/W/E
        if (direction[i] == 'N'):
            countNorth += 1

        elif (direction[i] == 'S'):
            countSouth += 1

        elif (direction[i] == 'W'):
            countWest += 1

        elif (direction[i] == 'E'):
            countEast += 1

        k1 = (countEast - countWest)
        k2 = (countNorth - countSouth)
        print(k1, "", k2)


    # required final position of robot
    print("Final Hoover Position: ", (countEast - countWest),"", (countNorth - countSouth))


if __name__ == '__main__':


    direction = input("Enter the Driving instructions \n")
    Hoover_finalPosition(direction)

