class NaturalPark:
    def __init__(self, name: str, surface: float, ecosystem: list, sensors: list, devices: list):
        self.name = name
        self.surface = surface
        self.ecosystem = list()
        self.sensors = list()
        self.devices = list()

    def __str__(self):
        return f"Name: {self.name}, surface: {self.surface}, ecosystem: {self.ecosystem}, sensors: {self.sensors}, devices: {self.devices}"
    
    def monitor_parameters(self):
        return dict()
    
    def activate_devices(self, name_of_ecosystems: str):
        return bool

class Ecosystem:
    def __init__(self, name: str, surface: float, sensors: list, devices: list, temperature: float, humidity: float, air_quality: float, nature_park: NaturePark):
        self.name = name
        self.surface = surface
        self.sensors = list(Sensor)
        self.devices = list(Device)
        self.temperature = float
        self.humidity = float
        self.air_quality = float
        self.nature_park = NaturalPark
    
    def __str__(self):
        return f"Name: {self.name}, surface: {self.surface}, sensors: {self.sensors}, devices: {self.devices}, temperature: {self.temperature}, humidity: {self.humidity}, air quality: {self.air_quality}"

class Device:
    def __init__(self, name: str, surface: float, sensors: list, devices: list, temperature: float, humidity: float, air_quality: float, nature_park: NaturePark):
        self.name =  str
        self.type = str
        self.status = str
        self.ecosystem = Ecosystem
        self.nature_park = NaturalPark
    
    def active(self, Ecosystem) : pass
    def disable(self) : pass 
    def check_status(self) :pass 

class Sprinklers(Device):
    def __init__():
        pass

class Fans(Device):
    def __init__():
        pass

class Lights(Device):
    def __init__():
        pass

class Sensor:
    def __init__(self, type: str, location: str, value: float, unit_measure: str, active: bool, ecosystem: Ecosystem, natural_park: NaturalPark):
        self.type = str
        self.location = str
        self.value = float
        self.unit_measure = str
        self.active = bool
        self.ecosystem = Ecosystem
        self.natural_park = NaturalPark