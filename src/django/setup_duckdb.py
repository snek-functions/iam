import duckdb

con = duckdb.connect(':memory:')
con.execute("INSTALL httpfs;")

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at