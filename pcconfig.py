import pynecone as pc

config = pc.Config(
    app_name="OBDLogger_PY",
    bun_path="$HOME/.bun/bin/bun",
    api_url="http://obdlogger.site:8000",
    # api_url="http://localhost:8000",
    db_url="sqlite:///OBDLogger_PY/pynecone.db",
    # env=pc.Env.DEV,
)
