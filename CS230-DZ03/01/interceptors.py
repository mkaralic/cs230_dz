from functools import wraps

def validate_args(*rules, **kwarg_rules):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Prolazimo kroz pravila i odgovarajuće argumente koristeći zip
            for arg, rule in zip(args, rules):
                expected_type = rule.get("type", None)
                min_val = rule.get("min", None)
                max_val = rule.get("max", None)

                # Provera tipa
                if expected_type and not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {arg} mora biti tipa {expected_type.__name__}, ali je tipa {type(arg).__name__}.")

                # Provera opsega
                if min_val is not None and arg < min_val:
                    raise ValueError(f"Argument {arg} mora biti veći ili jednak {min_val}.")
                if max_val is not None and arg > max_val:
                    raise ValueError(f"Argument {arg} mora biti manji ili jednak {max_val}.")

            # Provera kwargs argumenata prema pravilima
            for kwarg, value in kwargs.items():
                if kwarg in kwarg_rules:
                    rule = kwarg_rules[kwarg]
                    expected_type = rule.get("type", None)
                    min_val = rule.get("min", None)
                    max_val = rule.get("max", None)

                    # Provera tipa
                    if expected_type and not isinstance(value, expected_type):
                        raise TypeError(f"Kwarg '{kwarg}' mora biti tipa {expected_type.__name__}, ali je tipa {type(value).__name__}.")

                    # Provera opsega
                    if min_val is not None and value < min_val:
                        raise ValueError(f"Kwarg '{kwarg}' mora biti veći ili jednak {min_val}.")
                    if max_val is not None and value > max_val:
                        raise ValueError(f"Kwarg '{kwarg}' mora biti manji ili jednak {max_val}.")

            # Poziv originalne funkcije
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Funkcija koja koristi dekorator sa pravilima validacije
@validate_args(
    {"type": int, "min": 1, "max": 100},  # prvi argument mora biti int između 1 i 100
    {"type": int},  # drugi argument mora biti int
    a = {"type": int, "min": 18, "max": 120},  # 'a' mora biti int između 18 i 120
)
def add(a: int, b: int):
    return a + b

def main():
    try:
        print (f'Result is: {add(5, 3)}')
        print (f'Result is: {add(b = 5, a = 'aaa')}')
    except (TypeError, ValueError) as e:
        print(e)

if __name__ == '__main__':
    main()