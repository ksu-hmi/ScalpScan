# /ScalpScanProject/
# ├── alopecia_types.py
# └── main.py

class AlopeciaType:
    def __init__(self, name, description, is_scarring):
        self.name = name
        self.description = description
        self.is_scarring = is_scarring

    def info(self):
        return f"{self.name}:\n- Description: {self.description}\n- Scarring: {'Yes' if self.is_scarring else 'No'}\n"

alopecia_areata = AlopeciaType(
    "Alopecia Areata",
    "An autoimmune condition causing sudden, patchy hair loss.",
    False
)

androgenetic_alopecia = AlopeciaType(
    "Androgenetic Alopecia",
    "Genetic hair loss often known as male or female pattern baldness.",
    False
)

ccca = AlopeciaType(
    "Central Centrifugal Cicatricial Alopecia (CCCA)",
    "A scarring alopecia primarily affecting women of African descent.",
    True
)

traction_alopecia = AlopeciaType(
    "Traction Alopecia",
    "Hair loss caused by repeated tension from tight hairstyles.",
    True  # Sometimes scarring
)

telogen_effluvium = AlopeciaType(
    "Telogen Effluvium",
    "Temporary hair shedding due to stress, illness, or hormonal changes.",
    False
)

alopecia_list = [
    alopecia_areata,
    androgenetic_alopecia,
    ccca,
    traction_alopecia,
    telogen_effluvium
]
