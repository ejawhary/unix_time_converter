from datetime import datetime
import math


class StampToDate:

    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.remainingSeconds = self.timestamp
        self.year_seconds = 31556926
        self.month_seconds = 2629743
        self.day_seconds = 86400
        self.hour_seconds = 3600
        self.minute_seconds = 60
        self.year = 1970
        self.month = 1
        self.day = 1
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.date = datetime(1970, 1, 1, 0, 0, 0)
        self.periods_vars = {"year": self.year, "month": self.month, "day": self.day, "hour": self.hour,
                             "minute": self.minute, "second": self.second}
        self.period_seconds = {"year": self.year_seconds, "month": self.month_seconds, "day": self.day_seconds,
                             "hour": self.hour_seconds, "minute": self.minute_seconds, "second": self.second}

    def calculateDate(self):

        while self.remainingSeconds > 0:
            if self.remainingSeconds >= self.year_seconds:
                self.printPeriod("year")
                self.calculatePeriod("year")
                continue
            elif self.remainingSeconds >= self.month_seconds:
                self.printPeriod("month")
                self.calculatePeriod("month")
                continue
            elif self.remainingSeconds >= self.day_seconds:
                self.printPeriod("day")
                self.calculatePeriod("day")
                continue
            elif self.remainingSeconds >= self.hour_seconds:
                self.printPeriod("hour")
                self.calculatePeriod("hour")
                continue
            elif self.remainingSeconds >= self.minute_seconds:
                self.printPeriod("minute")
                self.calculatePeriod("minute")
                continue
            else:
                self.year = self.periods_vars["year"]
                self.month = self.periods_vars["month"]
                self.day = self.periods_vars["day"]
                self.hour = self.periods_vars["hour"]
                self.minute = self.periods_vars["minute"]
                self.second = self.remainingSeconds

                self.date = datetime(self.year, self.month, self.day, self.hour, self.minute, self.second)
                print(f"{self.timestamp} = {self.date.strftime('%d %b %Y %H:%M:%S')}")
                break

    def calculatePeriod(self, period):
        self.periods_vars[period] += math.floor(self.remainingSeconds / self.period_seconds[period])
        # print(self.periods_vars[period])
        # print(f"{self.remainingSeconds} % {self.period_seconds[period]}")
        self.remainingSeconds %= (self.period_seconds[period])

    def printPeriod(self, period):

        print(f"{period.title()} = {self.periods_vars[period]} + ({self.remainingSeconds} / "
              f"{self.period_seconds[period]}) = "
              f"{self.periods_vars[period] + math.floor(self.remainingSeconds / self.period_seconds[period])} "
              f"R {self.remainingSeconds % self.period_seconds[period]}")
