# Update fulfilled count
count = base.Count(self.get_theta(key="fulfilled_surveys", value=self.action["treatment"]))
count.update(self.reward["finished"])
self.set_theta(count, key="fulfilled_surveys", value=self.action["treatment"])
