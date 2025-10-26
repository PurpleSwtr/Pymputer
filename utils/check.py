from functools import wraps
import itertools
from typing import Callable

def check(turn_on: bool = False, num_inputs: int = 2, output_labels: tuple[str, ...] = ('OUT',), cnt_comands:bool = True) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            # time.sleep(0.05)
            # print(self.counter)
            if cnt_comands:
                self.counter += 1
            final_args = args
            final_kwargs = kwargs
            if turn_on:
                print(f"----- {func.__name__} -----")
                input_headers = [chr(ord('A') + i) for i in range(num_inputs)]
                all_headers = input_headers + list(output_labels)
                print("".join(f"{h:<8}" for h in all_headers))
                possible_inputs = itertools.product([0, 1], repeat=num_inputs)
                for inputs in possible_inputs:
                    result = func(self, *inputs)
                    result_tuple = result if isinstance(result, tuple) else (result,)
                    inputs_str = "".join(f"{i:<8}" for i in inputs)
                    outputs_str = "".join(f"{r:<8}" for r in result_tuple)
                    print(f"{inputs_str}{outputs_str}")
                print("----------------")
            return func(self, *final_args, **final_kwargs)
        return wrapper
    return decorator