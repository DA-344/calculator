class Calculator:
    from typing import (
        Union as __union,
        Optional as __optional,
        Any as __any,
        List as __list,
        Dict as __dict,
    )

    def __init__(self, *nums: __union[int, float]) -> None:
        """
        The Calculator class, before specifying an operation don't forget to give the numbers.
        Syntax i.e.:
        ```py
        Calculator([1, 2, 3]).add()
        ```
        """

        self.__nums = nums

    def add(self, **kwgs: __any) -> __union[int, float]:
        """
        Adds every number given in Calculator class.
        """
        rounded: bool = kwgs.pop("rounded", False)

        return sum(self.__nums) if rounded == False else round(sum(self.__nums))

    def substract(self, **kwgs: __any) -> __union[int, float]:
        """
        Substracts the numbers given in Calculator class.
        """

        rounded: bool = kwgs.pop("rounded", False)

        result = self.__nums[0]

        for num in self.__nums[1:]:
            result = result - num

        return result if rounded == False else round(result)

    @property
    def numbers(self) -> __list[__union[int, float]]:
        return self.__nums

    def factorize(self, **kwgs: __any) -> __dict[int, str]:
        """
        Factorizes all the numbers diven in Calculator class.
        Should raise errors due to some dicts limitations
        """

        nums = {}

        for n in self.__nums:
            txt: str

            for i in range(n + 1):
                if i != 0:
                    if n % i == 0:
                        nums[int(n)] += f"{i},"

        return nums

    def divide(self) -> __union[int, float]:
        """Divides the first number by the second, then divides the result by the third, etc."""
        result = self.__nums[0]
        for num in self.__nums[1:]:
            result /= num

        return result


del (
    Calculator.__any,
    Calculator.__union,
    Calculator.__dict,
    Calculator.__optional,
    Calculator.__list,
)
