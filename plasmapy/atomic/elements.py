"""
Dictionaries containing atomic data
Periodic table data from http://periodic.lanl.gov/index.shtml

"""

from astropy import units as u, constants as const

_atomic_symbols = {1: "H", 2: "He", 3: "Li", 4: "Be", 5: "B", 6: "C", 7: "N",
                   8: "O", 9: "F", 10: "Ne", 11: "Na", 12: "Mg", 13: "Al",
                   14: "Si", 15: "P", 16: "S", 17: "Cl", 18: "Ar", 19: "K",
                   20: "Ca", 21: "Sc", 22: "Ti", 23: "V", 24: "Cr", 25: "Mn",
                   26: "Fe", 27: "Co", 28: "Ni", 29: "Cu", 30: "Zn", 31: "Ga",
                   32: "Ge", 33: "As", 34: "Se", 35: "Br", 36: "Kr", 37: "Rb",
                   38: "Sr", 39: "Y", 40: "Zr", 41: "Nb", 42: "Mo", 43: "Tc",
                   44: "Ru", 45: "Rh", 46: "Pd", 47: "Ag", 48: "Cd", 49: "In",
                   50: "Sn", 51: "Sb", 52: "Te", 53: "I", 54: "Xe", 55: "Cs",
                   56: "Ba", 57: "La", 58: "Ce", 59: "Pr", 60: "Nd", 61: "Pm",
                   62: "Sm", 63: "Eu", 64: "Gd", 65: "Tb", 66: "Dy", 67: "Ho",
                   68: "Er", 69: "Tm", 70: "Yb", 71: "Lu", 72: "Hf", 73: "Ta",
                   74: "W", 75: "Re", 76: "Os", 77: "Ir", 78: "Pt", 79: "Au",
                   80: "Hg", 81: "Tl", 82: "Pb", 83: "Bi", 84: "Po", 85: "At",
                   86: "Rn", 87: "Fr", 88: "Ra", 89: "Ac", 90: "Th", 91: "Pa",
                   92: "U", 93: "Np", 94: "Pu", 95: "Am", 96: "Cm", 97: "Bk",
                   98: "Cf", 99: "Es", 100: "Fm", 101: "Md", 102: "No",
                   103: "Lr", 104: "Rf", 105: "Db", 106: "Sg", 107: "Bh",
                   108: "Hs", 109: "Mt", 110: "Ds", 111: "Rg", 112: "Cn",
                   113: "Nh", 114: "Fl", 115: "Mc", 116: "Lv", 117: "Ts",
                   118: "Og"}


_atomic_symbols_dict = {'hydrogen': "H", 'helium': "He", 'lithium': "Li",
                        'beryllium': "Be", 'boron': "B", 'carbon': "C",
                        'nitrogen': "N", 'oxygen': "O", 'fluorine': "F",
                        'neon': "Ne", 'sodium': "Na", 'magnesium': "Mg",
                        'aluminium': "Al", 'silicon': "Si", 'phosphorus': "P",
                        'sulfur': "S", 'chlorine': "Cl", 'argon': "Ar",
                        'potassium': "K", 'calcium': "Ca", 'scandium': "Sc",
                        'titanium': "Ti", 'vanadium': "V", 'chromium': "Cr",
                        'manganese': "Mn", 'iron': "Fe", 'cobalt': "Co",
                        'nickel': "Ni", 'copper': "Cu", 'zinc': "Zn",
                        'gallium': "Ga", 'germanium': "Ge", 'arsenic': "As",
                        'selenium': "Se", 'bromine': "Br", 'krypton': "Kr",
                        'rubidium': "Rb", 'strontium': "Sr", 'yttrium': "Y",
                        'zirconium': "Zr", 'niobium': "Nb", 'molybdenum': "Mo",
                        'technetium': "Tc", 'ruthenium': "Ru", 'rhodium': "Rh",
                        'palladium': "Pd", 'silver': "Ag", 'cadmium': "Cd",
                        'indium': "In", 'tin': "Sn", 'antimony': "Sb",
                        'tellurium': "Te", 'iodine': "I", 'xenon': "Xe",
                        'caesium': "Cs", 'barium': "Ba", 'lanthanum': "La",
                        'cerium': "Ce", 'praseodymium': "Pr",
                        'neodymium': "Nd", 'promethium': "Pm",
                        'samarium': "Sm", 'europium': "Eu", 'gadolinium': "Gd",
                        'terbium': "Tb", 'dysprosium': "Dy", 'holmium': "Ho",
                        'erbium': "Er", 'thulium': "Tm", 'ytterbium': "Yb",
                        'lutetium': "Lu", 'hafnium': "Hf", 'tantalum': "Ta",
                        'tungsten': "W", 'rhenium': "Re", 'osmium': "Os",
                        'iridium': "Ir", 'platinum': "Pt", 'gold': "Au",
                        'mercury': "Hg", 'thallium': "Tl", 'lead': "Pb",
                        'bismuth': "Bi", 'polonium': "Po", 'astatine': "At",
                        'radon': "Rn", 'francium': "Fr", 'radium': "Ra",
                        'actinium': "Ac", 'thorium': "Th",
                        'protactinium': "Pa", 'uranium': "U",
                        'neptunium': "Np", 'plutonium': "Pu",
                        'americium': "Am", 'curium': "Cm", 'berkelium': "Bk",
                        'californium': "Cf", 'einsteinium': "Es",
                        'fermium': "Fm", 'mendelevium': "Md", 'nobelium': "No",
                        'lawrencium': "Lr", 'rutherfordium': "Rf",
                        'dubnium': "Db", 'seaborgium': "Sg", 'bohrium': "Bh",
                        'hassium': "Hs", 'meitnerium': "Mt",
                        'darmstadtium': "Ds", 'roentgenium': "Rg",
                        'copernicium': "Cn", 'nihonium': "Nh",
                        'flerovium': "Fl", 'moscovium': "Mc",
                        'livermorium': "Lv", 'tennessine': "Ts",
                        'oganesson': "Og"}


_Elements = {
    "H": {"atomic_number": 1, "symbol": "H",
          "atomic_mass": 1.008*u.u, "name": "hydrogen", "period": 1,
          "group": 1, "block": "s", "category": "Nonmetals"},
    "He": {"atomic_number": 2, "symbol": "He",
           "atomic_mass": 4.002602*u.u, "name": "helium", "period": 1,
           "group": 18, "block": "s", "category": "Noble gases"},
    "Li": {"atomic_number": 3, "symbol": "Li",
           "atomic_mass": 6.94*u.u, "name": "lithium", "period": 2,
           "group": 1, "block": "s", "category": "Alkali metals"},
    "Be": {"atomic_number": 4, "symbol": "Be",
           "atomic_mass": 9.0121831*u.u, "name": "beryllium", "period": 2,
           "group": 2, "block": "s", "category": "Alkaline earth metals"},
    "B": {"atomic_number": 5, "symbol": "B",
          "atomic_mass": 10.806*u.u, "name": "boron", "period": 2,
          "group": 13, "block": "p", "category": "Metalloid"},
    "C": {"atomic_number": 6, "symbol": "C",
          "atomic_mass": 12.011*u.u, "name": "carbon", "period": 2,
          "group": 14, "block": "p", "category": "Nonmetals"},
    "N": {"atomic_number": 7, "symbol": "N",
          "atomic_mass": 14.007*u.u, "name": "nitrogen", "period": 2,
          "group": 15, "block": "p", "category": "Nonmetals"},
    "O": {"atomic_number": 8, "symbol": "O",
          "atomic_mass": 15.999*u.u, "name": "oxygen", "period": 2,
          "group": 16, "block": "p", "category": "Nonmetals"},
    "F": {"atomic_number": 9, "symbol": "F",
          "atomic_mass": 18.998403163*u.u, "name": "fluorine", "period": 2,
          "group": 17, "block": "p", "category": "Halogens"},
    "Ne": {"atomic_number": 10, "symbol": "Ne",
           "atomic_mass": 20.1797*u.u, "name": "neon", "period": 2,
           "group": 18, "block": "p", "category": "Noble gases"},
    "Na": {"atomic_number": 11, "symbol": "Na",
           "atomic_mass": 22.98976928*u.u, "name": "sodium", "period": 3,
           "group": 1, "block": "s", "category": "Alkali metals"},
    "Mg": {"atomic_number": 12, "symbol": "Mg",
           "atomic_mass": 24.305*u.u, "name": "magnesium", "period": 3,
           "group": 2, "block": "s", "category": "Alkaline earth metals"},
    "Al": {"atomic_number": 13, "symbol": "Al",
           "atomic_mass": 26.9815385*u.u, "name": "aluminium", "period": 3,
           "group": 13, "block": "p", "category": "Post-transition metals"},
    "Si": {"atomic_number": 14, "symbol": "Si",
           "atomic_mass": 28.085*u.u, "name": "silicon", "period": 3,
           "group": 14, "block": "p", "category": "Metalloid"},
    "P": {"atomic_number": 15, "symbol": "P",
          "atomic_mass": 30.973761998*u.u, "name": "phosphorus", "period": 3,
          "group": 15, "block": "p", "category": "Nonmetals"},
    "S": {"atomic_number": 16, "symbol": "S",
          "atomic_mass": 32.06*u.u, "name": "sulfur", "period": 3,
          "group": 16, "block": "p", "category": "Nonmetals"},
    "Cl": {"atomic_number": 17, "symbol": "Cl",
           "atomic_mass": 35.45*u.u, "name": "chlorine", "period": 3,
           "group": 17, "block": "p", "category": "Halogens"},
    "Ar": {"atomic_number": 18, "symbol": "Ar",
           "atomic_mass": 39.948*u.u, "name": "argon", "period": 3,
           "group": 18, "block": "p", "category": "Noble gases"},
    "K": {"atomic_number": 19, "symbol": "K",
          "atomic_mass": 39.0983*u.u, "name": "potassium", "period": 4,
          "group": 1, "block": "s", "category": "Alkali metals"},
    "Ca": {"atomic_number": 20, "symbol": "Ca",
           "atomic_mass": 40.078*u.u, "name": "calcium", "period": 4,
           "group": 2, "block": "s", "category": "Alkaline earth metals"},
    "Sc": {"atomic_number": 21, "symbol": "Sc",
           "atomic_mass": 44.955908*u.u, "name": "scandium", "period": 4,
           "group": 3, "block": "d", "category": "Transition metals"},
    "Ti": {"atomic_number": 22, "symbol": "Ti",
           "atomic_mass": 47.867*u.u, "name": "titanium", "period": 4,
           "group": 4, "block": "d", "category": "Transition metals"},
    "V": {"atomic_number": 23, "symbol": "V",
          "atomic_mass": 50.9415*u.u, "name": "vanadium", "period": 4,
          "group": 5, "block": "d", "category": "Transition metals"},
    "Cr": {"atomic_number": 24, "symbol": "Cr",
           "atomic_mass": 51.9961*u.u, "name": "chromium", "period": 4,
           "group": 6, "block": "d", "category": "Transition metals"},
    "Mn": {"atomic_number": 25, "symbol": "Mn",
           "atomic_mass": 54.938044*u.u, "name": "manganese", "period": 4,
           "group": 7, "block": "d", "category": "Transition metals"},
    "Fe": {"atomic_number": 26, "symbol": "Fe",
           "atomic_mass": 55.845*u.u, "name": "iron", "period": 4,
           "group": 8, "block": "d", "category": "Transition metals"},
    "Co": {"atomic_number": 27, "symbol": "Co",
           "atomic_mass": 58.933*u.u, "name": "cobalt", "period": 4,
           "group": 9, "block": "d", "category": "Transition metals"},
    "Ni": {"atomic_number": 28, "symbol": "Ni",
           "atomic_mass": 58.6934*u.u, "name": "nickel", "period": 4,
           "group": 10, "block": "d", "category": "Transition metals"},
    "Cu": {"atomic_number": 29, "symbol": "Cu",
           "atomic_mass": 63.546*u.u, "name": "copper", "period": 4,
           "group": 11, "block": "d", "category": "Transition metals"},
    "Zn": {"atomic_number": 30, "symbol": "Zn",
           "atomic_mass": 65.38*u.u, "name": "zinc", "period": 4,
           "group": 12, "block": "d", "category": "Transition metals"},
    "Ga": {"atomic_number": 31, "symbol": "Ga",
           "atomic_mass": 69.723*u.u, "name": "gallium", "period": 4,
           "group": 13, "block": "p", "category": "Post-transition metals"},
    "Ge": {"atomic_number": 32, "symbol": "Ge",
           "atomic_mass": 72.630*u.u, "name": "germanium", "period": 4,
           "group": 14, "block": "p", "category": "Metalloid"},
    "As": {"atomic_number": 33, "symbol": "As",
           "atomic_mass": 74.921595*u.u, "name": "arsenic", "period": 4,
           "group": 15, "block": "p", "category": "Metalloid"},
    "Se": {"atomic_number": 34, "symbol": "Se",
           "atomic_mass": 78.971*u.u, "name": "selenium", "period": 4,
           "group": 16, "block": "p", "category": "Nonmetals"},
    "Br": {"atomic_number": 35, "symbol": "Br",
           "atomic_mass": 79.904*u.u, "name": "bromine", "period": 4,
           "group": 17, "block": "p", "category": "Halogens"},
    "Kr": {"atomic_number": 36, "symbol": "Kr",
           "atomic_mass": 83.798*u.u, "name": "krypton", "period": 4,
           "group": 18, "block": "p", "category": "Noble gases"},
    "Rb": {"atomic_number": 37, "symbol": "Rb",
           "atomic_mass": 85.4678*u.u, "name": "rubidium", "period": 5,
           "group": 1, "block": "s", "category": "Alkali metals"},
    "Sr": {"atomic_number": 38, "symbol": "Sr",
           "atomic_mass": 87.62*u.u, "name": "strontium", "period": 5,
           "group": 2, "block": "s", "category": "Alkaline earth metals"},
    "Y": {"atomic_number": 39, "symbol": "Y",
          "atomic_mass": 88.90584*u.u, "name": "yttrium", "period": 5,
          "group": 3, "block": "d", "category": "Transition metals"},
    "Zr": {"atomic_number": 40, "symbol": "Zr",
           "atomic_mass": 91.224*u.u, "name": "zirconium", "period": 5,
           "group": 4, "block": "d", "category": "Transition metals"},
    "Nb": {"atomic_number": 41, "symbol": "Nb",
           "atomic_mass": 92.90637*u.u, "name": "niobium", "period": 5,
           "group": 5, "block": "d", "category": "Transition metals"},
    "Mo": {"atomic_number": 42, "symbol": "Mo",
           "atomic_mass": 95.95*u.u, "name": "molybdenum", "period": 5,
           "group": 6, "block": "d", "category": "Transition metals"},
    "Tc": {"atomic_number": 43, "symbol": "Tc",
           "name": "technetium", "period": 5,
           "group": 7, "block": "d", "category": "Transition metals"},
    "Ru": {"atomic_number": 44, "symbol": "Ru",
           "atomic_mass": 101.07*u.u, "name": "ruthenium", "period": 5,
           "group": 8, "block": "d", "category": "Transition metals"},
    "Rh": {"atomic_number": 45, "symbol": "Rh",
           "atomic_mass": 102.90550*u.u, "name": "rhodium", "period": 5,
           "group": 9, "block": "d", "category": "Transition metals"},
    "Pd": {"atomic_number": 46, "symbol": "Pd",
           "atomic_mass": 106.42*u.u, "name": "palladium", "period": 5,
           "group": 10, "block": "d", "category": "Transition metals"},
    "Ag": {"atomic_number": 47, "symbol": "Ag",
           "atomic_mass": 107.8682*u.u, "name": "silver", "period": 5,
           "group": 11, "block": "d", "category": "Transition metals"},
    "Cd": {"atomic_number": 48, "symbol": "Cd",
           "atomic_mass": 112.414*u.u, "name": "cadmium", "period": 5,
           "group": 12, "block": "d", "category": "Transition metals"},
    "In": {"atomic_number": 49, "symbol": "In",
           "atomic_mass": 114.818*u.u, "name": "indium", "period": 5,
           "group": 13, "block": "p", "category": "Post-transition metals"},
    "Sn": {"atomic_number": 50, "symbol": "Sn",
           "atomic_mass": 118.710*u.u, "name": "tin", "period": 5,
           "group": 14, "block": "p", "category": "Post-transition metals"},
    "Sb": {"atomic_number": 51, "symbol": "Sb",
           "atomic_mass": 121.760*u.u, "name": "antimony", "period": 5,
           "group": 15, "block": "p", "category": "Metalloid"},
    "Te": {"atomic_number": 52, "symbol": "Te",
           "atomic_mass": 127.60*u.u, "name": "tellurium", "period": 5,
           "group": 16, "block": "p", "category": "Metalloid"},
    "I": {"atomic_number": 53, "symbol": "I",
          "atomic_mass": 126.90447*u.u, "name": "iodine", "period": 5,
          "group": 17, "block": "p", "category": "Halogens"},
    "Xe": {"atomic_number": 54, "symbol": "Xe",
           "atomic_mass": 131.293*u.u, "name": "xenon", "period": 5,
           "group": 18, "block": "p", "category": "Noble gases"},
    "Cs": {"atomic_number": 55, "symbol": "Cs",
           "atomic_mass": 132.90545196*u.u, "name": "caesium", "period": 6,
           "group": 1, "block": "s", "category": "Alkali metals"},
    "Ba": {"atomic_number": 56, "symbol": "Ba",
           "atomic_mass": 137.327*u.u, "name": "barium", "period": 6,
           "group": 2, "block": "s", "category": "Alkaline earth metals"},
    "La": {"atomic_number": 57, "symbol": "La",
           "atomic_mass": 138.90547*u.u, "name": "lanthanum", "period": 6,
           "group": 3, "block": "d", "category": "Lanthanides"},
    "Ce": {"atomic_number": 58, "symbol": "Ce",
           "atomic_mass": 140.116*u.u, "name": "cerium", "period": 6,
           "group": 3, "block": "f", "category": "Lanthanides"},
    "Pr": {"atomic_number": 59, "symbol": "Pr",
           "atomic_mass": 140.90766*u.u, "name": "praseodymium", "period": 6,
           "group": 3, "block": "f", "category": "Lanthanides"},
    "Nd": {"atomic_number": 60, "symbol": "Nd",
           "atomic_mass": 144.242*u.u, "name": "neodymium", "period": 6,
           "group": 3, "block": "f", "category": "Lanthanides"},
    "Pm": {"atomic_number": 61, "symbol": "Pm",
           "name": "promethium", "period": 6,
           "group": 3, "block": "f", "category": "Lanthanides"},
    "Sm": {"atomic_number": 62, "symbol": "Sm",
           "atomic_mass": 150.36*u.u, "name": "samarium", "period": 6,
           "group": 3, "block": "f", "category": "Lanthanides"},
    "Eu": {"atomic_number": 63, "symbol": "Eu",
           "atomic_mass": 151.964*u.u, "name": "europium", "period": 6,
           "group": 3, "block": "f", "category": "Lanthanides"},
    "Gd": {"atomic_number": 64, "symbol": "Gd",
           "atomic_mass": 157.25*u.u, "name": "gadolinium", "period": 6,
           "group": 3, "block": "f", "category": "Lanthanides"},
    "Tb": {"atomic_number": 65, "symbol": "Tb",
           "atomic_mass": 158.92535*u.u, "name": "terbium", "period": 6,
           "group": 3, "block": "f", "category": "Lanthanides"},
    "Dy": {"atomic_number": 66, "symbol": "Dy",
           "atomic_mass": 162.500*u.u, "name": "dysprosium", "period": 6,
           "group": 3, "block": "f", "category": "Lanthanides"},
    "Ho": {"atomic_number": 67, "symbol": "Ho",
           "atomic_mass": 164.93033*u.u, "name": "holmium", "period": 6,
           "group": 3, "block": "f", "category": "Lanthanides"},
    "Er": {"atomic_number": 68, "symbol": "Er",
           "atomic_mass": 167.259*u.u, "name": "erbium", "period": 6,
           "group": 3, "block": "f", "category": "Lanthanides"},
    "Tm": {"atomic_number": 69, "symbol": "Tm",
           "atomic_mass": 168.93422*u.u, "name": "thulium", "period": 6,
           "group": 3, "block": "f", "category": "Lanthanides"},
    "Yb": {"atomic_number": 70, "symbol": "Yb",
           "atomic_mass": 173.045*u.u, "name": "ytterbium", "period": 6,
           "group": 3, "block": "f", "category": "Lanthanides"},
    "Lu": {"atomic_number": 71, "symbol": "Lu",
           "atomic_mass": 174.9668*u.u, "name": "lutetium", "period": 6,
           "group": 3, "block": "f", "category": "Lanthanides"},
    "Hf": {"atomic_number": 72, "symbol": "Hf",
           "atomic_mass": 178.49*u.u, "name": "hafnium", "period": 6,
           "group": 4, "block": "d", "category": "Transition metals"},
    "Ta": {"atomic_number": 73, "symbol": "Ta",
           "atomic_mass": 180.94788*u.u, "name": "tantalum", "period": 6,
           "group": 5, "block": "d", "category": "Transition metals"},
    "W": {"atomic_number": 74, "symbol": "W",
          "atomic_mass": 183.84*u.u, "name": "tungsten", "period": 6,
           "group": 6, "block": "d", "category": "Transition metals"},
    "Re": {"atomic_number": 75, "symbol": "Re",
           "atomic_mass": 186.207*u.u, "name": "rhenium", "period": 6,
           "group": 7, "block": "d", "category": "Transition metals"},
    "Os": {"atomic_number": 76, "symbol": "Os",
           "atomic_mass": 190.23*u.u, "name": "osmium", "period": 6,
           "group": 8, "block": "d", "category": "Transition metals"},
    "Ir": {"atomic_number": 77, "symbol": "Ir",
           "atomic_mass": 192.217*u.u, "name": "iridium", "period": 6,
           "group": 9, "block": "d", "category": "Transition metals"},
    "Pt": {"atomic_number": 78, "symbol": "Pt",
           "atomic_mass": 195.084*u.u, "name": "platinum", "period": 6,
           "group": 10, "block": "d", "category": "Transition metals"},
    "Au": {"atomic_number": 79, "symbol": "Au",
           "atomic_mass": 196.966569*u.u, "name": "gold", "period": 6,
           "group": 11, "block": "d", "category": "Transition metals"},
    "Hg": {"atomic_number": 80, "symbol": "Hg",
           "atomic_mass": 200.592*u.u, "name": "mercury", "period": 6,
           "group": 12, "block": "d", "category": "Transition metals"},
    "Tl": {"atomic_number": 81, "symbol": "Tl",
           "atomic_mass": 204.38*u.u, "name": "thallium", "period": 6,
           "group": 13, "block": "p", "category": "Post-transition metals"},
    "Pb": {"atomic_number": 82, "symbol": "Pb",
           "atomic_mass": 207.2*u.u, "name": "lead", "period": 6,
           "group": 14, "block": "p", "category": "Post-transition metals"},
    "Bi": {"atomic_number": 83, "symbol": "Bi",
           "atomic_mass": 208.98040*u.u, "name": "bismuth", "period": 6,
           "group": 15, "block": "p", "category": "Post-transition metals"},
    "Po": {"atomic_number": 84, "symbol": "Po",
           "name": "polonium", "period": 6,
           "group": 16, "block": "p", "category": "Metalloid"},
    "At": {"atomic_number": 85, "symbol": "At",
           "name": "astatine", "period": 6,
           "group": 17, "block": "p", "category": "Halogens"},
    "Rn": {"atomic_number": 86, "symbol": "Rn",
           "name": "radon", "period": 6,
           "group": 18, "block": "p", "category": "Noble gases"},
    "Fr": {"atomic_number": 87, "symbol": "Fr",
           "name": "francium", "period": 7,
           "group": 1, "block": "s", "category": "Alkali metals"},
    "Ra": {"atomic_number": 88, "symbol": "Ra",
           "name": "radium", "period": 7,
           "group": 2, "block": "s", "category": "Alkaline earth metals"},
    "Ac": {"atomic_number": 89, "symbol": "Ac",
           "name": "actinium", "period": 7,
           "group": 3, "block": "d", "category": "Actinides"},
    "Th": {"atomic_number": 90, "symbol": "Th",
           "atomic_mass": 232.0377*u.u, "name": "thorium", "period": 7,
           "group": 3, "block": "f", "category": "Actinides"},
    "Pa": {"atomic_number": 91, "symbol": "Pa",
           "atomic_mass": 231.03588*u.u, "name": "protactinium", "period": 7,
           "group": 3, "block": "f", "category": "Actinides"},
    "U": {"atomic_number": 92, "symbol": "U",
          "atomic_mass": 238.02891*u.u, "name": "uranium", "period": 7,
           "group": 3, "block": "f", "category": "Actinides"},
    "Np": {"atomic_number": 93, "symbol": "Np",
           "name": "neptunium", "period": 7,
           "group": 3, "block": "f", "category": "Actinides"},
    "Pu": {"atomic_number": 94, "symbol": "Pu",
           "name": "plutonium", "period": 7,
           "group": 3, "block": "f", "category": "Actinides"},
    "Am": {"atomic_number": 95, "symbol": "Am",
           "name": "americium", "period": 7,
           "group": 3, "block": "f", "category": "Actinides"},
    "Cm": {"atomic_number": 96, "symbol": "Cm",
           "name": "curium", "period": 7,
           "group": 3, "block": "f", "category": "Actinides"},
    "Bk": {"atomic_number": 97, "symbol": "Bk",
           "name": "berkelium", "period": 7,
           "group": 3, "block": "f", "category": "Actinides"},
    "Cf": {"atomic_number": 98, "symbol": "Cf",
           "name": "californium", "period": 7,
           "group": 3, "block": "f", "category": "Actinides"},
    "Es": {"atomic_number": 99, "symbol": "Es",
           "name": "einsteinium", "period": 7,
           "group": 3, "block": "f", "category": "Actinides"},
    "Fm": {"atomic_number": 100, "symbol": "Fm",
           "name": "fermium", "period": 7,
           "group": 3, "block": "f", "category": "Actinides"},
    "Md": {"atomic_number": 101, "symbol": "Md",
           "name": "mendelevium", "period": 7,
           "group": 3, "block": "f", "category": "Actinides"},
    "No": {"atomic_number": 102, "symbol": "No",
           "name": "nobelium", "period": 7,
           "group": 3, "block": "f", "category": "Actinides"},
    "Lr": {"atomic_number": 103, "symbol": "Lr",
           "name": "lawrencium", "period": 7,
           "group": 3, "block": "f", "category": "Actinides"},
    "Rf": {"atomic_number": 104, "symbol": "Rf",
           "name": "rutherfordium", "period": 7,
           "group": 4, "block": "d", "category": "Transition metals"},
    "Db": {"atomic_number": 105, "symbol": "Db",
           "name": "dubnium", "period": 7,
           "group": 5, "block": "d", "category": "Transition metals"},
    "Sg": {"atomic_number": 106, "symbol": "Sg",
           "name": "seaborgium", "period": 7,
           "group": 6, "block": "d", "category": "Transition metals"},
    "Bh": {"atomic_number": 107, "symbol": "Bh",
           "name": "bohrium", "period": 7,
           "group": 7, "block": "d", "category": "Transition metals"},
    "Hs": {"atomic_number": 108, "symbol": "Hs",
           "name": "hassium", "period": 7,
           "group": 8, "block": "d", "category": "Transition metals"},
    "Mt": {"atomic_number": 109, "symbol": "Mt",
           "name": "meitnerium", "period": 7,
           "group": 9, "block": "d", "category": "Transition metals"},
    "Ds": {"atomic_number": 110, "symbol": "Ds",
           "name": "darmstadtium", "period": 7,
           "group": 10, "block": "d", "category": "Transition metals"},
    "Rg": {"atomic_number": 111, "symbol": "Rg",
           "name": "roentgenium", "period": 7,
           "group": 11, "block": "d", "category": "Transition metals"},
    "Cn": {"atomic_number": 112, "symbol": "Cn",
           "name": "copernicium", "period": 7,
           "group": 12, "block": "d", "category": "Transition metals"},
    "Nh": {"atomic_number": 113, "symbol": "Nh",
           "name": "nihonium", "period": 7,
           "group": 13, "block": "p", "category": "Post-transition metals"},
    "Fl": {"atomic_number": 114, "symbol": "Fl",
           "name": "flerovium", "period": 7,
           "group": 14, "block": "p", "category": "Post-transition metals"},
    "Mc": {"atomic_number": 115, "symbol": "Mc",
           "name": "moscovium", "period": 7,
           "group": 15, "block": "p", "category": "Post-transition metals"},
    "Lv": {"atomic_number": 116, "symbol": "Lv",
           "name": "livermorium", "period": 7,
           "group": 16, "block": "p", "category": "Post-transition metals"},
    "Ts": {"atomic_number": 117, "symbol": "Ts",
           "name": "tennessine", "period": 7,
           "group": 17, "block": "p", "category": "Halogens"},
    "Og": {"atomic_number": 118, "symbol": "Og",
           "name": "oganesson", "period": 7,
           "group": 18, "block": "p", "category": "Noble gases"},
    }
