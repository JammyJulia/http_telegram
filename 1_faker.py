# 
# Uzdevums: Izmantojot bibliotēku Faker uzģenerēt fake datus
# https://faker.readthedocs.io/en/master/
# https://faker.readthedocs.io/en/stable/providers.html
# 
# Uzinstalē bibliotēku ievadot terminālī
# > pip install Faker
#
from faker import Faker

fake = Faker()
fakeLV = Faker('lv_LV')

while True:
    print("\nNejaušo datu ģenerators:")
    print("1. 5 personu vārdi un uzvārdi")
    print("2. 5 personu vārdi un uzvārdi latviešu valodā")
    print("3. 5 persona vārdi un uzvārdi ar telefona numuru, adresi un personas kodu")
    print("5. Teksts dotā maksimāla garumā") # lietotājs ievada maksimalo garumu
    print("6. 5 Dazādas cenas") # valūtas zīme un summa
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        for _ in range(5):
            print(fake.name())
    elif choice == "2":
        for _ in range(5):
            print(fakeLV.name())
    elif choice == "3":
        for _ in range(5):
            print(f"{fake.name()}   -   {fake.phone_number()}   -   {fake.address()}   -  {fake.ssn()}")
            print('')
    elif choice == "4":
        pass
    elif choice == "5":
        length = int(input("Text length: "))
        print(fake.text(length))
    elif choice == "6":
        for _ in range(5):
            print(fake.pricetag())
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")