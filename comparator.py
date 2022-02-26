import timeit
from typing import Any, Dict, List, Protocol, Union


class GenericFunction(Protocol):
    def __call__(self, **kwds: Any) -> Any:
        ...


class FunctionsTimer:
    def __setup_attributes(self) -> None:
        # Dictionary with keys as function names and values as a list of times
        self.funcs_times: Dict[str, List[float]] = {}

        # Dictionary with keys as executed codes and values as a list of times
        self.code_times: Dict[str, List[float]] = {}

        # Dictionary that has both information. See time_funcs doc for details
        self.funcs_code_times: Dict[str, Dict[str, Union[str, List[float]]]] = {}

    def time_funcs(
        self,
        functions: Dict[GenericFunction, Dict[str, Any]],
        repeat_times: int = 5,
        num_trials: int = 1_000_000,
    ) -> Dict[str, Dict[str, List]]:
        """Times functions execution

        Args:
            functions (Dict[GenericFunction, Dict[str, Any]]):
                    {
                        function_to_be_analyzed: {  # empty if function does not accept any parameters
                            'parameter_name': param_value,
                            'parameter_name': param_value,
                            .
                            .
                            .
                        }
                        function_to_be_analyzed: {  # empty if function does not accept any parameters
                            'parameter_name': param_value,
                            'parameter_name': param_value,
                            .
                            .
                            .
                        }
                        .
                        .
                        .
                    }
            repeat_times (int, optional): Number of repeats. Defaults to 5.
            num_trials (int, optional): Number of times the function is called in
            each repeat. Defaults to 1_000_000.

        Returns:
            Dict[str, Dict[str, List]]:

                {
                    function_name: {
                        'code_execution': code that got executed: str,
                        'times': List of timed execution results
                    }
                    function_name {
                        'code_execution': code that got executed: str,
                        'times': List of timed execution results
                    }
                    .
                    .
                    .
                }
        """

        self.__setup_attributes()

        for func, args in functions.items():

            arg_correspondents = [f"{arg_name}={arg}" for arg_name, arg in args.items()]

            parameters = ",".join(arg_correspondents)

            globals()[func.__name__] = func

            func_str = f"{func.__name__}({parameters})"

            times = timeit.repeat(
                stmt=func_str,
                globals=globals(),
                repeat=repeat_times,
                number=num_trials,
            )

            self.funcs_code_times[func.__name__] = {
                "code_executed": func_str,
                "times": times,
            }

            self.funcs_times[func.__name__] = times

            self.code_times[func_str] = times

        return self.funcs_code_times
