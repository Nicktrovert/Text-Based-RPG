import random, os

class Player:
    Inventory = []
    Health = 100
    Energy = 100
    CurrentRoom = None
    def __init__(self, _Inventory = [], _Health = 100, _Energy = 100):
        self.Inventory = _Inventory
        self.Health = _Health
        self.Energy = _Energy
    def InspectRoom(self, room):
        os.system('cls')
        print("-----Loot-----")
        lootNumber = 0
        for loot in room.Loot:
            print(f"\n{lootNumber}. -{loot.Name}-\n{loot.Description}\nAmount:{loot.Amount}\n")
            lootNumber += 1

        print("-----Enemies-----")
        enemyNumber = 0
        for enemy in room.Enemies:
            print(f"\n{enemyNumber}. -{enemy.Name}-\n{enemy.Description}")
            enemyNumber += 1

        print("-----Rooms----- #- 0 is the way back (unless you are in the first room).")
        roomNumber = 0;
        for room in room.Rooms:
            print(f"\nRoom-{roomNumber}-")
            roomNumber += 1

    def EnterRoom(self, number):
        os.system('cls')
        print("\nYou entered The room.\n")
        selected_room = self.CurrentRoom.Rooms[int(number)]
        selected_room.Generate()
        selected_room.GenerateRooms()
        self.CurrentRoom = selected_room
    def TakeItem(self, number):
        os.system('cls')
        selected_item = self.CurrentRoom.Loot[int(number)]
        for item in self.Inventory:
            if item.Name == selected_item.Name:
                item.Amount += selected_item.Amount
                break
        else:
            self.Inventory.append(selected_item)
        self.CurrentRoom.Loot.remove(selected_item)
        print(f"\n {selected_item.Name} was added to your Inventory. \n")

    def CheckInventory(self):
        os.system('cls')
        print("-----Inventory-----")
        objNumber = 0
        for obj in self.Inventory:
            print(f"\n{objNumber}. -{obj.Name}-\n{obj.Description}\nAmount:{obj.Amount}\n")
            objNumber += 1

class Enemy:
    Name = ""
    Description = ""
    Health = 1
    AttackDamage = 1
    def __init__(self, _Name, _Description, _Health, _AttackDamage):
        self.Name = _Name
        self.Description = _Description
        self.Health = _Health
        self.AttackDamage = _AttackDamage

class Weapon:
    Name = ""
    Description = ""
    Amount = 1
    Damage = 0
    Durability = 0
    Range = 0
    def __init__(self, Name, description, damage, durability, range):
        self.Name = Name
        self.Description = description
        self.Damage = damage
        self.Durability = durability
        self.Range = range

class Item:
    Name = ""
    Description = ""
    Amount = 0
    Rarity = 0
    def __init__(self, _Name, _Description, _Amount, _Rarity):
        self.Name = _Name
        self.Description = _Description
        self.Amount = _Amount
        self.Rarity = _Rarity

    def generate_amount(self):
        # Define rarity thresholds for amount generation
        if self.Rarity == "Common":
            min_amount = 5
            max_amount = 15
        elif self.Rarity == "Uncommon":
            min_amount = 4
            max_amount = 12
        elif self.Rarity == "Rare":
            min_amount = 2
            max_amount = 8
        elif self.Rarity == "Epic":
            min_amount = 1
            max_amount = 5
        elif self.Rarity == "Legendary":
            min_amount = 1
            max_amount = 3
        else:
            raise ValueError("Invalid rarity")

        # Generate a random amount within the specified range
        return random.randint(min_amount, max_amount)


class Room:
    Loot = []
    Enemies = []
    Rooms = []
    def __init__(self):
        return
    def GenerateLoot(self):
        AmountOfLoot = random.randint(0, 2)
        for i in range(AmountOfLoot):
            RandomItemFromLootTable = LootTable[random.randint(0, len(LootTable)-1)]
            newLoot = Item(RandomItemFromLootTable.Name, RandomItemFromLootTable.Description, RandomItemFromLootTable.generate_amount(), RandomItemFromLootTable.Rarity)
            self.Loot.append(newLoot)

    def GenerateEnemies(self):
        AmountOfEnemies = random.randint(0, 2)
        for i in range(AmountOfEnemies):
            RandomEnemyFromLootTable = EnemyTable[random.randint(0, len(EnemyTable)-1)]
            newEnemie = Enemy(RandomEnemyFromLootTable.Name, RandomEnemyFromLootTable.Description, RandomEnemyFromLootTable.Health, RandomEnemyFromLootTable.AttackDamage)
            self.Enemies.append(newEnemie)

    def GenerateRooms(self):
        AmountOfRooms = random.randint(1, 2)
        for i in range(AmountOfRooms):
            newRoom = Room()
            newRoom.Rooms.append(self)
            self.Rooms.append(Room)

    def Generate(self):
        self.GenerateLoot()
        self.GenerateEnemies()
        return

key = Item("Key", "A key that unlocks a mysterious door.", 1, "Epic")
torch = Item("Torch", "A source of light to illuminate dark places.", 1, "Rare")
potion = Item("Potion", "A magical potion that restores health.", 1, "Uncommon")
gold = Item("Gold Coins", "Shiny coins worth their weight in gold.", 1, "Common")

LootTable = [key, torch, potion, gold, potion, gold, gold, gold, gold, potion, gold, gold, key]

goblin = Enemy("Goblin", "A small and cunning creature.", 50, 10)
skeleton = Enemy("Skeleton", "A reanimated undead with a bony frame.", 70, 15)
orc = Enemy("Orc", "A brutish humanoid with great strength.", 100, 20)

EnemyTable = [goblin, goblin, goblin, goblin, goblin, goblin, skeleton, skeleton, skeleton, orc]

if __name__ == '__main__':
    os.system('cls')
    print("---------Text-Based RPG-----------")
    player = Player()

    StartRoom = Room()
    StartRoom.Generate()
    StartRoom.GenerateRooms()

    Sword = Weapon("Beginner Sword", "The sword of beginnings.", 3, 350, 2)
    Spear = Weapon("Beginner Spear", "The spear of beginnings.", 2, 300, 3)
    Dagger = Weapon("Beginner Dagger", "The dagger of beginnings.", 4, 325, 1)

    StartRoom.Loot.append(Sword)
    StartRoom.Loot.append(Spear)
    StartRoom.Loot.append(Dagger)

    player.CurrentRoom = StartRoom

    GameIsRunning = True

    while GameIsRunning == True:
        UserInput = input("\nWhat do you want to do?"
                          "\n[1. Inspect the Room]"
                          "\n[2. Take an Item]"
                          "\n[3. Check your Inventory]"
                          "\n[4. Enter a Room]"
                          "\n")

        match UserInput:
            case "1":
                player.InspectRoom(player.CurrentRoom)
            case "2":
                if (len(player.CurrentRoom.Loot) != 0):
                    UserInput2 = input(f"\nWhat item do you want to pick? [0 - {len(player.CurrentRoom.Loot) - 1}]\n")
                    try:
                        if (int(UserInput2) <= len(player.CurrentRoom.Loot) and int(UserInput2) >= 0):
                            player.TakeItem(UserInput2)
                        else:
                            os.system('cls')
                            print("\nThat Item does not exist!\n")
                    except:
                        os.system('cls')
                        print("\nInvalid Input!\n")
                else:
                    os.system('cls')
                    print("\nNo Items to take!\n")
            case "3":
                player.CheckInventory()
            case "4":
                UserInput2 = input(f"\nWhat room do you want to enter?")
                try:
                    if (int(UserInput2) <= len(player.CurrentRoom.Rooms) and int(UserInput2) >= 0):
                        player.EnterRoom(UserInput2)
                    else:
                        os.system('cls')
                        print("\nThat Room does not exist!\n")
                except:
                    os.system('cls')
                    print("\nInvalid Input!\n")
            case _:
                print("Invalid Input!")
