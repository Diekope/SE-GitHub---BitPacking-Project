from bit_pack import *

"""
============
 Le Factory
============
"""
def create_bit_packer(compressor_num):
    if compressor_num == 'v1':
        return BitPacking_v1
    elif compressor_num == 'v2':
        return BitPacking_v2
    else:
        print("Choix incorrect, veuillez réessayer")
    

"""
===========
 Les tests
===========
"""
liste_a = [Number(1),Number(2),Number(3),Number(4)]
liste_b = [Number(1),Number(5),Number(11),Number(4),Number(8),Number(50)]

def test(liste=liste_b):
    indice = int(input(f"Donnez un indice pour la fonction 'Get' (max {len(liste)-1}): "))
    if indice > len(liste)-1:
        while not(indice) or indice > len(liste)-1:
            print("Mauvais choix")
            indice = int(input("Donnez un indice pour la fonction 'Get': "))

    max_len = int(input(f"Donnez une longueur de nombre compressé max : "))

    # BitPacking V1
    print("===============\n BitPacking V1\n===============")
    V1 = create_bit_packer('v1')
    V1 = V1(liste, max_len)
    print("- Compression")
    bin_list, bin_num = V1.compress()
    print(f"Liste nombre binaires : {bin_list}\nNombre binaire final : {bin_num}")
    print("- Get")
    get_num = V1.get(indice)
    print(f"Nombre get : {get_num}")
    print("- Decompress")
    int_list = V1.decompress()
    print(f"Liste décompressée : {int_list}")

    # BitPacking V2
    print("\n===============\n BitPacking V2\n===============")
    V2 = create_bit_packer('v2')
    V2 = V2(liste, max_len)
    print("- Compression")
    bin_list, bin_num = V2.compress()
    print(f"Liste nombre binaires : {bin_list}\nNombre binaire final : {bin_num}")
    print("- Get")
    get_num = V2.get(indice)
    print(f"Nombre get : {get_num}")
    print("- Decompress")
    int_list = V2.decompress()
    print(f"Liste décompressée : {int_list}")


"""
La fonction pour lancer les tests
On peut créer une liste de Number si voulu et la mettre en paramètre
"""
# test()