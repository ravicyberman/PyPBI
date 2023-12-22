from sys import path

path.append("\\Program Files\\Microsoft.NET\\ADOMD.NET\\150")
from pyadomd import Pyadomd

CONNECTION_STRING = (
    r"Provider=MSOLAP;Data Source=.\SQLSERVER2019;Catalog=StackOverflow_Tabular;"
)