def run():
    num_post = int(input('Escribe le numero de post: '))
    if num_post  >  0:
        num_act = (num_post * 2) + 4
        num_afi = int((num_act + num_post) / 5)
    else:
        print('Ingrese un numero mayor a 0')
        num_post = int(input('Escribe le numero de post: '))
        num_act = (num_post * 2) + 4
        num_afi = int((num_act + num_post) / 5)
    

    if num_afi >= 0 and num_afi <= 20:
        print(str(num_post) + ' ' + str(num_act) + ' ' + str(num_afi) +'\nuno')

    if num_afi >= 21 and num_afi <= 30:
        print(str(num_post) + ' ' + str(num_act) + ' ' + str(num_afi) +'\ndos')

    if num_afi >= 31 and num_afi <= 50:
        print(str(num_post) + ' ' + str(num_act) + ' ' + str(num_afi) +'\ntres')

    if num_afi >= 50:
        print(str(num_post) + ' ' + str(num_act) + ' ' + str(num_afi) +'\ncuatro')       

    

if __name__ == '__main__':
    run()
