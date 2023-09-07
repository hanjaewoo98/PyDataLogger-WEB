import pynecone as pc
import pandas as pd
import numpy as np

from .data_print_processor import get_stored_log_list, get_drive_speed_data, get_coolant_temp_data, get_rpm_data, \
    get_data_list
from .helpers import inside_navbar
# from .api import get_stored_log_list

from .base_state import State
from .sms_sender import MessageSendState

carName = "K3GT"
loggerPageUrl = "/logger"
mainPageUrl = "/"
logging_header = "OBD 로깅 기록 조회"


class HomeState(State):
    search: str


def index():
    return pc.center(
        pc.vstack(
            pc.heading("OBD DATA LOGGER",
                       background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                       background_clip="text",
                       font_weight="bold", font_size="2em"),
            pc.box("Simple And Powerful OBD2-Based Data Logger"),
            pc.link(
                "Upload Data",
                href=loggerPageUrl,
                border="0.1em solid",
                padding="0.2em",

                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },

            ),
            pc.button(
                pc.icon(tag="moon"),
                on_click=pc.toggle_color_mode,

            ),

            spacing="1.5em",
            font_size="3.6em",
        ),
        padding_top="10%",

    )


def logger():
    return pc.box(
        pc.mobile_and_tablet(
            pc.vstack(
                inside_navbar(State),
                pc.vstack(

                    pc.heading(
                        carName,
                        background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                        background_clip="text",
                        font_weight="bold",
                        font_size="2.5em",
                        padding_top="18%",
                    ),

                    pc.image(
                        src="https://www.kia.com/content/dam/kwp/kr/ko/configurator/k3-gt/trim/exterior/swp/swp_01.png",
                        width="800px",
                        height="auto",
                    ),
                    spacing="0.3em",
                    font_size="2em",
                ),
                pc.vstack(
                    pc.box(
                        pc.hstack(
                            pc.box(
                                pc.vstack(
                                    pc.text("최근 드라이빙 데이터", font_size="1.65em", color="black", font_weight="bold"),
                                    padding="1%",
                                ),
                                pc.hstack(
                                    pc.stat_group(
                                        pc.stat(
                                            pc.stat_label("AVG SPEED"),
                                            pc.stat_number("65Km/h"),
                                            pc.stat_help_text(
                                                pc.stat_arrow(type_="increase"),
                                                "4%",
                                            ),
                                            padding="2.2%",
                                            color="black",
                                        ),
                                        pc.stat(
                                            pc.stat_label("TOP SPEED"),
                                            pc.stat_number("165Km/h"),
                                            pc.stat_help_text(
                                                pc.stat_arrow(type_="increase"),
                                                "4%",
                                            ),
                                            padding="2.2%",
                                            color="black",
                                        ),
                                        pc.stat(
                                            pc.stat_label("AIR TEMP"),
                                            pc.stat_number("42°C"),
                                            pc.stat_help_text(
                                                pc.stat_arrow(type_="decrease"),
                                                "14%",
                                            ),
                                            padding="2.2%",
                                            color="black",
                                        ),
                                        pc.stat(
                                            pc.stat_label("DCT TEMP"),
                                            pc.stat_number("132°C"),
                                            pc.stat_help_text(
                                                pc.stat_arrow(type_="increase"),
                                                "134%",
                                            ),
                                            padding="2.2%",
                                            color="black",
                                        ),
                                        pc.stat(
                                            pc.stat_label("EFFICIENCY"),
                                            pc.stat_number("6.5km/l"),
                                            pc.stat_help_text(
                                                pc.stat_arrow(type_="decrease"),
                                                "0.8km/l",
                                            ),
                                            padding="2.2%",
                                            color="black",
                                        ),
                                        pc.stat(
                                            pc.stat_label("AVG POWER"),
                                            pc.stat_number("132HP"),
                                            pc.stat_help_text(
                                                pc.stat_arrow(type_="increase"),
                                                "4HP",
                                            ),
                                            padding="2.2%",
                                            color="black",
                                        ),
                                        width="100%",
                                    )

                                ),
                                bg="#FFFFFF",
                                border_radius="15px",
                                padding="2%",
                                width="100%",
                                height="auto",
                                padding_top="1%",

                            ),

                        ),
                        pc.hstack(padding="1.7%"),
                        pc.hstack(
                            pc.button(
                                "통계 전송하기",
                                border_radius="1em",
                                box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                                background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                                box_sizing="border-box",
                                color="white",
                                on_click=MessageSendState.send_sms,
                                _hover={
                                    "opacity": 0.85,
                                },
                                width="100%"

                            ),
                        ),
                        pc.hstack(padding="1.7%"),
                        pc.hstack(
                            pc.box(
                                pc.vstack(
                                    pc.box(
                                        element="iframe",
                                        src="https://www.youtube.com/embed/Zxg04v_GN1Y",
                                        width="100%",
                                        height="170px",
                                    ),
                                    pc.box(
                                        element="iframe",
                                        src="https://www.youtube.com/embed/mNyUbPLiv_g",
                                        width="100%",
                                        height="170px",
                                    ),
                                    spacing="1%",

                                ),

                                bg="#FFFFFF",
                                border_radius="15px",
                                padding="2%",
                                width="100%",
                                height="auto",
                                padding_top="1%",
                            ),
                        ),
                        pc.hstack(padding="0.7%"),

                        bg="#555c5f",
                        border_radius="15px",
                        padding="1%",
                        width="80%",
                        height="auto",
                        padding_top="1%",

                    ),
                ),
            ),
        ),
        pc.tablet_and_desktop(
            pc.vstack(
                inside_navbar(State),
                pc.vstack(

                    pc.heading(carName,
                               background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                               background_clip="text",
                               font_weight="bold", font_size="2.5em"),
                    pc.image(
                        src="https://www.kia.com/content/dam/kwp/kr/ko/configurator/k3-gt/trim/exterior/swp/swp_01.png",
                        width="800px",
                        height="auto",
                    ),
                    spacing="1.1em",
                    font_size="2em",
                    padding_top="7%",
                ),
                pc.vstack(
                    pc.box(
                        pc.hstack(
                            pc.box(
                                pc.vstack(
                                    pc.text("최근 드라이빙 데이터", font_size="1.65em", color="black", font_weight="bold"),
                                    padding="1%",
                                ),
                                pc.hstack(
                                    pc.stat_group(
                                        pc.stat(
                                            pc.stat_label("AVG SPEED"),
                                            pc.stat_number("65Km/h"),
                                            pc.stat_help_text(
                                                pc.stat_arrow(type_="increase"),
                                                "4%",
                                            ),
                                            padding="1%",
                                            color="black",
                                        ),
                                        pc.stat(
                                            pc.stat_label("TOP SPEED"),
                                            pc.stat_number("165Km/h"),
                                            pc.stat_help_text(
                                                pc.stat_arrow(type_="increase"),
                                                "4%",
                                            ),
                                            padding="1%",
                                            color="black",
                                        ),
                                        pc.stat(
                                            pc.stat_label("AIR TEMP"),
                                            pc.stat_number("42°C"),
                                            pc.stat_help_text(
                                                pc.stat_arrow(type_="decrease"),
                                                "14%",
                                            ),
                                            padding="1%",
                                            color="black",
                                        ),
                                        pc.stat(
                                            pc.stat_label("DCT TEMP"),
                                            pc.stat_number("132°C"),
                                            pc.stat_help_text(
                                                pc.stat_arrow(type_="increase"),
                                                "134%",
                                            ),
                                            padding="1%",
                                            color="black",
                                        ),
                                        pc.stat(
                                            pc.stat_label("DRIVE TIME"),
                                            pc.stat_number("4:32hr"),
                                            pc.stat_help_text(
                                                pc.stat_arrow(type_="decrease"),
                                                "22min",
                                            ),
                                            padding="1%",
                                            color="black",
                                        ),
                                        pc.stat(
                                            pc.stat_label("FUEL EFFICIENCY"),
                                            pc.stat_number("6.5km/l"),
                                            pc.stat_help_text(
                                                pc.stat_arrow(type_="decrease"),
                                                "0.8km/l",
                                            ),
                                            padding="1%",
                                            color="black",
                                        ),
                                        pc.stat(
                                            pc.stat_label("AVG POWER"),
                                            pc.stat_number("132HP"),
                                            pc.stat_help_text(
                                                pc.stat_arrow(type_="increase"),
                                                "4HP",
                                            ),
                                            padding="1%",
                                            color="black",
                                        ),
                                        width="100%",
                                    )

                                ),
                                bg="#FFFFFF",
                                border_radius="15px",
                                padding="1%",
                                width="100%",
                                height="auto",
                                padding_top="1%",

                            ),

                        ),
                        pc.hstack(padding="0.7%"),
                        pc.hstack(
                            pc.button(
                                "통계 전송하기",
                                border_radius="1em",
                                box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                                background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                                box_sizing="border-box",
                                color="white",
                                on_click=MessageSendState.send_sms,
                                _hover={
                                    "opacity": 0.85,
                                },
                                width="80em"

                            ),
                        ),
                        pc.hstack(padding="0.7%"),
                        pc.hstack(
                            pc.box(
                                pc.hstack(
                                    pc.box(
                                        element="iframe",
                                        src="https://www.youtube.com/embed/Zxg04v_GN1Y",
                                        width="100%",
                                        height="340px",
                                    ),
                                    pc.box(
                                        element="iframe",
                                        src="https://www.youtube.com/embed/mNyUbPLiv_g",
                                        width="100%",
                                        height="340px",
                                    ),
                                    spacing="1%",

                                ),

                                bg="#FFFFFF",
                                border_radius="15px",
                                padding="1%",
                                width="100%",
                                height="auto",
                                padding_top="1%",
                            ),
                        ),
                        bg="#555c5f",
                        border_radius="15px",
                        padding="1%",
                        width="80%",
                        height="auto",
                        padding_top="1%",

                    ),
                ),
            ),
        ),
    )


def log():
    return pc.box(
        pc.mobile_and_tablet(
            pc.vstack(
                inside_navbar(State),
                pc.box(
                    pc.vstack(
                        pc.box(
                            pc.center(
                                pc.text("주행 스타일", color="black", font_weight="bold", font_size="1.6em"),
                            ),
                            pc.box(
                                pc.pie(
                                    data=pc.data(
                                        "pie",
                                        x=["정차", "에코", "노말", "스포츠", "스마트"],
                                        y=[1, 2, 3, 10, 4],
                                    ),
                                    color_scale="qualitative",
                                    pad_angle=5.0,
                                    inner_radius=100.0,
                                    start_angle=90.0,
                                ),

                            ),
                            width="19em",
                            height="19em",
                        ),
                        pc.hstack(padding="3%"),

                        pc.box(
                            pc.center(
                                pc.text("냉각수 온도", color="black", font_weight="bold", font_size="1.6em"),
                            ),
                            pc.box(
                                pc.chart(
                                    pc.line(
                                        data=pc.data(
                                            "line",
                                            x=list(get_coolant_temp_data("admin").keys()),
                                            y=list(get_coolant_temp_data("admin").values())

                                        ),
                                        interpolation="natural",
                                        style={
                                            "data": {"stroke": "green", "strokeWidth": 2}
                                        },
                                    ),

                                    domainPadding={"x": 50, "y": 50},
                                ),
                            ),
                            width="25em",
                        ),

                    ),
                    pc.hstack(padding="3%"),

                    pc.vstack(
                        pc.box(
                            pc.center(
                                pc.text("주행 평균속도", color="black", position="center", left="5%", top="5%",
                                        font_weight="bold", font_size="1.4em"),
                            ),
                            # data_dict=get_drive_speed_data("admin"),
                            # x=list(get_drive_speed_data("admin").keys()),
                            # y=list(get_drive_speed_data("admin").values()),

                            pc.center(
                                pc.box(
                                    pc.chart(
                                        pc.line(
                                            data=pc.data(
                                                "line", x=list(get_drive_speed_data("admin").keys()),
                                                y=list(get_drive_speed_data("admin").values()),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            width="25em",
                            # height="25em",
                        ),
                        pc.hstack(padding="3%"),

                        pc.box(
                            pc.center(
                                pc.text("RPM 로깅데이터", color="black", font_weight="bold", font_size="1.4em"),
                            ),
                            pc.box(
                                pc.chart(
                                    pc.line(
                                        data=pc.data(
                                            "line",
                                            x=list(get_rpm_data("admin").keys()),
                                            y=list(get_rpm_data("admin").values())

                                        ),
                                        interpolation="natural",
                                        style={
                                            "data": {"stroke": "green", "strokeWidth": 2}
                                        },
                                    ),

                                    domainPadding={"x": 50, "y": 80},

                                ),
                            ),
                            width="25em",

                            # height="25em",
                        ),
                    ),
                    bg="#f8f8f8",
                    border_radius="15px",
                    width="auto",
                    padding_top="2%",
                    padding_bottom="2%",
                    padding_side="2%",
                ),
                padding_top="14%",
            ),
        ),
        pc.tablet_and_desktop(
            pc.vstack(
                inside_navbar(State),
                pc.box(
                    pc.hstack(
                        pc.box(
                            pc.center(
                                pc.text("주행 스타일", color="black", font_weight="bold", font_size="1.4em"),
                            ),
                            pc.box(
                                pc.pie(
                                    data=pc.data(
                                        "pie",
                                        x=["정차", "에코", "노말", "스포츠", "스마트"],
                                        y=[1, 2, 3, 10, 4],
                                    ),
                                    color_scale="qualitative",
                                    pad_angle=5.0,
                                    inner_radius=100.0,
                                    start_angle=90.0,
                                ),

                            ),
                            width="25em",
                            height="25em",
                        ),
                        pc.center(
                            pc.divider(
                                orientation="vertical", border_color="black"
                            ),
                            height="30em",
                        ),
                        pc.box(

                            pc.center(
                                pc.text("냉각수 온도", color="black", font_weight="bold", font_size="1.4em"),
                            ),
                            pc.box(
                                pc.chart(
                                    pc.line(
                                        data=pc.data(
                                            "line",
                                            x=list(get_coolant_temp_data("admin").keys()),
                                            y=list(get_coolant_temp_data("admin").values())

                                        ),
                                        interpolation="natural",
                                        style={
                                            "data": {"stroke": "green", "strokeWidth": 2}
                                        },
                                    ),

                                    domainPadding={"x": 50, "y": 50},
                                ),
                            ),
                            width="25em",
                            # height="25em",
                        ),

                    ),

                    pc.divider(
                        border_color="black",
                    ),

                    pc.hstack(
                        pc.box(
                            pc.center(
                                pc.text("주행 평균속도", color="black", position="center", left="5%", top="5%",
                                        font_weight="bold", font_size="1.4em"),
                            ),
                            # data_dict=get_drive_speed_data("admin"),
                            # x=list(get_drive_speed_data("admin").keys()),
                            # y=list(get_drive_speed_data("admin").values()),

                            pc.center(
                                pc.box(
                                    pc.chart(
                                        pc.line(
                                            data=pc.data(
                                                "line", x=list(get_drive_speed_data("admin").keys()),
                                                y=list(get_drive_speed_data("admin").values()),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            width="25em",
                            # height="25em",
                        ),
                        pc.center(
                            pc.divider(
                                orientation="vertical", border_color="black"
                            ),
                            height="30em",
                        ),
                        pc.box(
                            pc.center(
                                pc.text("RPM 로깅데이터", color="black", font_weight="bold", font_size="1.4em"),
                            ),
                            pc.box(
                                pc.chart(
                                    pc.line(
                                        data=pc.data(
                                            "line",
                                            x=list(get_rpm_data("admin").keys()),
                                            y=list(get_rpm_data("admin").values())

                                        ),
                                        interpolation="natural",
                                        style={
                                            "data": {"stroke": "green", "strokeWidth": 2}
                                        },
                                    ),

                                    domainPadding={"x": 50, "y": 80},

                                ),
                            ),
                            width="25em",

                            # height="25em",
                        ),
                    ),
                ),
                bg="#f8f8f8",
                border_radius="15px",
                width="auto",
                padding_top="2%",
                padding_bottom="2%",
                padding_side="2%",
            ),
            padding_top="0.6%",
        ),
    )


def loggingpage():
    return pc.box(
        pc.vstack(
            inside_navbar(State),
            pc.vstack(
                pc.heading("API 기록 조회",
                           background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                           background_clip="text",
                           font_weight="bold",
                           font_size="4.7em",
                           spacing="0.3em",
                           padding="2.2%",
                           padding_side="50%",
                           ),
                # pc.text("OBD 로깅 기록 조회"),
                get_stored_log_list("admin")
            ),
            padding_top="7%",
        ),
    )


def apidatapage():
    username = "admin"

    return pc.box(
        pc.vstack(
            inside_navbar(State),
            pc.vstack(
                # pc.heading(username,
                #            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                #            background_clip="text",
                #            font_weight="bold",
                #            font_size="3.0em",
                #            spacing="0.3em",
                #            padding="2.2%",
                #            padding_side="50%",
                #            ),
                pc.heading("Api 데이터 조회",
                           background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                           background_clip="text",
                           font_weight="bold",
                           font_size="3.3em",
                           spacing="0.3em",
                           padding="2.2%",
                           padding_side="50%",
                           ),
                get_data_list(username)

            ),
            padding_top="7%",
        ),
    )
