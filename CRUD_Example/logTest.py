import sqlite3
connection = sqlite3.connect('./test.db')
connection.set_trace_callback(print)