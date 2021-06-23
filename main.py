def Hoover_finalPosition(direction):

    d = len(direction)

    # Enter Initial position of the Robotic Hoover
    countEast,countNorth=list(map(int,input("Enter the X Y Co-ordinate point of the Robotic Hoover initial Position: ").split(" ")))

    #Dirt particle coordinates
    dirtX,dirtY=[4,1,2,3],[2,3,2,3]
   
    countWest = 0
    countSouth = 0
    countDirt = 0
    dict1 = {};

    print("Traversed co-ordinates are ")
    for i in range(d):

        # for each direction N/S/W/E
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
        dict1[k1] = k2
    for key, value in dict1.items():
        for i in dirtX and dirtY:
            if (key == dirtX[i] and value == dirtY[i]):
                countDirt += 1

    print("Number of Dirt particles:", countDirt)

    # required final position of robot
    print("Final Hoover Position: ", (countEast - countWest), "", (countNorth - countSouth))

if __name__ == '__main__':


    direction = input("Enter the Driving instructions: \n")
    Hoover_finalPosition(direction)

