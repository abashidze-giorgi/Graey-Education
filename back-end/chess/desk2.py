
boardObjects = []

cube_names = ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8",
              "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",
              "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6",
              "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",
              "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
              "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",
              "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
              "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"]


class SetBoard:
    color = "White"
    rowIndex = 1
    colIndex = 1

    def __init__(self):
        for names in cube_names:
            BoardCube(names, self.set_color(), True, False)
            if self.colIndex == 8:
                self.set_color()
                self.colIndex = 0
            self.colIndex += 1

    def set_color(self):
        if self.color == "White":
            self.color = "Black"
            return self.color
        else:
            self.color = "White"
        return self.color


class BoardCube:

    def __init__(self, name, color, is_empty, can_move):
        self.name = name
        self.color = color
        self.insideObject = " [ ] "
        if color == "White":
            self.insideObject = " [=] "
        self.isEmpty = is_empty
        self.canMove = can_move
        boardObjects.append(self)


class DisplayBoard:

    SetBoard()
    letter = ["A", "B", "C", "D", "E", "F", "G", "H"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    colIndex = 1
    rowindex = 1

    def __init__(self):
        print(self.rowindex, end=" ")
        for i in boardObjects:

            if self.colIndex == 9:
                self.colIndex = 1
                self.rowindex += 1
                print("\n")
                print(self.rowindex, end=" ")
            print(i.insideObject, end="")
            self.colIndex += 1
        print("\n", end="  ")
        for x in self.letter:
            print("  " + x + "  ", end="")


DisplayBoard()
