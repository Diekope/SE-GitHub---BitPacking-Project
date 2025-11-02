import time
import random
from number import Number
from main import create_bit_packer

def run_detailed_benchmark(compressor_class, data, max_length, repetitions=100):
    """
    Runs a detailed and accurate benchmark for a given class and data,
    measuring each operation separately over a number of repetitions.
    """
    # On utilise une copie pour éviter de modifier la liste originale (pour V2)
    data_copy = data.copy()

    # 2. Benchmark Compression
    compressors = [compressor_class(data_copy, max_length) for _ in range(repetitions)]
    start_time = time.perf_counter()
    for c in compressors:
        c.compress()
    end_time = time.perf_counter()
    compress_time = (end_time - start_time) / repetitions

    # 3. Benchmark Décompression
    compressors = [compressor_class(data_copy, max_length) for _ in range(repetitions)]
    for c in compressors:
        c.compress()
    start_time = time.perf_counter()
    for c in compressors:
        c.decompress()
    end_time = time.perf_counter()
    decompress_time = (end_time - start_time) / repetitions

    # 4. Benchmark Get
    compressor = compressor_class(data_copy, max_length)
    comp = compressor.compress()
    get_time = 0
    if len(data_copy) > 0:
        get_index = random.randint(0, len(comp) - 1)
        start_time = time.perf_counter()
        for _ in range(repetitions):
            compressor.get(get_index)
        end_time = time.perf_counter()
        get_time = (end_time - start_time) / repetitions

    return {
        "compress": compress_time,
        "decompress": decompress_time,
        "get": get_time,
    }

def compare_packing_methods_final():
    """
    Generates 5 different datasets and compares the performance of
    BitPacking_v1 and BitPacking_v2 on each, for several max_length values.
    """
    print("="*70)
    print("  Démarrage du Benchmark Final Détaillé des Méthodes de BitPacking")
    print("="*70)

    datasets = {
        "1. Petite liste, petits nombres (1-50)": [Number(random.randint(1, 50)) for _ in range(100)],
        "2. Grande liste, petits nombres (1-50)": [Number(random.randint(1, 50)) for _ in range(1000)],
        "3. Petite liste, grands nombres (1-1000)": [Number(random.randint(1, 1000)) for _ in range(100)],
        "4. Grande liste, grands nombres (1-1000)": [Number(random.randint(1, 1000)) for _ in range(1000)],
        "5. Liste moyenne, très grands nombres (1-10000)": [Number(random.randint(1, 10000)) for _ in range(500)],
    }

    packer_v1_class = create_bit_packer('v1')
    packer_v2_class = create_bit_packer('v2')
    
    test_max_lengths = [8, 16, 32]
    repetitions = 100

    for max_len in test_max_lengths:
        print(f"\n\n{'='*25} Test avec max_length = {max_len} {'='*25}")

        for name, data in datasets.items():
            print(f"\n--- Jeu de données : {name} ---")
            print(f"(Taille: {len(data)} nombres, Répétitions: {repetitions})" )
            
            for version, packer_class in [('v1', packer_v1_class), ('v2', packer_v2_class)]:
                results = run_detailed_benchmark(packer_class, data, max_len, repetitions)
                
                print(f"  - BitPacking_{version}:")
                if isinstance(results, str):
                    print(f"    {results}")
                else:
                    print(f"    - Temps compress:   {results['compress'] * 1e6:.2f} µs")
                    print(f"    - Temps decompress: {results['decompress'] * 1e6:.2f} µs")
                    print(f"    - Temps get:        {results['get'] * 1e6:.2f} µs")

    print("\n" + "="*70)
    print("Fin du benchmark")
    print("="*70)

compare_packing_methods_final()
