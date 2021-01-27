def func_executor(*args):
    results = []
    for func_name, data in args:
        result = func_name(*data)
        results.append(result)
    return results
