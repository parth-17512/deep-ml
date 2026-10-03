def matrixmul(a: list[list[int | float]],
              b: list[list[int | float]]) -> list[list[int | float]]:

    if len(a[0]) != len(b):
        return -1

    result = []

    for i in range(len(a)):
        row = []

        for k in range(len(b[0])):
            total = 0

            for j in range(len(b)):
                total += a[i][j] * b[j][k]

            row.append(total)

        result.append(row)

    return result