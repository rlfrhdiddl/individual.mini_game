import random
import time

# 모든 캐릭터의 모체가 되는 클래스
# 도박적인 요소를 많이 넣으려고 함.
class Character:
    def __init__(self, name):
        self.name = name
        self.max_hp = random.randint(75,150)
        self.hp = self.max_hp
        self.max_mp = random.randint(50,150)
        self.mp = self.max_mp
        self.ad = random.randint(5,15)
        self.ap = random.randint(10,20)

    def attack(self, other):
        damage = random.randint(self.ad - 2, self.ad + 5)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}: HP {self.hp}/{self.max_hp}")

# 모든 몬스터의 모체가 되는 클래스
class Monster:
    def __init__(self, name):
        self.name = name
        self.max_hp = random.randint(50,150)
        self.hp = self.max_hp
        self.max_mp = random.randint(50,150)
        self.mp = self.max_mp
        self.ad = random.randint(5,15)

    def attack(self, other):
        damage = random.randint(self.ad - 2, self.ad + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}: HP {self.hp}/{self.max_hp}")


# 플레이어의 데미지 계산방식.
# self가 정의되어 있지 않았기 때문에 Character를 상속하는 클래스를 만들어서 self를 가져옮.
class player(Character):
     def attack(self, other):
        while True: 
          if att == 1:
            damage = random.randint(self.ad - 2, self.ad + 5)
            break
          elif att == 2:
            if self.mp < 50 :
                print("-----마나가 부족합니다. 약한 물리공격으로 대체합니다-----")
                damage = random.randint(self.ad - 5, self.ad + 2)
                break
            else :
                damage = random.randint(self.ap - 5, self.ap + 10)
                self.mp = max(self.mp - 50, 0)
                break
            
        other.hp = max(other.hp - damage, 0)
        print(f"!!!!!  {self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.  !!!!!")
        if other.hp == 0:
            print(f"-----{other.name}이(가) 쓰러졌습니다.-----")

     # 랜덤으로 정해진 플레이어의 ad와 ap를 확인할 수 있게 만든 창
     def statistics(self):
         return f"HP:{self.hp} MP:{self.mp} AD:{self.ad} AP:{self.ap} "      
     def show_status(self):
        print(f"{self.name}: HP {self.hp}/{self.max_hp} MP {self.mp}/{self.max_mp}\n")

# Monster을 mop로 정의
class mop(Monster):
    def attack(self, other):
        damage = random.randint(self.ad - 2, self.ad + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"!!!!!  {self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.  !!!!!")
        if other.hp == 0:
            print(f"-----{other.name}이(가) 쓰러졌습니다.-----")
    def show_status(self):
        print(f"{self.name}: HP {self.hp}/{self.max_hp} MP {self.mp}/{self.max_mp} AD: ?? AP: ??\n")

print("게임을 시작합니다")
time.sleep(1)
print("게임 내에서 사용할 캐릭터명을 입력하세요: ")
ID = str(input(" "))

hero = player(ID)
jmop = mop("BOSS")

print(f"\n당신의 스탯은 {hero.statistics()} 입니다.\n-AD와 AP의 수치에 비례하여 물리공격과 마법공격이 강해집니다.\n-마법공격은 물리공격보다 강하지만 마나가 부족하면 기존의 물리공격보다 약한 물리공격을 합니다.")
time.sleep(2)
print("\n스탯과 마나량을 고려하여 전략을 세우십시오.\n어떤 몬스터를 만나든 행운을 빕니다.\n\n준비가 되었다면 떠나봅시다 y/n")
choice = str(input())
if choice == "y":
    print("몬스터를 찾아 나섰습니다.")
elif choice == "n":
    print("시간은 기다려주지 않습니다.\n몬스터를 찾아 나섰습니다.")
else:
    print("이런! 얼른 몬스터를 잡고 싶으시군요\n몬스터를 찾아 나섰습니다.")

time.sleep(1)    
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")
time.sleep(1)

print("------------------------------\n!!!야생의 몬스터가 나타났다!!!\n------------------------------")

time.sleep(1)

print("이런! BOSS 몬스터 입니다. 싸우시겠습니까? y/n")
hero.show_status()
jmop.show_status()
ans = str(input())
if ans == "y":
    print("-------------------------공격합니다.-------------------------\n")
elif ans == "n":
    print("-------------------------\n싸움을 피할 수 없다..!!\n-------------------------\n공격합니다.\n")
else:
    print("-------------------------\n긴장하셨군요. 공격합니다.\n-------------------------\n")

while True:
  print("-----공격 타입을 선택해 주세요 1. 물리공격 2. 마법공격(mp-50) : -----\n")
  hero.show_status()
  jmop.show_status()
  att = int(input())
  damage = hero.attack(jmop)
  time.sleep(0.5)
  jmop.show_status()

  if jmop.hp == 0:
      print(f"-----{jmop.name}을 쓰러뜨렸습니다!-----")
      print(f"축하합니다. 당신은 {jmop.name}을 잡고 모험을 마쳤습니다.")
      break
  
  time.sleep(1)

  print(f"-----{jmop.name}가 공격합니다-----\n")
  time.sleep(0.5)
  jmop.attack(hero)
  time.sleep(0.5)
  hero.show_status()

  if hero.hp == 0:
      print(f"-----당신은 {jmop.name}에게 사망했습니다-----")
      break
  
