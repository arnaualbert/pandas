# Imports
import pandas  as pd

# -----------------------------------------------------------------------------
# Student name: WRITE YOUR NAME HERE
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question: get_total_deaths()
# -----------------------------------------------------------------------------
# 
# - You are given the fixed Tycho dataset.
# - Write a function to view the ranking of diseases by number of total deaths. 
# - Additionally, create a new field that calculates the percent of deaths  
# - of each diseases compared to the total of deaths in this year.
# 
# - Return parameters:
#   - Return a dataframe.
#   - The dataframe must have 4 columns in this order: ranking, disease, num_deaths, pct_deaths
#   - The ranking must start at 1
#   - The index must be numerical, starting from 0.
# 
# - Hint:
# - A Percentage is calculated by the mathematical formula of dividing the value by the sum of 
# - all the values and then multiplying the sum by 100. 
# - This is also applicable in Pandas Dataframes. 
# - The pre-defined sum() method of pandas series is used to compute the sum 
# - of all the values of a column.
# 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
#   - Run pytest to make sure you succeeded.
# -----------------------------------------------------------------------------


# - Write your solution here.
# - This function must be pure. Remember to delete your print() calls when done.
# -----------------------------------------------------------------------------
def get_total_deaths(entries: pd.DataFrame) -> pd.DataFrame:

    ranking_deaths: pd.DataFrame = (entries)
    ranking_deaths.drop(["id"],axis=1,inplace=True)
    ranking_deaths.drop(["year"],axis=1,inplace=True)
    ranking_deaths.drop(["epi_week"],axis=1,inplace=True)
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

    contar = ranking_deaths["pct_deaths"]
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


    # print(lista)
    # suma = ranking_deaths["num_deaths"].sum()
    # muertes = ranking_deaths["num_deaths"]
    # lista = []
    # for _ in muertes:
    #     total = muertes * suma / 100 
    #     lista.append(total)
    # print(lista)
# -----------------------------------------------------------------------------
