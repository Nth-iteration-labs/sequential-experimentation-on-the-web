n = 2
request_countl = base.List(self.get_theta(key="request_count"), base.Count, ["1", "2"])
fulfill_countl = base.List(self.get_theta(key="fulfilled_surveys"), base.Count, ["1", "2"])

# For the first n surveys, give a random condition
if request_countl.count() < n:
    self.action["treatment"] = request_countl.random()
    # Or else, give the condition with the lowest fulfilled surveys
else:
    self.action['treatment'] = fulfill_countl.min()

# Increase request count
count = base.Count(self.get_theta(key="request_count", value=self.action["treatment"]))
count.increment()
self.set_theta(count, key="request_count", value=self.action["treatment"])
