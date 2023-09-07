import pynecone as pc


class User(pc.Model, table=True):
    """A table of Users."""

    username: str
    password: str


class OBDData(pc.Model, table=True):
    loggedUser: str
    datetime: str
    driveData: str


class SpeedData(pc.Model, table=True):
    loggedUser: str
    datetime: str
    avgSpeed: str
    maxSpeed: str


class TempData(pc.Model, table=True):
    loggedUser: str
    datetime: str
    avgCoolantTemp: str
    avgIntakeTemp: str


class RPMData(pc.Model, table=True):
    loggedUser: str
    datetime: str
    avgRPM: str
    maxRPM: str


class DriveTimeData(pc.Model, table=True):
    loggedUser: str
    datetime: str
    avgDriveTime: str


class DriveData(pc.Model, table=True):
    loggedUser: str
    datetime: str
    avgDriveTime: str


class StoreApiDataModel(pc.Model, table=True):
    loggedUser: str
    datetime: str
    driveDataType: str
    driveData: str


class State(pc.State):
    """The base state for the app."""

    username: str
    logged_in: bool = False

    def logout(self):
        """Log out a user."""
        self.reset()
        return pc.redirect("/")


