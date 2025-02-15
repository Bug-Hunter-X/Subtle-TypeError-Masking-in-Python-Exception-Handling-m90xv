def function_with_uncommon_bug(data):
    try:
        result = 10 / data['value']
        return result
    except KeyError:
        return 'KeyError'
    except TypeError:
        return 'TypeError'
    except ZeroDivisionError:
        return 'ZeroDivisionError'

# This is the problematic part, it hides the type error
result = function_with_uncommon_bug({'value': 0})
print(result) # Output: ZeroDivisionError

result = function_with_uncommon_bug({'wrong_key': 0})
print(result) # Output: KeyError

result = function_with_uncommon_bug(None)
print(result)  # Output: TypeError

result = function_with_uncommon_bug({'value': 'abc'}) #this will raise an error
print(result) 