import logging
from .main import special_command, RAW_QUERY, PARSED_QUERY

log = logging.getLogger(__name__)

@special_command('\\dt', '\\dt', 'List tables.', arg_type=RAW_QUERY, case_sensitive=True)
def list_tables(cur, **_):
    query = 'SHOW TABLES'
    log.debug(query)
    cur.execute(query)
    if cur.description:
        headers = [x[0] for x in cur.description]
        return [(None, cur, headers, '')]
    else:
        return [(None, None, None, '')]

@special_command('\\l', '\\l', 'List databases.', arg_type=RAW_QUERY, case_sensitive=True)
def list_databases(cur, **_):
    query = 'SHOW DATABASES'
    log.debug(query)
    cur.execute(query)
    if cur.description:
        headers = [x[0] for x in cur.description]
        return [(None, cur, headers, '')]
    else:
        return [(None, None, None, '')]


@special_command('\\d', '\\d [table]', 'Describe table.', case_sensitive=True)
def describe_table(cur, arg=None, arg_type=PARSED_QUERY, **_):
    if arg is None:
        return list_tables(cur)
    query = 'SHOW FIELDS FROM {0}'.format(arg)
    log.debug(query)
    cur.execute(query)
    if cur.description:
        headers = [x[0] for x in cur.description]
        return [(None, cur, headers, '')]
    else:
        return [(None, None, None, '')]
