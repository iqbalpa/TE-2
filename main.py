from data import save_data, load_data
from greedy import set_cover
from bnb import BB
import time
import tracemalloc as trace

# Function to run greedy algorithm
def run_greedy(U, S, C):
    print(">>> GREEDY")
    trace.start()
    start = time.time()
    cover, total_cost = set_cover(U, S, C)
    end = time.time()
    _, peak = trace.get_traced_memory()
    trace.stop()
    # print(f'covering sets:\n{cover}')
    print(f'cost: {total_cost}')
    print(f'time: {end-start}')
    print(f'memory: {peak}')

# Function to run branch and bound algorithm
def run_bb(U, S, C):
    print(">>> BRANCH & BOUND")
    trace.start()
    start = time.time()
    X =(BB(U, S, C))
    cost = X[0]
    sets = X[1]
    cover = []
    for x in range(len(sets)):
        if sets[x]==1:
            cover.append(S[x])
    end = time.time()
    _, peak = trace.get_traced_memory()
    trace.stop()
    # print(f'covering sets:\n{cover}')
    print(f'cost: {cost}')
    print(f'time: {end-start}')
    print(f'memory: {peak}')
    print()

# Function to compare both algorithm
def run_algo(U, S, C):
    run_greedy(U, S, C)
    run_bb(U, S, C)

if __name__ == '__main__':
    # # Save Data
    # save_data()

    # Load Data
    U_kecil, S_kecil, C_kecil = load_data("data/data_kecil.pickle")
    U_sedang, S_sedang, C_sedang = load_data("data/data_sedang.pickle")
    U_besar, S_besar, C_besar = load_data("data/data_besar.pickle")
    # print("Data Kecil")
    # print(f'U: {U_kecil}')
    # print(f'S: {S_kecil}')
    # print(f'C: {C_kecil}')

    # Run Algorithm
    print("=== DATA KECIL ===")
    run_algo(U_kecil, S_kecil, C_kecil)
    print("=== DATA SEDANG ===")
    run_algo(U_sedang, S_sedang, C_sedang)
    print("=== DATA BESAR ===")
    run_algo(U_besar, S_besar, C_besar)