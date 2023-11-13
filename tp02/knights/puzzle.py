from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
# A dice "Soy tanto un caballero como un mentiroso."
knowledge0 = And(
    Biconditional(AKnight, And(AKnight, AKnave)),
    Biconditional(AKnight, Not(AKnave))
)

# Puzzle 1
# A says "We are both knaves." A dice "Ambos somos mentirosos."
# B says nothing. B no dice nada.
knowledge1 = And(
    Biconditional(AKnight, Not(AKnave)),  
    Biconditional(BKnight, Not(BKnave)),  
    Biconditional(BKnave, AKnight),
    Implication(AKnight, And(AKnave, BKnave)),
)

# Puzzle 2
# A says "We are the same kind." A dice "Somos del mismo tipo."
# B says "We are of different kinds." B dice "Somos de diferentes tipos."
knowledge2 = And(
    Biconditional(AKnight, And(AKnight, BKnight)),
    Biconditional(BKnight, Not(AKnight)),
    Implication(BKnight, AKnave)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Biconditional(AKnight, Not(AKnave)),          
    Biconditional(BKnight, Not(BKnave)),          
    Biconditional(CKnight, Not(CKnave)),        

    Or(AKnight, AKnave),                            # A says either "I am a knight." or "I am a knave."
    Biconditional(BKnave, And(AKnight, BKnight)),   # B says "A said 'I am a knave'."
    Biconditional(CKnave, BKnight),                 # B says "C is a knave."
    Biconditional(AKnave, CKnave),                  # C says "A is a knight." 
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
