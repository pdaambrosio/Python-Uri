list1: list[str] = ['maratonaicpc', 'maraton', 'programacao', 'progress', 'inputs']
list2: list[str] = ['marat', 'programacao', 'outputs']

for result in list1:
    for test in list2:
        if test == result[:len(test)]:
            print(result)
            break
