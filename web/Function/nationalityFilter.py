from web.Function.data import data

nationality = data[data["Nationality"].isin(["England", "France", "Italy", "Spain", "Brazil", "Argentina", "Germany"])]
