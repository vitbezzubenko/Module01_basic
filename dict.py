

def unique()
    unig = []
    result = []
    for _dict in data:
        for key in _dict:
            if key in keys:
                if _dict[key] not in unig:
                    unig.append(_dict[key])
                    result.append(_dict)

    print(result)
