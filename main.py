import random

name_hero  = "Флоки"
hp_hero = 100

expirience = 0

# название, урон, прочность
rusty_sword = ["Ржавый меч", 5, 10]

iron_sword = ["Железный меч", 10, 20]

inventory = [rusty_sword]

# название, здоровье, урон, предмет
zombie = ["Зомби", 10, 5, ""]

# название, здоровье, урон, предмет
skeleton = ["Скелет", 20, 10, iron_sword]

# название, здоровье, урон, предмет
spider = ["Паук", 15, 7, ""]

enemies = [zombie, skeleton, spider]


while True:
  
  print(f"ваши характеристики: имя {name_hero}, хп {hp_hero}")
  print(f"ваш инвентарь: {inventory}")
  
  
  enemy_name = enemies[0][0]
  enemy_damage = enemies[0][2]
  enemy_hp = enemies[0][1]
  enemy_reward = enemies[0][3]
  
  print("вы встречаете", enemy_name)
  
  #  логика боя 
  while True:
    
    
    print(f"здоровье врага {enemy_hp}")
    print("1. Атаковать")
    print("2. Использовать предмет")
    print("3. Попытаться сбежать")
    choice = input("Выберите действие: ")
    if choice == "1":
      print("Вы атакуете врага")
      weapon = inventory[0]
      name_weapon = weapon[0]
      
      print(f"Ваше оружее {name_weapon}")
      # проверка прочности
      if weapon[2] > 0:
        damage = weapon[1]
        # отнимаем прочность 
        weapon[2] = weapon[2] - 1
      else:
        print("Ваше оружие сломано вы сражаетесь руками")
        damage = 3
      
      print(f"ваш урон {damage}")
      enemy_hp -= damage
      print(f"здоровье врага {enemy_hp}")
    elif choice == "2":
      print("Вы используете предмет")
      print("Вы ничего не нашли")
    elif choice == "3":
      print("Вы пытаетесь сбежать")
      print("Вы успешно сбежали")
      break
    else:
      print("Неверный выбор")
  
    if enemy_hp <= 0:
      print(f"{enemy_name} мёртв ")
      print("Вы победили врага")
      expirience += 1
      print(f"ваш опыт {expirience}")
      if enemy_reward != "":
        inventory.insert(0, enemy_reward)
      
      enemies.pop(0) 
      
      break
    
    print("Враг атакует вас")
    hp_hero -= enemy_damage
    print(f"ваше здоровье {hp_hero}")
    if hp_hero <= 0:
      print("Вы погибли")
      exit()
  

