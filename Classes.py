class Brakes:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time, name):
        self.name = name
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)

class Gearbox:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time, name):
        self.name = name
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)

class Rear_wing:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time, name):
        self.name = name
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)

class Front_wing:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time, name):
        self.name = name
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)

class Suspension:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time, name):
        self.name = name
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)

class Engine:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time, name):
        self.name = name
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)

class Bottle:
    def __init__(self, speed, cornering, power_unit, reliability, pit_stop, overtaking, defending, race_start, tyre_management, name):
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_stop = pit_stop
        self.overtaking = overtaking
        self.defending = defending
        self.race_start = race_start
        self.tyre_management = tyre_management
        self.name = name
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + self.pit_stop + self.overtaking + self.defending + self.race_start + self.tyre_management)

class Setup:
    def __init__(self, Brakes, Gearbox, Rear_Wing, Front_Wing, Suspension, Engine, n):
        self.Brakes = Brakes.teamscore
        self.Gearbox = Gearbox.teamscore
        self.Rear_wing = Rear_Wing.teamscore
        self.Front_wing = Front_Wing.teamscore
        self.Suspension = Suspension.teamscore
        self.Engine = Engine.teamscore
        self.n = n
        #self.Bottle = Bottle.teamscore
        self.teamscore =Brakes.teamscore + Gearbox.teamscore + Rear_Wing.teamscore + Front_Wing.teamscore + Suspension.teamscore + Engine.teamscore

class Pilots:
    def __init__(self, name, overtaking, defending, qualifying, race_start, tyre_management):
        self.name = name
        self.overtaking = overtaking
        self.defending = defending
        self.qualifying = qualifying
        self.race_start = race_start
        self.tyre_management = tyre_management
        self.teamscore = (self.overtaking + self.defending + self.qualifying + self.race_start + self.tyre_management)
