
board_objects = []


class Cube:
    """
    - name - უჯრების კვეთის ინდექსი,
    - color - ფერი
    - is_empty (boolean) default მნიშვნელობა არის True, იცვლება იმის მიხედვით, დგას თუ არა ზედ რაიმე ფიგურა
    - can_move (boolean) default მნიშვნელობა არის False, როდესაც ავირჩევთ რომელიმე ფიგურას,იმის მიხედვით,
      თუ რომელ უჯრებზე შეუძლია გადასვლა, იმ უჯრებს მიენიჭება True მნიშვნელობა,
      სვლის დასრულებისას ან ფიგურის გადარჩევისას ყველა უჯრას ენიჭება ისევ False
    cube_inside - უჯრის შიგთავსი, ვერ ცავტვირთე ემოჯები, რომ შევავსო ფიგურებით.
      ასევე თუ უჯრა თეთრია, შევავსე "=" სიმბოლოთი, ხოლო შავი " ".
    """

    def __init__(self, name, color, figure, cube_inside):
        self.name = name
        self.color = color
        self.figure = figure
        self.is_empty = True
        self.can_move = False
        self.cube_inside = cube_inside
        if color == "Black" and self.cube_inside == " ":
            self.cube_inside = "="
        if not self.is_empty:
            self.cube_inside = self.figure
        # აქ არ ვიცი, ცალკე მეთოდი დავწერო თუ პირდაპირ ეგრე გამოვიტანო print-ით.
        print(" [" + self.cube_inside + "] ", end=" ")
        board_objects.append(self)


class Board:
    """
    collIndex - უჯრის ფერის ინდექსი. იცვლება თანმიმდევრობით coll - ფუნქციის გამოძახებისას.
    ასევე იმის მიხედვით, რიცხვების კენტ თუ ლუწ პოზიციაზეა უჯრა
    """

    """ ვხატავთ დაფას"""
    def __init__(self):
        letter = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
        numbers = ("8", "7", "6", "5", "4", "3", "2", "1")
        for x in numbers:
            print(x, end=" ")
            if (numbers.index(x) + 10) % 2 != 1:  # სტროფის ინდექსის გასაგებად, ლუწია თუ კენტი
                self.coll_index = "Black"
            else:
                self.coll_index = "White"
            for y in letter:
                Cube(name=y + x, color=self.coll(), figure=" ", cube_inside=" ")
            print("\n")
        print("   ", end=" ")
        for z in letter:
            print(z, end="     ")

    def coll(self):
        if self.coll_index == "White":
            self.coll_index = "Black"
            return self.coll_index

        self.coll_index = "White"
        return self.coll_index


b = Board()
"""
for i in board_objects:

    print(i.name, end = "-") # გამოაქვს board_objects-ის ობიექტები.
    print(i.color, end=",")

print("\n")
board_objects[1].figure = "king"
print(board_objects[1].figure)
"""