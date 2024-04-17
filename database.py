from typing import Sequence, Any, Dict, Union

from langchain_community.utilities import SQLDatabase
from sqlalchemy import Result

import settings

db: SQLDatabase


def init_database() -> None:

    global db
    db = SQLDatabase.from_uri(settings.MYSQL_DATABASE_URI)


def get_schema(_) -> str:
    return db.get_table_info()


def execute_sql(sql) -> Union[str, Sequence[Dict[str, Any]], Result[Any]]:
    return db.run(sql)
