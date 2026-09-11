class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:

        def is_leap(year):
            return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

        def days_in_month(year, month):

            if month == 2:
                return 29 if is_leap(year) else 28

            if month in [4, 6, 9, 11]:
                return 30

            return 31

        def next_day(year, month, day):

            day += 1

            if day > days_in_month(year, month):
                day = 1
                month += 1

                if month > 12:
                    month = 1
                    year += 1

            return year, month, day

        # Convert date string into integers
        y1, m1, d1 = map(int, date1.split("-"))
        y2, m2, d2 = map(int, date2.split("-"))

        # Make date1 the earlier date
        if (y1, m1, d1) > (y2, m2, d2):
            y1, m1, d1, y2, m2, d2 = y2, m2, d2, y1, m1, d1

        count = 0

        # Move one day at a time
        while (y1, m1, d1) != (y2, m2, d2):

            y1, m1, d1 = next_day(y1, m1, d1)
            count += 1

        return count