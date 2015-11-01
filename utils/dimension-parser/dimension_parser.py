with open('dimension.txt', 'r') as input_file:
    with open('output_dimension.txt', 'w') as output_file:
        for line in input_file:
            dimensions = line.strip().split('x')
            width = dimensions[0]
            height = dimensions[1]
            output_file.write(
                'size' + width + 'x' + height +
                '(' + width + ', ' + height + '),\n')

