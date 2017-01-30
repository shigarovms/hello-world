n = int(input('Какое число нужно перевести в римскую запись?'))

def convert_to_roman(data):
    
    roman = ''
    
    all_rom = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    #           0    1    2    3    4    5    6
    
    # Создадим массив состоящий из цифр нашего числа
    
    data_array = []
    u_data = data
    dec_num = [1000, 100, 10, 1]
    
    for i in range(4):
        res = u_data // dec_num[i]
        data_array.append(res)
        u_data = u_data % dec_num[i]
    #print (data_array)
    
    # В римской записи комбинации букв строго соответствуют арабской цифре. Поэтому:
    # Создадим функцию для замены арабской цифры на комбинацию римских букв.
    
    def rrlet(q, n):
        let = ''

        if q <=3:
            let = ('%s' % all_rom[n])*q
        elif q == 4:
            let = '%s' % all_rom[n] + '%s' % all_rom[n-1]
            # В условии data < 3999, поэтому нам не страшен отрицательный индекс массива all_rom, который получился бы при data >= 4000
        elif q > 4 and q < 9:
            let = '%s' % all_rom[n-1] + ('%s' % all_rom[n])*(q-5)
        elif q == 9:
            let = '%s' % all_rom[n] + '%s' % all_rom[n-2]
        
        return let
        
    # Вызовем эту функцию для каждой нашей цифры и запишем результат в строку roman последовательно
    
    for i in range(4):
            roman += rrlet(data_array[i], 2*i)
        
    # Эта строка и является римской записью нашего числа
    
    return roman

print (convert_to_roman(n))
