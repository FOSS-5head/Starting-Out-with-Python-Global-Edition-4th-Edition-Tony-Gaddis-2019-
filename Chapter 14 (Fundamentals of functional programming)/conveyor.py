# Конвейер обработки данных.


def pipe(data, *fseq):
    for fn in fseq:
        data = fn(data)
    return data


pipe(2,
     lambda x: x + 5,
     lambda x: x * x,
     lambda x: str(x))

