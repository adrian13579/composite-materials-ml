import numpy as np


def efective_properties(laminas):
    """
    Computes the 5 elastics constants of a composite laminates through homogenization
    where the laminas are elastic, isotrophic and homogeneus.
    """
    p = np.array((1, 5))
    assert sum(x[2] for x in laminas) == 1
    assert all(x[2]!=0 for x in laminas) 

    temp1 = 0
    temp2 = 0
    temp3 = 0
    for lamina in laminas:
        temp1 += lamina[2] * (lamina[0] / (1 - lamina[1] ** 2))
        temp2 += lamina[2] * (lamina[1] / (1 - lamina[1]))
        temp3 += lamina[2] * (
            (1 + lamina[1]) * (1 - 2 * lamina[1]) / (lamina[0] * (1 - lamina[1]))
        )
    p[0] = temp1 + (temp2**2) / temp3

    temp1 = 0
    temp2 = 0
    for lamina in laminas:
        temp1 += lamina[2] * (lamina[1] / (1 - lamina[1]))
        temp2 += lamina[2] * (
            (1 + lamina[1]) * (1 - 2 * lamina[1]) / (lamina[0] * (1 - lamina[1]))
        )
    p[1] = temp1 / temp2

    temp1 = 0
    for lamina in laminas:
        temp1 += lamina[2] * (1 + lamina[1]) / lamina[0]
    p[2] = 1 / (2 * temp1)

    temp1 = 0
    for lamina in laminas:
        temp1 += lamina[2] * (lamina[0] / (1 + lamina[1]))
    p[3] = 0.5 * temp1

    temp1 = 0
    for lamina in laminas:
        temp1 += lamina[2] * (
            (1 + lamina[1]) * (1 - 2 * lamina[1]) / (lamina[0] * (1 - lamina[1]))
        )

    p[4] = 1 / temp1
    return p
