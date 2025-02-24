class NaturalPark:
    def __init__(self, name: str, surface: float, ecosystems: list, sensors: list, devices: list):
        self.name = name
        self.surface = surface
        self.ecosystems = ecosystems
        self.sensors = sensors
        self.devices = devices

    def __str__(self):
        return f"Name: {self.name}, Surface: {self.surface}, Ecosystems: {self.ecosystems}, Sensors: {self.sensors}, Devices: {self.devices}"

    def monitor_parameters(self):
        parameters = {}
        for ecosystem in self.ecosystems:
            parameters[ecosystem.name] = {
                "temperature": ecosystem.temperature,
                "humidity": ecosystem.humidity,
                "air_quality": ecosystem.air_quality
            }
        return parameters

    def activate_devices(self, name_of_ecosystem: str):
        for ecosystem in self.ecosystems:
            if ecosystem.name == name_of_ecosystem:
                for device in ecosystem.devices:
                    device.active()
                return True
        return False

    def deactivate_devices(self, name_of_ecosystem: str):
        for ecosystem in self.ecosystems:
            if ecosystem.name == name_of_ecosystem:
                for device in ecosystem.devices:
                    device.disable()
                return True
        return False

    def monitor_and_control(self):
        parameters = self.monitor_parameters()
        for ecosystem in self.ecosystems:
            name = ecosystem.name
            if parameters[name]["temperature"] > 30:
                self.activate_devices(name)
            else:
                self.deactivate_devices(name)

            if parameters[name]["humidity"] < 60:
                self.activate_devices(name)
            else:
                self.deactivate_devices(name)

            if parameters[name]["air_quality"] < 40:
                self.activate_devices(name)
            else:
                self.deactivate_devices(name)
        return parameters

class Ecosystem:
    def __init__(self, name: str, surface: float, sensors: list, devices: list, temperature: float, humidity: float, air_quality: float, natural_park: NaturalPark):
        self.name = name
        self.surface = surface
        self.sensors = sensors
        self.devices = devices
        self.temperature = temperature
        self.humidity = humidity
        self.air_quality = air_quality
        self.natural_park = natural_park
    
    def __str__(self):
        return f"Name: {self.name}, Surface: {self.surface}, Sensors: {self.sensors}, Devices: {self.devices}, Temperature: {self.temperature}, Humidity: {self.humidity}, Air Quality: {self.air_quality}"

class Device:
    def __init__(self, name: str, type: str, status: str, ecosystem: Ecosystem, natural_park: NaturalPark):
        self.name = name
        self.type = type
        self.status = status
        self.ecosystem = ecosystem
        self.natural_park = natural_park
    
    def active(self):
        self.status = 'active'
    
    def disable(self):
        self.status = 'inactive'
    
    def check_status(self):
        return self.status

class Sprinklers(Device):
    def __init__(self, name: str, ecosystem: Ecosystem, natural_park: NaturalPark):
        super().__init__(name, 'Sprinkler', 'inactive', ecosystem, natural_park)

class Fans(Device):
    def __init__(self, name: str, ecosystem: Ecosystem, natural_park: NaturalPark):
        super().__init__(name, 'Fan', 'inactive', ecosystem, natural_park)

class Lights(Device):
    def __init__(self, name: str, ecosystem: Ecosystem, natural_park: NaturalPark):
        super().__init__(name, 'Light', 'inactive', ecosystem, natural_park)

class Sensor:
    def __init__(self, type: str, location: str, value: float, unit_measure: str, active: bool, ecosystem: Ecosystem, natural_park: NaturalPark):
        self.type = type
        self.location = location
        self.value = value
        self.unit_measure = unit_measure
        self.active = active
        self.ecosystem = ecosystem
        self.natural_park = natural_park

    def __str__(self):
        return f"Type: {self.type}, Location: {self.location}, Value: {self.value} {self.unit_measure}, Active: {self.active}"

sprinkler1 = Sprinklers(name="Sprinkler1", ecosystem=None, natural_park=None)
fan1 = Fans(name="Fan1", ecosystem=None, natural_park=None)
light1 = Lights(name="Light1", ecosystem=None, natural_park=None)
sensor1 = Sensor(type="Temperature", location="Zone1", value=25.0, unit_measure="C", active=True, ecosystem=None, natural_park=None)

ecosystem1 = Ecosystem(
    name="Forest",
    surface=100.0,
    sensors=[sensor1],
    devices=[sprinkler1, fan1, light1],
    temperature=25.0,
    humidity=70.0,
    air_quality=80.0,
    natural_park=None
)
natural_park = NaturalPark(
    name="Eco Park",
    surface=1000.0,
    ecosystems=[ecosystem1],
    sensors=[sensor1],
    devices=[sprinkler1, fan1, light1]
)

ecosystem1.natural_park = natural_park
sensor1.ecosystem = ecosystem1
sensor1.natural_park = natural_park
sprinkler1.ecosystem = ecosystem1
sprinkler1.natural_park = natural_park
fan1.ecosystem = ecosystem1
fan1.natural_park = natural_park
light1.ecosystem = ecosystem1
light1.natural_park = natural_park

parameters = natural_park.monitor_and_control()
print(parameters)

sensor2 = Sensor(type="Humidity", location="Zone2", value=60.0, unit_measure="%", active=True, ecosystem=None, natural_park=None)
sensor3 = Sensor(type="Air Quality", location="Zone3", value=75.0, unit_measure="AQI", active=True, ecosystem=None, natural_park=None)
sprinkler2 = Sprinklers(name="Sprinkler2", ecosystem=None, natural_park=None)
fan2 = Fans(name="Fan2", ecosystem=None, natural_park=None)
light2 = Lights(name="Light2", ecosystem=None, natural_park=None)

ecosystem2 = Ecosystem(
    name="Wetlands",
    surface=200.0,
    sensors=[sensor2, sensor3],
    devices=[sprinkler2, fan2, light2],
    temperature=22.0,
    humidity=85.0,
    air_quality=70.0,
    natural_park=None
)

natural_park.ecosystems.append(ecosystem2)
ecosystem2.natural_park = natural_park
sensor2.ecosystem = ecosystem2
sensor2.natural_park = natural_park
sensor3.ecosystem = ecosystem2
sensor3.natural_park = natural_park
sprinkler2.ecosystem = ecosystem2
sprinkler2.natural_park = natural_park
fan2.ecosystem = ecosystem2
fan2.natural_park = natural_park
light2.ecosystem = ecosystem2
light2.natural_park = natural_park

parameters = natural_park.monitor_and_control()
print(parameters)