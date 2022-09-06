import duckdb
from django.conf import settings


def export():
    con = duckdb.connect(':memory:')

    if settings.DEBUG:
        con.execute("INSTALL 'sqlite_scanner';")
        con.execute("LOAD 'sqlite_scanner';")
        con.execute(f"CALL sqlite_attach('{settings.SQLITE_PATH}');")
    else:
        con.execute("INSTALL 'postgres_scanner';")
        con.execute("LOAD 'postgres_scanner';")
        print(f"CALL POSTGRES_ATTACH('{settings.POSTGRES_URL}');")
        con.execute(f"CALL POSTGRES_ATTACH('{settings.POSTGRES_URL}');")
        #con.execute("CALL postgres_scanner('?::STRING');", (settings.POSTGRES_URL,))

    # Create a table with all user for authentication.
    # Format:
    # user_id | password |
    # INTEGER | VARCHAR  |
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
    # INTEGER | VARCHAR |
    con.execute(" \
        CREATE TABLE '_alias' AS \
        SELECT alias, \
            user_id \
        FROM user_alias \
        ORDER BY user_id \
    ")

    # Create table with all user permissions granted and/or inherited
    # for authorization.
    # Format:
    # user_id | permission_id | permission_name | ressources_id
    # INTEGER | INTEGER       | VARCHAR         | INTEGER
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

    con.execute("PRAGMA show('_permission');")
    con.execute("SELECT * FROM _user;")
    user = con.fetchall()
    con.execute("SELECT * FROM _alias;")
    alias = con.fetchall()
    con.execute("SELECT * FROM _permission;")
    permission = con.fetchall()

    #con.execute("SHOW TABLES;")
    con.execute(
        f"EXPORT DATABASE '{settings.DUCKDB_DATA_PATH}' (FORMAT PARQUET, CODEC 'SNAPPY')")

    return (user, alias, permission)

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at
