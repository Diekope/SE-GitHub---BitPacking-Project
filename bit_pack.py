from number import *
"""
La v1
"""
class BitPacking_v1:
    def __init__(self,number_list, max_length):
        self.number_list = number_list

        self.id_list = []
        self.compressed_numbers = []
        self.decompressed_numbers = []

        self.max_length = max_length

        self.compressed_number = ""

    def compress(self):
        temp_max_length = self.max_length

        for number in self.number_list:
            bin_number, number_id = number.convert_to_binary()
            if len(str(bin_number)) > self.max_length:
                print(f"Le nombre {number.value} - {bin_number} dépasse la taille maximum d'un entier ({self.max_length}), il sera donc ignoré")
                pass
            else:
                self.compressed_numbers.append(bin_number)
                self.id_list.append(number_id)

        temp_max_length = self.max_length

        for binary_number in self.compressed_numbers:
            if len(str(binary_number)) <= temp_max_length:
                self.compressed_number = self.compressed_number + str(binary_number)
                temp_max_length -= len(str(binary_number))
            else:
                while temp_max_length > 0:
                    self.compressed_number += '0'
                    temp_max_length -= 1
                self.compressed_number += ' '
                temp_max_length = self.max_length

                self.compressed_number += str(binary_number)
                temp_max_length -= len(str(binary_number))
        return self.compressed_numbers, self.compressed_number
    
    def decompress(self):
        for binary_number in self.compressed_numbers:
            int_value = convert_to_int(binary_number)
            self.decompressed_numbers.append(int_value)
        return self.decompressed_numbers

    def get(self,indice):
        return convert_to_int(self.compressed_numbers[indice])


"""
La v2
"""

class BitPacking_v2:
    def __init__(self, number_list, max_length):
        self.number_list = number_list
        
        self.max_length = max_length
        self.id_list = []

        self.bin_numbers = []
        
        self.bin_number = ""
        

    def compress(self):
        valid_numbers = []
        for number in self.number_list:
            _, bin_size = number.convert_to_binary()
            if bin_size > self.max_length:
                print(f"Le nombre {number.value} (taille: {bin_size}) dépasse la taille maximum d'une piste ({self.max_length}), il sera donc ignoré")
                pass
            else:
                valid_numbers.append(number)
        self.number_list = valid_numbers

        temp_length_list = [self.max_length]
        count_per_track = [0]

        for number in self.number_list:
            bin_number, bin_size = number.convert_to_binary()
            placed = False

            for i in range(len(temp_length_list)):
                if bin_size <= temp_length_list[i]:
                    temp_length_list[i] -= bin_size
                    count_per_track[i] += 1
                    self.id_list.append([i, count_per_track[i] - 1])
                    placed = True
                    break

            if not placed:
                temp_length_list.append(self.max_length - bin_size)
                count_per_track.append(1)
                self.id_list.append([len(temp_length_list) - 1, 0])

        self.bin_numbers = [[] for _ in range(len(temp_length_list))]

        for idx, number in enumerate(self.number_list):
            bin_number, _ = number.convert_to_binary()
            track_id, _ = self.id_list[idx]
            self.bin_numbers[track_id].append(bin_number)

        self.bin_number = ""
        for bin_num in self.bin_numbers:
            for j in bin_num:
                self.bin_number = self.bin_number + str(j)
            self.bin_number = self.bin_number + " "

        return self.bin_numbers, self.bin_number
    
    def decompress(self):
        decompressed = []

        for _, (track_id, _) in enumerate(self.id_list):
            bin_number = self.bin_numbers[track_id].pop(0)
            value = convert_to_int(bin_number)
            decompressed.append(value)

        return decompressed
    
    def get(self, index):
        track_id, pos = self.id_list[index]
        bin_number = self.bin_numbers[track_id][pos]
        value = convert_to_int(bin_number)
        return value
        