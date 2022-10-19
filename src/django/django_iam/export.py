import duckdb
import pandas as pd
from sqlalchemy import create_engine
from django.conf import settings

def export():
    # Create an engine instance
    alchemyEngine = create_engine(settings.POSTGRESQL_URL, pool_recycle=3600)

    # Connect to PostgreSQL server
    dbConnection = alchemyEngine.connect()

    # Read data from PostgreSQL database tables and load into a DataFrame instance
    user_user = pd.read_sql(
        "SELECT permissionsmixin_ptr_id, password FROM user_user WHERE is_active IS TRUE", dbConnection)
    user_alias = pd.read_sql(
        "SELECT alias, user_id FROM user_alias", dbConnection)
    permission_permission = pd.read_sql(
        "SELECT * FROM permission_permission", dbConnection)
    user_permissionsmixin_user_permissions = pd.read_sql(
        "SELECT * FROM user_permissionsmixin_user_permissions", dbConnection)
    group_group_permissions = pd.read_sql(
        "SELECT * FROM group_group_permissions", dbConnection)
    user_permissionsmixin_groups = pd.read_sql(
        "SELECT * FROM user_permissionsmixin_groups", dbConnection)

    # Close the database connection
    dbConnection.close()


    # Create DuckDB Connection
    con = duckdb.connect(':memory:')

    # Create a table with all user for authentication.
    # Format:
    # user_id | password |
    # UUID    | VARCHAR  |
    con.execute(" \
        CREATE TABLE '_user' AS \
        SELECT permissionsmixin_ptr_id as user_id, \
            password \
        FROM user_user \
        ORDER BY user_id \
    ")

    # Create table with all alias and associated user for authentication.
    # Format:
    # user_id | alias   |
    # UUID    | VARCHAR |
    con.execute(" \
        CREATE TABLE '_alias' AS \
        SELECT user_id, \
            alias \
        FROM user_alias \
        ORDER BY user_id \
    ")

    # Create table with all user permissions granted and/or inherited
    # for authorization.
    # Format:
    # user_id | permission_id | permission_name | ressources_id
    # UUID    | INTEGER       | VARCHAR         | INTEGER
    con.execute(" \
        CREATE TABLE '_permission' AS \
        SELECT permissionsmixin_id AS user_id,\
            __permission.id AS permission_id, \
            __permission.name AS permission_name, \
            __permission.ressources_id AS ressources_id \
        FROM 'permission_permission' __permission \
        INNER JOIN user_permissionsmixin_user_permissions __user_permission \
        ON __permission.id = __user_permission.permission_id \
        INNER JOIN user_user __user \
        ON __user.permissionsmixin_ptr_id = __user_permission.permissionsmixin_id \
        UNION \
        SELECT permissionsmixin_id AS user_id, \
            __permission.id AS permission_id, \
            __permission.name AS permission_name, \
            __permission.ressources_id AS ressources_id \
        FROM 'permission_permission' __permission \
        INNER JOIN group_group_permissions __group_permission \
        ON __permission.id = __group_permission.permission_id \
        INNER JOIN user_permissionsmixin_groups __user_group_mix\
        ON __group_permission.group_id = __user_group_mix.group_id \
        ORDER BY user_id \
    ")

    con.execute("SELECT * FROM _user;")
    user = con.fetchall()
    con.execute("SELECT * FROM _alias;")
    alias = con.fetchall()
    con.execute("SELECT * FROM _permission;")
    permission = con.fetchall()

    con.execute(
        f"EXPORT DATABASE '{settings.DUCKDB_DATA_PATH}' (FORMAT PARQUET, CODEC 'SNAPPY')")

    return (user, alias, permission)

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at
