list1: list[str] = ['maratonaicpc', 'maraton', 'programacao', 'progress', 'inputs']
list2: list[str] = ['marat', 'programacao', 'outputs']

for test in list2:
    count: int = 0
    count2: int = 0
    for result in list1:
        if test == result[:len(test)]:
            count += 1
            
            if count2 < len(result):
                count2 = len(result)

    if count == 0:
        print('-1')
    else:
        print(f'{count} {count2}')