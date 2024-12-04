import random

# we use this to access the properties of a class similarly in python we use self 

# Define the environment (room grid) (Room class) 
class Room:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # randomly assign numbers ie 0 or 1
        self.grid = [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]  # 0: clean, 1: dirty

# displays status of room 0 or 1
    def display(self):
        print("Room status:")
        for row in self.grid:
            print(row)
        print("\n")

# this method checks if the cell is dirty or not return true if dirty
    def is_dirty(self, x, y):
        return self.grid[x][y] == 1

# if the cell is dirty (1) changes it to (0) else prints already cleaned 
    def clean_cell(self, x, y):
        if self.grid[x][y] == 1:
            self.grid[x][y] = 0
            print(f"Cell ({x}, {y}) cleaned.")
        else:
            print(f"Cell ({x}, {y}) already clean.")

# check if all the room is clean or not
    def is_all_clean(self):
        return all(cell == 0 for row in self.grid for cell in row)

# Define the vacuum (class) cleaner agent
class VacuumCleaner:
    def __init__(self, room):
        self.room = room   # Room is the grid  
        self.x = random.randint(0, room.height - 1) # initial position chossed randomly 
        self.y = random.randint(0, room.width - 1)

# Enables movement on x axis and y axis (x + 1 = up on x axis and vice versa)
    def move(self, direction):
        if direction == 'up' and self.x > 0:
            self.x -= 1
        elif direction == 'down' and self.x < self.room.height - 1:
            self.x += 1
        elif direction == 'left' and self.y > 0:
            self.y -= 1
        elif direction == 'right' and self.y < self.room.width - 1:
            self.y += 1
        else:
            print("Invalid move")
        print(f"Vacuum moved to ({self.x}, {self.y})")

# method calls clean_cell method of the room class to clean the cell (current position)
    def clean(self):
        self.room.clean_cell(self.x, self.y)

     # enable random movement on the grid 
    def random_walk(self):
        return random.choice(['up', 'down', 'left', 'right'])

# Main function
def run_vacuum_cleaner():
    width, height = 5, 5  # Room dimensions 
    room = Room(width, height)
    vacuum = VacuumCleaner(room)

    room.display()

    # Run the vacuum cleaner until all cells are clean
    while not room.is_all_clean():
        vacuum.clean()
        direction = vacuum.random_walk()
        vacuum.move(direction)
        room.display()

    print("Room is fully cleaned!")

# Execute the vacuum cleaner simulation
if __name__ == "__main__":
    run_vacuum_cleaner()
