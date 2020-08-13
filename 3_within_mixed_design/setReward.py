if self.reward["finished"] is 1:
    finished_treatment = base.Count(self.get_theta(key="finished" + self.context["user_id"], value=self.action["treatment"]))
    finished_treatment.increment()
    self.set_theta(finished_treatment, key="finished" + self.context["user_id"], value=self.action["treatment"])     
