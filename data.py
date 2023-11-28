import random as rand
import pickle

def get_data(size) -> (set, list, list):
    U = set(range(1, size+1))
    S = []
    covered = set()
    while len(S)<=50 or covered != U:  
        temp = set(rand.sample(U, rand.randint(1, size)))
        S.append(temp)
        covered.update(temp)
    C = [rand.randint(1, 100) for _ in range(len(S))]
    return U, S, C
# def get_data(size) -> (set, list, list):
#     U = set(range(1, size+1))
#     S = []
#     for i in range(size):
#         # temp must be the subset of U
#         temp = set(rand.sample(U, rand.randint(1, size)))
#         S.append(temp)
#     C = []
#     for i in range(size):
#         C.append(rand.randint(1, 100))
#     return U, S, C

# Load Data
def load_data(fname: str):
    with open(fname, "rb") as f:
        return pickle.load(f)

# Save Data
def save_data():
    # Data Kecil
    U_kecil, S_kecil, C_kecil = get_data(20)
    # Data Sedang
    U_sedang, S_sedang, C_sedang = get_data(200)
    # Data Besar
    U_besar, S_besar, C_besar = get_data(2000)
    # Dump Data into pickle
    with open("data/data_kecil.pickle", "wb") as f:
        pickle.dump((U_kecil, S_kecil, C_kecil), f)
    with open("data/data_sedang.pickle", "wb") as f:
        pickle.dump((U_sedang, S_sedang, C_sedang), f)
    with open("data/data_besar.pickle", "wb") as f:
        pickle.dump((U_besar, S_besar, C_besar), f)
