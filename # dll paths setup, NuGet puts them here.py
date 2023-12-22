# dll paths setup, NuGet puts them here
base = "C:/Program Files/PackageManagement/NuGet/Packages/Microsoft.AnalysisServices"
_version = "19.4.0.2"  # at time of this writing
AMO_PATH = f"{base}.retail.amd64.{_version}/lib/net45/Microsoft.AnalysisServices.Tabular.dll"
ADOMD_PATH = f"{base}.AdomdClient.retail.amd64.{_version}/lib/net45/Microsoft.AnalysisServices.AdomdClient.dll"