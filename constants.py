from collections import OrderedDict
constants = dict()

EMPTY_STRING = ""

datatypes_list = [
    # Numeric datatypes
    'BIT',
    'TINYINT',
    'BOOL',
    'SMALLINT',
    'MEDIUMINT',
    'INT',
    'BIGINT',
    'DECIMAL',
    'FLOAT',
    'DOUBLE',

    # Time and Date datatypes
    'DATE',
    'DATETIME',
    'TIMESTAMP',
    'TIME',
    'YEAR',

    # String datatypes
    'CHAR',
    'VARCHAR',
    'BINARY',
    'TEXT',
    'MEDIUMTEXT',
    'LONGTEXT',
    'ENUM',
    'SET',
]

constraints = [
    'NOT NULL',
    'UNIQUE',
    'CHECK',
    'DEFAULT',
    'NONE'
]

constants['datatypes'] = OrderedDict(zip(datatypes_list, datatypes_list))
constants['constraints'] = OrderedDict(zip(constraints, constraints))
constants['EMPTY_STRING'] = EMPTY_STRING