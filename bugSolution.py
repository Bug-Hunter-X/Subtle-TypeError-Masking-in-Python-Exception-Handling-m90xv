def function_with_uncommon_bug_fixed(data):
    try:
        if not isinstance(data, dict) or 'value' not in data:
            raise TypeError('Input must be a dictionary with a "value" key')
        value = data['value']
        if not isinstance(value,(int,float)):
            raise TypeError("Value must be a number")
        result = 10 / value
        return result
    except KeyError as e:
        return f'KeyError: {e}'
    except TypeError as e:
        return f'TypeError: {e}'
    except ZeroDivisionError:
        return 'ZeroDivisionError'

result = function_with_uncommon_bug_fixed({'value': 0})
print(result) # Output: ZeroDivisionError

result = function_with_uncommon_bug_fixed({'wrong_key': 0})
print(result) # Output: KeyError

result = function_with_uncommon_bug_fixed(None)
print(result)  # Output: TypeError: Input must be a dictionary with a "value" key

result = function_with_uncommon_bug_fixed({'value': 'abc'})
print(result) # Output: TypeError: Value must be a number