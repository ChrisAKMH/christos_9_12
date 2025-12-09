# class Akeraios:
#     __count = 0

#     def __init__(self, x = 0):
#         self.x = x
#         Akeraios.__count += 1
#         print(">>> Ένα αντικείμενο akeraios καταστράφηκε.")
#     def __del__(self):
#         Akeraios.__count -= 1
#         print(">>> Ένα αντικείμενο akeraios καταστράφηκε.")
#     def SetData(self, x):
#         self.x = x
#     def getData(self):
#         return self.x
    
#     def Ekthetis(self, e):
#         ekthetis = self.x**e
#         print(f"O ekthetis tou {self.x} einai {ekthetis}")
    
#     # def printCount(self):
#     #     print("To plithos twn antikeimenwn einai ", self.count)
#     @staticmethod
#     def getCount():
#         return Akeraios.__count

#     # def AddObject():
#     #     Akeraios.__count += 1
#     # def DeleteObject(self):
#     #     Akeraios.__count -= 1

# v1 = Akeraios(5)
# v1 = Akeraios(10)
# print("safhsdjk")

# # del v1
# # print(Akeraios.getCount)

class akeraios:
    # ιδιωτική μεταβλητή-μέλος για το πλήθος των αντικειμένων
    __count = 0

    # ---- Constructor ----
    def __init__(self, value=0):
        self.value = value       # μοναδικό property
        akeraios.__count += 1    # αυξάνει πλήθος αντικειμένων
        print(">>> Δημιουργήθηκε νέο αντικείμενο akeraios!")

    # ---- Destructor ----
    def __del__(self):
        akeraios.__count -= 1    # μειώνει το πλήθος αντικειμένων
        print(">>> Ένα αντικείμενο akeraios καταστράφηκε.")

    # ---- Συναρτήσεις-μέλη για το property ----
    def setValue(self, v):
        self.value = v

    def getValue(self):
        return self.value

    def printValue(self):
        print(f"Τιμή μεταβλητής: {self.value}")

    # ---- Συναρτήση που επιστρέφει το πλήθος αντικειμένων ----
    @staticmethod
    def getCount():
        return akeraios.__count

    # ---- Συνάρτηση υπολογισμού δύναμης ----
    def power(self, e):
        return self.value ** e


# ===== Κύριο πρόγραμμα για δοκιμή =====
a1 = akeraios(3)
a1.printValue()
print("Πλήθος αντικειμένων:", akeraios.getCount())

a2 = akeraios(5)
print("Πλήθος αντικειμένων:", akeraios.getCount())

print("3^4 =", a1.power(4))

del a1
print("Πλήθος αντικειμένων:", akeraios.getCount())

del a2
print("Τελικό πλήθος αντικειμένων:", akeraios.getCount())

