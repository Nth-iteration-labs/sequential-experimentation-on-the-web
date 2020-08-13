if self.context["user_id"] == "":
    self.context["user_id"] = hex(random.getrandbits(42))[2:-1]
    
    while self.get_theta(key="finished" + self.context["user_id"]) != {}:
        self.context["user_id"] = hex(random.getrandbits(42))[2:-1]
        
    member_finished = base.List(self.get_theta(key="finished" + self.context["user_id"]), base.Count, ["A", "B", "C"])
    self.action["treatment"] = member_finished.random()   
elif self.get_theta(key="finished" + self.context["user_id"]) != {}:
    member_finished = base.List(self.get_theta(key="finished" + self.context["user_id"]), base.Count, ["A", "B", "C"])
    if member_finished.count() < 3:
        self.action["treatment"] = member_finished.random()
        while int(member_finished.get_dict()[self.action["treatment"]]['n']) > 0:
            self.action["treatment"] = member_finished.random()
    else:
        self.action["treatment"] = "finished"
else:
    self.action["treatment"] = "wrong_id"      
