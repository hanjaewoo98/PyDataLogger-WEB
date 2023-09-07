import pynecone as pc

logpage = "/log"


def navbar(State):
    """The navbar."""
    return pc.box(
        pc.hstack(
            pc.link(
                pc.hstack(pc.image(src="favicon.ico"), pc.heading("OBDMonitor")),
                href="/",
            ),

            pc.menu(
                pc.menu_button(
                    pc.cond(
                        State.logged_in,
                        pc.avatar(name=State.username, size="md"),
                        pc.box(),
                    )
                ),
                pc.menu_list(
                    pc.center(
                        pc.vstack(
                            pc.avatar(name=State.username, size="md"),
                            pc.text(State.username),
                        )
                    ),
                    pc.menu_divider(),
                    # pc.link(pc.menu_item("로그아웃"), on_click=State.logout),
                    # pc.link(
                    #     pc.menu_item("테마변경"),
                    #     on_click=pc.toggle_color_mode,
                    # ),
                    pc.link(
                        pc.menu_item("기록확인"),
                        href="/log"
                    ),
                    pc.link(
                        pc.menu_item("로그확인"),
                        href="/apidatapage"
                    ),
                    pc.button(
                        pc.icon(tag="moon"),
                        on_click=pc.toggle_color_mode,
                        width="100%",
                    ),
                    pc.button(
                        pc.icon(tag="close"),
                        on_click=State.logout,
                        width="100%",
                    )
                    # pc.link(
                    #     pc.menu_item("AI통계"),
                    # ),
                ),
            ),
            justify="space-between",
            border_bottom="0.2em solid #F0F0F0",
            padding_x="2em",
            padding_y="0.5em",
            bg="rgba(173, 173, 173, 1)",
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="500",
    )


def inside_navbar(State):
    """Inside Navbar"""
    return pc.box(
        pc.hstack(
            pc.link(
                pc.hstack(pc.image(src="favicon.ico"), pc.heading("OBDMonitor")),
                href="/logger",
            ),

            pc.menu(
                pc.menu_button(
                    pc.cond(
                        State.logged_in,
                        pc.avatar(name=State.username, size="md"),
                        pc.box(),
                    )
                ),
                pc.menu_list(
                    pc.center(
                        pc.vstack(
                            pc.avatar(name=State.username, size="md"),
                            pc.text(State.username),
                        )
                    ),
                    pc.menu_divider(),
                    # pc.link(pc.menu_item("로그아웃"), on_click=State.logout),
                    # pc.link(
                    #     pc.menu_item("테마변경"),
                    #     on_click=pc.toggle_color_mode,
                    # ),
                    pc.link(
                        pc.menu_item("기록확인"),
                        href="/log"
                    ),
                    pc.link(
                        pc.menu_item("로그확인"),
                        href="/apidatapage"
                    ),
                    pc.button(
                        pc.icon(tag="moon"),
                        on_click=pc.toggle_color_mode,
                        width="100%",
                    ),
                    pc.button(
                        pc.icon(tag="close"),
                        on_click=State.logout,
                        width="100%",
                    )
                    # pc.link(
                    #     pc.menu_item("AI통계"),
                    # ),
                ),
            ),
            justify="space-between",
            border_bottom="0.2em solid #F0F0F0",
            padding_x="2em",
            padding_y="0.5em",
            bg="rgba(173, 173, 173, 1)",
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="500",
    )
