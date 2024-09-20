class modelbasedreflexagent:
    def __init__(self,desired_temperature):
        self.desired_temperature = desired_temperature
        self.heater_state = {}     

    def percieve(self,current_temperature):
        self.current_temperature = current_temperature

    def act(self):
        if self.current_temperature < self.desired_temperature:
            if self.heater_state != "on":   #avoid redundent action
                action = "Turn on heater"
                self.heater_state = "on"
            else:
                action = "Heater already on"

        else:
            if self.heater_state != "off":
                action = "Turn off heateer"
                self.heater_state = "off"

            else:
                action = "Heater already off"

        return action

rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 25
}


desired_temperature = 22
agent = modelbasedreflexagent(desired_temperature)

for room, temperature in rooms.items():
    agent.percieve(temperature)
    action = agent.act()
    print(f"{room}: Current temperature = {temperature}C. {action}.")