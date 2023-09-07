import pynecone as pc
from .base_state import State
from .auth import login, signup
from .home import logger, log, loggingpage, apidatapage
from .api import api_store_drivedata

app = pc.App(state=State)
app.add_page(login, title="OBDLOGGER_LOGIN", route="/")
app.add_page(signup, title="OBDLOGGER_SIGNUP")
app.add_page(logger, title="OBDLOGGER")
app.add_page(log, title="OBDLOGGER_LOG")
app.add_page(loggingpage, title="OBDLOGGER_LOGGING")
app.add_page(apidatapage, title="OBDLOGGER_API_DATA")
# app.api.add_api_route("/api/{item_id}", api_test)
# app.api.add_api_route("/api/store/{item_id}", api_store_data, methods=["POST"])
app.api.add_api_route("/api/status", api_store_drivedata, methods=["GET"])
app.api.add_api_route("/api/drivedata/{user_id}", api_store_drivedata, methods=["POST"])
app.compile()
