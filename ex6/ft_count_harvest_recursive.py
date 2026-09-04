def ft_recursive(i, days):
    print('Day ', i)
    if i in range(1, days):
        ft_recursive(i + 1, days)
    else:
        print('Harvest time!')

def ft_count_harvest_recursive():
    days = int(input('Days until harvest: '))
    ft_recursive(1, days)
