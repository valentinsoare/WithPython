#!/usr/bin/python

class Time:

    def __init__(self, hour=0, minute=0, second=0, total_seconds=0):
        self._hour = hour
        self._minute = minute
        self._second = second
        self._total_seconds = total_seconds

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, hour):
        if not (0 <= hour < 24):
            raise ValueError(f'Hour {hour} must be between 0 - 23')
        else:
            self._hour = hour

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, minute):
        if not (0 <= minute < 60):
            raise ValueError(f'Minute {minute} must be between 0 and 59')
        else:
            self._minute = minute

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, second):
        if not (0 <= second < 60):
            raise ValueError(f'Second {second} must bet between 0 and 59')
        else:
            self._second = second

    @property
    def time(self):
        return self.hour, self.minute, self.second

    @time.setter
    def time(self, time):
        self.set_time(*time)

    def set_time(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def total_seconds(self):
        return self._total_seconds

    @total_seconds.setter
    def total_seconds(self, seconds=0):
        if seconds < 0:
            raise ValueError('Total seconds must be greater than 0')

        self._total_seconds = seconds

    def get_total_seconds(self):
        if self.total_seconds != 0:
            return self.total_seconds
        else:
            return self.hour * 3600 + self.minute * 60 + self.second

    @property
    def universal_str(self):
        var_to_return = ''
        if self.hour in range(0, 10):
            var_to_return = f'{self.hour:0>2}:'
        elif self.hour in range(10, 12):
            var_to_return = f'{self.hour}:'
        elif self.hour in range(12, 24):
            var_to_return = f'{self.hour}:'

        var_to_return += f'{self.minute:0>2}:{self.second:0>2}'

        if self.hour in range(0, 12):
            var_to_return += ' AM'
        elif self.hour in range(12, 24):
            var_to_return += ' PM'

        return var_to_return

    def __str__(self):
        if self.hour in (0, 12):
            var_to_return = '12'
        else:
            var_to_return = str(self.hour % 12)

        var_to_return += f':{self.minute:0>2}:{self.second:0>2}'

        if self.hour < 12:
            var_to_return += ' AM'
        else:
            var_to_return += ' PM'

        return var_to_return


def main():
    my_hour = Time(17, 30, 5)

    print(my_hour.universal_str)
    print(f'{my_hour}')


main()
