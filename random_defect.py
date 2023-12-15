import random
import json

c_amount = random.randint(1, 5)
f_amount = random.randint(1, 5)
cosmetic_defects = []
functional_defects = []
defect_bank = { #Defect Bank
    "Cosmetic Defects": [
      { "defect": "Scratching, light", "weight": 0.15 },
      { "defect": "Scratching, medium", "weight": 0.25 },
      { "defect": "Scratching, heavy", "weight": 0.5 },
      { "defect": "Dent, small", "weight": 0.25 },
      { "defect": "Dent, large", "weight": 0.35 },
      { "defect": "Dents, multiple", "weight": 0.5 },
      { "defect": "Missing key", "weight": 0.25 },
      { "defect": "Missing keys", "weight": 0.5 },
      { "defect": "Keys worn", "weight": 0.15 },
      { "defect": "Crack, bezel", "weight": 0.15 },
      { "defect": "Crack, chassis", "weight": 0.2 },
      { "defect": "Chip in chassis, small", "weight": 0.25 },
      { "defect": "Chip in chassis, large", "weight": 0.5 },
      { "defect": "Screen scratch, small", "weight": 0.25 },
      { "defect": "Screen scratch, large", "weight": 0.5 },
      { "defect": "Key marks on screen (light)", "weight": 0.15 },
      { "defect": "Key marks on screen (heavy)", "weight": 0.35 },
      { "defect": "Paint wear, light", "weight": 0.2 },
      { "defect": "Paint wear, heavy", "weight": 0.35 },
      { "defect": "Foot missing", "weight": 0.2 },
      { "defect": "Foot missing, multiple", "weight": 0.35 }
    ],
    "Functional Defects": [
      { "defect": "Microphone fail", "weight": 0.25 },
      { "defect": "Webcam fail", "weight": 0.25 },
      { "defect": "Speaker fail (single channel)", "weight": 0.25 },
      { "defect": "Speaker fail (both channels)", "weight": 0.5 },
      { "defect": "USB fail", "weight": 0.25 },
      { "defect": "USB fail (multiple)", "weight": 1 },
      { "defect": "CPU, Mobo, RAM fail", "weight": 1 },
      { "defect": "Dead pixel", "weight": 0.25 },
      { "defect": "Dead pixels, few (2-3)", "weight": 0.35 },
      { "defect": "Dead pixels, many (4-5)", "weight": 0.5 },
      { "defect": "Dead pixels, excessive", "weight": 1 },
      { "defect": "Battery fail (<60%)", "weight": 0.25 },
      { "defect": "Battery needs replacement (0%)", "weight": 0.5 },
      { "defect": "Battery missing", "weight": 0.35 },
      { "defect": "Keyboard fail, single key", "weight": 0.25 },
      { "defect": "Keyboard fail, multiple keys (=2)", "weight": 0.5 },
      { "defect": "Touchpad fail, buttons", "weight": 0.5 },
      { "defect": "Touchpad fail, tracking", "weight": 0.5 },
      { "defect": "Port damaged, power", "weight": 0.5 },
      { "defect": "Port damaged, video", "weight": 0.25 },
      { "defect": "Backlight issue", "weight": 0.25 }
    ]
}

def choose_random_defects():
    for defect in defect_bank:
        if len(cosmetic_defects) < c_amount:
            add_cdefect = random.choice(defect_bank["Cosmetic Defects"])
            cosmetic_defects.append(add_cdefect['defect'])
        if len(functional_defects) < f_amount:
            add_fdefect = random.choice(defect_bank["Functional Defects"])
            functional_defects.append(add_fdefect['defect'])

choose_random_defects()
print(cosmetic_defects)
print(functional_defects)
