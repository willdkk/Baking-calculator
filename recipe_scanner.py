import cv2
import pytesseract
import re
import fractions

class RecipeScanner:
    def __init__(self, preferred_system='metric'):
        self.recognized_ingredients = []
        self.set_preferred_system(preferred_system)

    def set_preferred_system(self, system):
        self.preferred_system = system
        self.supported_units = {
            'g': 'grams', 'gram': 'grams', 'grams': 'grams',
            'kg': 'kilograms', 'kilogram': 'kilograms', 'kilograms': 'kilograms',
            'oz': 'ounces', 'ounce': 'ounces', 'ounces': 'ounces',
            'lb': 'pounds', 'pound': 'pounds', 'pounds': 'pounds',
            'ml': 'milliliters', 'milliliter': 'milliliters', 'milliliters': 'milliliters',
            'l': 'liters', 'liter': 'liters', 'liters': 'liters',
            'tsp': 'teaspoons', 'teaspoon': 'teaspoons', 'teaspoons': 'teaspoons',
            'tbsp': 'tablespoons', 'tablespoon': 'tablespoons', 'tablespoons': 'tablespoons',
            'cup': 'cups', 'cups': 'cups'
        }

        self.conversion_table = {
            ('grams', 'ounces'): lambda g: g / 28.35,
            ('kilograms', 'pounds'): lambda kg: kg * 2.20462,
            ('milliliters', 'ounces'): lambda ml: ml / 29.57,
            ('liters', 'cups'): lambda l: l * 4.22675,
            ('ounces', 'grams'): lambda oz: oz * 28.35,
            ('pounds', 'kilograms'): lambda lb: lb / 2.20462,
            ('ounces', 'milliliters'): lambda oz: oz * 29.57,
            ('cups', 'liters'): lambda c: c / 4.22675,
        }

    def scan_image(self, image_path):
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
        return text

    def parse_fraction(self, text):
        unicode_fractions = {
            '½': '1/2', '¼': '1/4', '¾': '3/4', '⅓': '1/3', '⅔': '2/3',
            '⅛': '1/8', '⅜': '3/8', '⅝': '5/8', '⅞': '7/8'
        }
        for uni, frac in unicode_fractions.items():
            text = text.replace(uni, frac)
        return text

    def parse_ingredients(self, ocr_text):
        lines = ocr_text.split('\\n')
        ingredients = []

        for line in lines:
            line = self.parse_fraction(line.strip())
            parts = line.split()
            if not parts:
                continue

            try:
                if '/' in parts[0]:
                    quantity = float(fractions.Fraction(parts[0]))
                    unit = parts[1] if len(parts) > 2 else ''
                    name = ' '.join(parts[2:]) if len(parts) > 2 else ' '.join(parts[1:])
                elif len(parts) > 1 and '/' in parts[1]:
                    whole = float(parts[0])
                    frac = float(fractions.Fraction(parts[1]))
                    quantity = whole + frac
                    unit = parts[2] if len(parts) > 3 else ''
                    name = ' '.join(parts[3:]) if len(parts) > 3 else ' '.join(parts[2:])
                else:
                    quantity = float(parts[0])
                    unit = parts[1] if len(parts) > 2 else ''
                    name = ' '.join(parts[2:]) if len(parts) > 2 else ' '.join(parts[1:])

                std_unit = self.supported_units.get(unit.lower(), unit)
                ingredients.append({"name": name, "quantity": quantity, "unit": std_unit})

            except:
                continue

        self.recognized_ingredients = ingredients
        return ingredients

    def convert_units(self):
        for ing in self.recognized_ingredients:
            unit = ing['unit']
            quantity = ing['quantity']

            if self.preferred_system == 'metric':
                for (from_unit, to_unit), func in self.conversion_table.items():
                    if unit == from_unit and 'gram' in to_unit or 'liter' in to_unit:
                        ing['quantity'] = round(func(quantity), 2)
                        ing['unit'] = to_unit
                        break
            elif self.preferred_system == 'imperial':
                for (from_unit, to_unit), func in self.conversion_table.items():
                    if unit == from_unit and ('ounce' in to_unit or 'cup' in to_unit):
                        ing['quantity'] = round(func(quantity), 2)
                        ing['unit'] = to_unit
                        break

    def scale_recipe(self, factor):
        for ing in self.recognized_ingredients:
            ing['quantity'] *= factor
