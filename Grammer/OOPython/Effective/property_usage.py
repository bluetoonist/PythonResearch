from datetime import timedelta
import datetime


class Bucket(object):
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.datetime.now()
        self.quota = 0
        # 추가 부분
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return "Bucket(quota=%d)" % self.quota

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        if amount == 0:
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta


def fill(bucket, amount):
    now = datetime.datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount
    return True


def deduct(bucket, amount):
    now = datetime.datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        return False
    bucket.quota -= amount
    return True


bucket = Bucket(60)
fill(bucket, 100)
print(bucket)

if deduct(bucket, 99):
    print("Had 99 quota")
else:
    print("Not Enough for 99 quota")
print(bucket)

if deduct(bucket, 3):
    print('Had 3 Quota')
else:
    print("Not enough for 3 quota")
print(bucket)
