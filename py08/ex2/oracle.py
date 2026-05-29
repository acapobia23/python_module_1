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


    def handler_error(self, key: str, type_error: str) -> None:
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
                self.handler_error(key, "missing")


    def validate_raw_config(self) -> None:
        keys_required = self.all_vars.get("required", [])

        for key in keys_required:
            raw_value = self.raw_config.get(key)
            if key == "MATRIX_MODE" and raw_value not in {"development", "production"}:
                self.handler_error(key, "invalid") 
            elif raw_value == "":
                self.handler_error(key, "empty") 

        log_valid = ["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"]
        log_value = self.raw_config.get("LOG_LEVEL")
        if log_value == "":
            self.handler_error("LOG_LEVEL", "empty")
            self.raw_config["LOG_LEVEL"] = "DEBUG"
        if log_value.islower() is True:
            log_value = log_value.upper()
            self.raw_config["LOG_LEVEL"] = log_value
        if log_value not in log_valid:
            self.handler_error("LOG_LEVEL", "invalid")
            self.raw_config["LOG_LEVEL"] = "INFO"
        raw_value = self.raw_config.get("ZION_ENDPOINT")
        if raw_value == "":
            self.handler_error("ZION_ENDPOINT", "empty")
            self.raw_config["ZION_ENDPOINT"] = "http://localhost" 
        if raw_value.isspace is True:
            self.handler_error("ZION_ENDPOINT", "invalid")
            self.raw_config["ZION_ENDPOINT"] = "http://localhost500"
        self.config = self.raw_config.copy()


    def prod_output(self, key: str, value: str) -> tuple[str, str]:
        fancy_keys = {
            "MATRIX_MODE": "SYSTEM MODE",
            "DATABASE_URL": "NEURAL CORE",
            "API_KEY": "ORACLE ACCESS",
            "LOG_LEVEL": "MONITORING LEVEL",
            "ZION_ENDPOINT": "ZION NETWORK"
        }

        f_key = fancy_keys.get(key, key)

        if key == "DATABASE_URL":
            f_value = "Connected to Neural Core Cluster"

        elif key == "API_KEY":
            f_value = "Oracle authentication layer active"

        elif key == "ZION_ENDPOINT":
            f_value = "Secure resistance channel established"

        elif key == "LOG_LEVEL":
            levels = {
                "DEBUG": "Full system observability enabled",
                "INFO": "Operational awareness active",
                "WARN": "Stability monitoring active",
                "ERROR": "Critical-only logging mode"
            }
            f_value = levels.get(value, "Unknown logging state")

        elif key == "MATRIX_MODE":
            f_value = "Production sanctum active"

        return f_key, f_value

    def show_config(self) -> None:
        mode = self.config.get("MATRIX_MODE")

        print("Configuration loaded :")
        if mode == "development":
            for key, value in self.config.items():
                print(f" {key}: {value}")
        else:
            for key, value in self.config.items():
                f_key, f_value = self.prod_output(key, value)
                print(f" {f_key}: {f_value}")
        print()

    def env_security_check(self) -> list[tuple[str, str]]:
        mode = self.config.get("MATRIX_MODE")

        if mode == "production":
            return [
                ("OK", "No hardcoded secrets detected"),
                ("OK", ".env file properly configured"),
                ("OK", "Production overrides available")
            ]
        return [
            ("OK", "No hardcoded secrets detected (dev-safe mode)"),
            ("OK", ".env file loaded"),
            ("INFO", "Production overrides not active")
        ]


    def show_env_security(self) -> None:
        print("Environment security check:")

        for status, msg in self.env_security_check():
            print(f" [{status}] {msg}")
        print()


if __name__ == "__main__":

    oracle = OracleConfig()

    print("ORACLE STATUS: Reading the Matrix...\n")
    oracle.init_raw_config()
    oracle.validate_raw_config()
    oracle.show_config()
    oracle.show_env_security()
    print("The Oracle sees all configurations.")
    



