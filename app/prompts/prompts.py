from langchain_core.prompts import ChatPromptTemplate


def get_sql_query_prompt() -> ChatPromptTemplate:

    sql_query_prompt_template = """
    Based on the table schema below, write a SQL query that would answer the user's question:
    {schema}
    
    Question: {question}
    SQL Query:
    """

    return ChatPromptTemplate.from_template(sql_query_prompt_template)


def get_bot_response_prompt() -> str:

    genie_reply_prompt = """
    Process the result from the output returned by the database 
    from the execution SQL query in a chat generated message:
    {db_rows}.

    INSTRUCTIONS:
    1. If output from the SQL query is a count of records, then output message should be:
    These are n records where n is the count.
    2. If the output from the SQL query is an array of records, then output should contain the count of records
    and then the actual records.
    Do not add any other information to the output which does not correspond to SQL result.   
    """

    return genie_reply_prompt
