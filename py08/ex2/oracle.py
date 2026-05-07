import sys
import os
import dotenv


class OracleConfig():
    def __init__(self):
        self.raw_config: dict[str, str | None] = {}
        self.config: dict[str, str] = {}

        self.mode = "development"

        self.all_vars = {
                "required" : [
                    "MATRIX_MODE", 
                    "DATABASE_URL",
                    "API_KEY"
                    ],
                "optional" : [
                    "LOG_LEVEL",
                    "ZION_ENDPOINT"
                    ]}

        self.errors = []
        self.warnings = []



        

    def handler_ouput_error(self, key: str, type_error: str) -> None:
        messages = {
            "MATRIX_MODE": {
                "missing": "MATRIX_MODE is missing: system mode not defined",
                "empty": "MATRIX_MODE is empty: cannot determine environment",
                "invalid": "MATRIX_MODE invalid: must be 'development' or 'production'",
            },
            "DATABASE_URL": {
                "missing": "DATABASE_URL is missing: no database connection available",
                "empty": "DATABASE_URL is empty: cannot establish database connection",
                "invalid": "DATABASE_URL invalid: expected valid connection string",
            },
            "API_KEY": {
                "missing": "API_KEY is missing: authentication required",
                "empty": "API_KEY is empty: external services access denied",
                "invalid": "API_KEY invalid: security credentials not valid",
            },
            "LOG_LEVEL": {
                "missing": "LOG_LEVEL is missing: defaulting to DEBUG",
                "empty": "LOG_LEVEL is empty: using DEBUG as fallback",
                "invalid": "LOG_LEVEL invalid: falling back to INFO",
            },
            "ZION_ENDPOINT": {
                "missing": "ZION_ENDPOINT is missing: using localhost fallback",
                "empty": "ZION_ENDPOINT is empty: defaulting to http://localhost",
                "invalid": "ZION_ENDPOINT invalid: fallback to safe local endpoint",
            },
        }

        message = messages.get(key, {}).get(type_error, f"{key} {type_error}")
        should_exit = key in self.all_vars.get("required", [])

        print(message)
        if should_exit:
            print("\nConfiguration abort:\n  exit\n")
            sys.exit(1)
        

    def init_raw_config(self) -> None:
        dotenv.load_dotenv()
        keys = self.all_vars.get("required", []) + self.all_vars.get("optional", [])

        self.raw_config = {k: os.getenv(k) for k in keys}

        for key in keys:
            raw_value = self.raw_config.get(key)
            if raw_value is None:
                self.handler_ouput_error(key, "missing")
            elif raw_value == "":
                self.handler_ouput_error(key, "empty")
            elif key == "MATRIX_MODE" and raw_value not in {"development", "production"}:
                self.handler_ouput_error(key, "invalid")


    def set_config(self, new_key: str, mode: str) -> None:
        if mode is "KEY":
            
            self.set_config(new_key, "VALUE")
        if mode is "VALUE":
            if new_key is "LOG_LEVEL":
                if 

    def validate_raw_config(self) -> None:
        key = self.raw_config.get("LOG_LEVEL")
        if key is None:
            self.raw_config.update("LOG_LEVEL", "DEBUG")
            self.raw_config.pop("None")
        elif key is "":
            self.raw_config["LOG_LEVEL"] = "DEBUG"
        elif 
        self.config = self.raw_config.copy()
        
            



if __name__ == "__main__":

    oracle = OracleConfig()

    print("ORACLE STATUS: Reading the Matrix...\n")
    oracle.init_raw_config()
    oracle.validate_raw_config()
    print(oracle.raw_config)
    tmp = oracle.raw_config.get("LOG_LEVEL")
    print(type(tmp))
    if tmp is "":
        print("   is empty")
    



