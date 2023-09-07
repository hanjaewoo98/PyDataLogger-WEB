import pynecone as pc
from .base_state import State, User, OBDData, DriveData, StoreApiDataModel, SpeedData, TempData, RPMData


def get_stored_log_data(username):
    with pc.session() as session:
        result = session.query(StoreApiDataModel).filter(StoreApiDataModel.loggedUser == username).first()
        if result is not None:
            result_list = session.query(StoreApiDataModel).filter(StoreApiDataModel.loggedUser == username).all()
            data_dict_list = [{column.key: getattr(data, column.key) for column in StoreApiDataModel.__table__.columns}
                              for data in result_list]
            return data_dict_list
    return ""


def get_stored_log_list(username):
    with pc.session() as session:
        result = session.query(StoreApiDataModel).filter(StoreApiDataModel.loggedUser == username).first()
        if result is not None:
            result_list = session.query(StoreApiDataModel).filter(StoreApiDataModel.loggedUser == username).all()
            data_dict_list = [{column.key: getattr(data, column.key) for column in StoreApiDataModel.__table__.columns}
                              for data in result_list]
            data = data_dict_list
            from pynecone import List
            columns: List[str] = ["loggedUser", "datetime", "driveDataType", "driveData"]
            return pc.data_table(
                data=data,
                columns=columns,
            )
        else:
            return ""


def get_drive_speed_data(username):
    with pc.session() as session:
        result_list = session.query(SpeedData).filter(SpeedData.loggedUser == username).all()
        if result_list is not None:
            data_dict = {data.datetime: data.avgSpeed for data in result_list}
            return data_dict
        else:
            return {}


def print_coolant_temp(username):
    with pc.session() as session:
        result = session.query(TempData).filter(DriveData.loggedUser == username).first()
        if result is not None:
            result_list = session.query(DriveData).filter(DriveData.loggedUser == username).all()
            data_dict_list = [{column.key: getattr(data, column.key) for column in DriveData.__table__.columns}
                              for data in result_list]
            data = data_dict_list
            from pynecone import List
            columns: List[str] = ["loggedUser", "datetime", "avgDriveTime"]
            return pc.data_table(
                data=data,
                columns=columns,
            )


def get_coolant_temp_data(username):
    with pc.session() as session:
        result_list = session.query(TempData).filter(TempData.loggedUser == username).all()
        if result_list is not None:
            data_dict = {i + 1: data.avgCoolantTemp for i, data in enumerate(result_list)}
            return data_dict
        else:
            return {}


def get_rpm_data(username):
    with pc.session() as session:
        result_list = session.query(RPMData).filter(RPMData.loggedUser == username).all()
        if result_list is not None:
            data_dict = {i + 1: data.avgRPM for i, data in enumerate(result_list)}
            return data_dict
        else:
            return {}


def get_data_list(username):
    with pc.session() as session:
        drive_data_result = session.query(DriveData).filter(DriveData.loggedUser == username).all()
        drive_data_result = sorted(drive_data_result, key=lambda x: x.datetime, reverse=True)
        if not drive_data_result:
            return ""

        data_rows = []
        for drive_data_row in drive_data_result:
            datetime = drive_data_row.datetime
            avg_drive_time = drive_data_row.avgDriveTime

            speed_data_result = session.query(SpeedData).filter(SpeedData.loggedUser == username, SpeedData.datetime == datetime).first()
            if speed_data_result:
                avg_speed = speed_data_result.avgSpeed
                max_speed = speed_data_result.maxSpeed
            else:
                avg_speed = None
                max_speed = None

            rpm_data_result = session.query(RPMData).filter(RPMData.loggedUser == username, RPMData.datetime == datetime).first()
            if rpm_data_result:
                avg_rpm = rpm_data_result.avgRPM
                max_rpm = rpm_data_result.maxRPM
            else:
                avg_rpm = None
                max_rpm = None

            temp_data_result = session.query(TempData).filter(TempData.loggedUser == username, TempData.datetime == datetime).first()
            if temp_data_result:
                avg_coolant_temp = temp_data_result.avgCoolantTemp
                avg_intake_temp = temp_data_result.avgIntakeTemp
            else:
                avg_coolant_temp = None
                avg_intake_temp = None

            data_rows.append({
                'loggedUser': username,
                'datetime': datetime,
                'avgSpeed': avg_speed,
                'maxSpeed': max_speed,
                'avgRPM': avg_rpm,
                'maxRPM': max_rpm,
                'avgCoolantTemp': avg_coolant_temp,
                'avgIntakeTemp': avg_intake_temp,
                'avgDriveTime': avg_drive_time
            })

        return pc.data_table(
            data=data_rows,
            columns=['loggedUser', 'datetime', 'avgSpeed', 'maxSpeed', 'avgRPM', 'maxRPM', 'avgCoolantTemp',
                     'avgIntakeTemp', 'avgDriveTime']
        )
