import pynecone as pc
from .base_state import State, User
from .helpers import navbar

styles = {
    "login_page": {
        "padding_top": "10em",
        "text_align": "top",
        "position": "relative",
        "width": "100%",
        "height": "100vh",
    },
    "login_input": {
        "shadow": "lg",
        "padding": "1em",
        "border_radius": "lg",
        "background": "gray",
    },
}


class AuthState(State):
    password: str
    confirm_password: str

    def signup(self):
        """Sign up a user."""
        with pc.session() as session:
            if self.password != self.confirm_password:
                return pc.window_alert("비밀번호가 일치하지 않습니다.")
            if session.exec(User.select.where(User.username == self.username)).first():
                return pc.window_alert("중복된 아이디입니다.")
            user = User(username=self.username, password=self.password)
            session.add(user)
            session.commit()
            self.logged_in = True
            return pc.redirect("/logger")

    def login(self):
        """Log in a user."""
        with pc.session() as session:
            user = session.exec(
                User.select.where(User.username == self.username)
            ).first()
            if user and user.password == self.password:
                self.logged_in = True
                return pc.redirect("/logger")
            else:
                return pc.window_alert("로그인 정보가 일치하지 않습니다")


def signup():
    return pc.box(
        pc.mobile_and_tablet(
            pc.vstack(
                navbar(State),
                pc.center(
                    pc.vstack(
                        pc.heading("Sign Up", font_size="1.5em"),
                        pc.input(
                            on_blur=State.set_username, placeholder="Username", width="100%"
                        ),
                        pc.input(
                            on_blur=AuthState.set_password,
                            placeholder="Password",
                            width="100%",
                        ),
                        pc.input(
                            on_blur=AuthState.set_confirm_password,
                            placeholder="Confirm Password",
                            width="100%",
                        ),
                        pc.button("Sign Up", on_click=AuthState.signup, width="100%"),
                    ),
                    style=styles["login_input"],
                ),
            ),
            style=styles["login_page"],
        ),
        pc.tablet_and_desktop(
            pc.vstack(
                navbar(State),
                pc.center(
                    pc.vstack(
                        pc.heading("Sign Up", font_size="1.5em"),
                        pc.input(
                            on_blur=State.set_username, placeholder="Username", width="100%"
                        ),
                        pc.input(
                            on_blur=AuthState.set_password,
                            placeholder="Password",
                            width="100%",
                        ),
                        pc.input(
                            on_blur=AuthState.set_confirm_password,
                            placeholder="Confirm Password",
                            width="100%",
                        ),
                        pc.button("Sign Up", on_click=AuthState.signup, width="100%"),
                    ),
                    style=styles["login_input"],
                ),
            ),
            style=styles["login_page"],
        ),
    )


def login():
    return pc.box(
        pc.mobile_and_tablet(
            pc.vstack(
                navbar(State),
                pc.center(
                    pc.vstack(
                        pc.input(
                            on_blur=State.set_username, placeholder="Username", width="100%"
                        ),
                        pc.input(
                            on_blur=AuthState.set_password,
                            placeholder="Password",
                            type_="password",
                            width="100%",
                        ),
                        pc.button("Login", on_click=AuthState.login, width="100%"),
                        pc.link(
                            pc.button("Sign Up", width="100%"), href="/signup", width="100%"
                        ),
                    ),
                    style=styles["login_input"],
                ),
            ),
            style=styles["login_page"],
        ),
        pc.tablet_and_desktop(
            pc.vstack(
                navbar(State),
                pc.center(
                    pc.vstack(
                        pc.input(
                            on_blur=State.set_username, placeholder="Username", width="100%"
                        ),
                        pc.input(
                            on_blur=AuthState.set_password,
                            placeholder="Password",
                            type_="password",
                            width="100%",
                        ),
                        pc.button("Login", on_click=AuthState.login, width="100%"),
                        pc.link(
                            pc.button("Sign Up", width="100%"), href="/signup", width="100%"
                        ),
                    ),
                    style=styles["login_input"],
                ),
            ),
            style=styles["login_page"],
        ),
    )
