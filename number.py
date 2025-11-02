class Number:
    def __init__(self,value):
        self.value = value
    
    def convert_to_binary(self):
        temp_value = self.value
        bin_num = 0
        indice = 0
        while (temp_value != 0):
            temp_num = temp_value%2
            bin_num += temp_num*(10**indice)
            temp_value = temp_value//2
            indice+=1
        return bin_num, indice


def convert_to_int(num):
    int_num = 0
    indice = 0
    while(num != 0):
        temp_num = num%10
        int_num += temp_num*(2**indice)
        num = num//10
        indice+=1
    return int_num