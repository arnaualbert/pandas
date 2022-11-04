import pandas  as pd

# - You are given the fixed Tycho dataset.
# - Write a function to view the ranking of diseases by number of total deaths 
# - at year 1896 in Massachussetts state (MA).

# - The dataframe must have 3 columns in this order: ranking, disease, num_deaths.


# -----------------------------------------------------------------------------
def get_total_deaths(entries: pd.DataFrame) -> pd.DataFrame:

    ranking_deaths: pd.DataFrame = (entries)
    #ranking_deaths.drop(["id"],axis=1,inplace=True)
    # ranking_deaths.loc[ : ,'state'] = "MA"
    ranking_deaths = ranking_deaths.query("year == 1896")
    ranking_deaths = ranking_deaths.query("state == 'MA' ")
    #ranking_deaths.drop(["epi_week"],axis=1,inplace=True)
    ranking_deaths = ranking_deaths.groupby(by="disease").sum()
    muertes = ranking_deaths["num_deaths"]
    suma = ranking_deaths["num_deaths"].sum()
    pct = []
    for muerte in muertes:
        muerte = muerte / suma * 100
        pct.append(muerte)
    pct_d = pct
    ranking_deaths["pct_deaths"] = pct_d
    ranking_deaths = ranking_deaths.sort_values(by=["num_deaths"],ascending=False)
    # ranking_deaths.drop(["year"],axis=1,inplace=True)
    contar = ranking_deaths["num_deaths"]
    indices = []
    cont = 1
    for _ in contar:
        indices.append(cont)
        cont += 1
    id = indices
    ranking_deaths["ranking"] = id
    ranking_deaths.reset_index(inplace=True)
    ranking_deaths = ranking_deaths.reindex(columns=["ranking","disease","num_deaths","pct_deaths"])


    return ranking_deaths


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    entries: pd.DataFrame = pd.read_csv("data/tycho-fixed22.csv", sep=",")
    
    ranking_deaths:  pd.DataFrame = get_total_deaths(entries)
    print(ranking_deaths)