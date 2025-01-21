from enum import Enum


class CreatedByRole(str, Enum):
    ACCOUNT = "account"
    END_USER = "end_user"
