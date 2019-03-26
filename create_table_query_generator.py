from collections import OrderedDict
from constants import constants


def get_datatype():
    """Returns the datatype selected by the user from a list of
       available datatypes.
    """

    print("\n")
    for index, datatype in enumerate(constants["datatypes"]):
        print(f"{index}. {datatype}")

    datatype_index = input("\nEnter the data type: ")
    datatype_index = int(datatype_index)
    datatype = list(constants["datatypes"].values())[datatype_index]
    return datatype


def get_constraint():
    """Returns the specific constrained if desired by the user
       on the query, NONE if no constraint is selected.
    """

    print("\n")
    for index, constraint in enumerate(constants["constraints"]):
        print(f"{index}. {constraint}")

    constraint_index = input("\nEnter the constraint : ")
    constraint_index = int(constraint_index)
    constraint = list(constants["constraints"].values())[constraint_index]
    return constraint


def generate_column_query(column):
    """Generates column data part of the create table query"""

    primary_key = "PRIMARY KEY" if column['primary_key'] is 'Y' else constants['EMPTY_STRING']

    if column['foreign_key']['is_foreign_key'] is 'Y':
        foreign_key = f"FOREIGN KEY REFERENCES {column['foreign_key']['referenced_table']}({column['foreign_key']['referenced_column']})"
    else:
        foreign_key = constants['EMPTY_STRING']
    
    return (
        f"{column['name']} {column['datatype']} {primary_key} {foreign_key}"
    )


def generate_create_table_query(table):
    """Generates single create table query according to the table
       schema passed.
    """

    create_table_SQL = f"CREATE TABLE {table['name']} ( " 
    column_SQL = constants['EMPTY_STRING']

    
    for column in table['columns']:
        column_SQL = column_SQL + generate_column_query(column) + ", "
    
    column_SQL = column_SQL[0:column_SQL.rfind(',')]
    column_SQL = column_SQL + ")"

    return create_table_SQL + column_SQL + ";"


def generate_query(schema): 
    """Generates a string which is the final query for generating the given schema."""

    SQL = constants['EMPTY_STRING']
    for table in schema.keys():
        SQL = SQL + generate_create_table_query(schema[table]) + "\n"

    # Replace double spaces by single space
    final_query = SQL.replace("  ", " ")
    return final_query


num_tables = input("Enter the number of tables: ")
num_tables = int(num_tables)

schema = OrderedDict()
for table_num in range(1, num_tables + 1):
    table_name = 'table' + str(table_num)
    schema[table_name] = dict()

    # Get tablewise information
    print(f"\n**************   Table no. {table_num}    ***************************")

    name = input("Name: " )
    schema[table_name]['name'] = name

    num_columns = input('Number of columns: ')
    num_columns = int(num_columns)
    schema[table_name]['columns'] = list()

    # Get columnwise information
    for column_num in range(1, num_columns + 1):
        print(f"\n**************   Column no. {column_num}    ***************************")
        column_name = input("Name: ")
        datatype = get_datatype()
        primary_key = input("Primary Key (Y/N): ")
        foreign_key = input("Foreign Key (Y/N): ")
        if foreign_key is 'Y':
            referenced_table = input('References(Table Name): ')
            referenced_column = input('References(Column Name): ')
        else : 
            referenced_table = None
            referenced_column = None
        constraint = get_constraint()
        if constraint is not 'NONE':
            value = input('Value: ')
        else :
            value = ""
        # Create column dictionary from above values
        column = {
            'name': column_name,
            'datatype': datatype,
            'primary_key': primary_key,
            'foreign_key': {
                'is_foreign_key': foreign_key,
                'referenced_table': referenced_table,
                'referenced_column': referenced_column
            },
            'constraint': {
                'name': constraint,
                'value': value
            }
        }

        schema[table_name]['columns'].append(column)


SQL = generate_query(schema)
print(SQL)
