# Imports
import pandas  as pd

# -----------------------------------------------------------------------------
# Student name: Arnau Albert Sanchez
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question: get_total_deaths()
# -----------------------------------------------------------------------------
# 
# - You are given the fixed Tycho dataset.
# - You can also use the files with solutions of question 2.
# -
# - Now, write a function that obtains all the disease that have registered
# - cases and deaths. 
# - We need to solve this question to resolve question 4, a ranking of
# - disease by death_ratio.
# 
# - Return parameters, in each function:
#   - Return a dataframe
#   - The dataframe must have 4 columns in this order: id,disease,deaths,cases
#   - 
# - Hints:
#   - 1. To make an intersection of 2 dataframe you can use merge function, using the parameter how='inner'
#   - 2. Watch the expected results in the file:
#   - tycho-q3-cases-deaths.csv
#   - 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
# -----------------------------------------------------------------------------
def merge_cases_and_deaths(entries: pd.DataFrame) -> pd.DataFrame:
    df_merged_cases_and_deaths: pd.DataFrame = (entries)

    df_total_deaths: pd.DataFrame = (entries)

    df_total_deaths = df_total_deaths.loc[df_total_deaths["event"] == 'DEATHS']

    df_total_deaths = df_total_deaths.groupby(by="disease").sum()
    df_total_deaths = df_total_deaths.sort_values(by=["disease"],ascending=False)
    df_total_deaths.reset_index(inplace=True)
    df_total_deaths = df_total_deaths.reindex(columns=["disease","number"])


    df_total_cases: pd.DataFrame = (entries)
    df_total_cases = df_total_cases.loc[df_total_cases["event"] == 'CASES']

    df_total_cases = df_total_cases.groupby(by="disease").sum()
    df_total_cases = df_total_cases.sort_values(by=["disease"],ascending=False)
    df_total_cases = df_total_cases.rename(columns={'number':'cases'})
    df_total_cases.reset_index(inplace=True)
    df_total_cases = df_total_cases.reindex(columns=["disease","cases"])


    df_merged_cases_and_deaths = pd.merge(df_total_deaths,df_total_cases)
    df_merged_cases_and_deaths = df_merged_cases_and_deaths.rename(columns={'number':'deaths'})


   # df_merged_cases_and_deaths = df_merged_cases_and_deaths.sort_values(by=['Deaths','cases'],ascending=False)
    df_merged_cases_and_deaths = df_merged_cases_and_deaths.sort_values(by=['cases','deaths'],ascending=False)
    contar = df_merged_cases_and_deaths["disease"]
    indices = []
    cont = 1
    for _ in contar:
        indices.append(cont)
        cont += 1
    id = indices
    df_merged_cases_and_deaths["id"] = id
    #df_merged_cases_and_deaths = df_merged_cases_and_deaths.reset_index(drop=True).assign(id=lambda df: df.index)
    df_merged_cases_and_deaths = df_merged_cases_and_deaths.reindex(columns=["id","disease","deaths","cases"])
    return df_merged_cases_and_deaths



# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    entries: pd.DataFrame = pd.read_csv("data/tycho-fixed.csv", sep=",")

    merged_cases_and_deaths:  pd.DataFrame = merge_cases_and_deaths(entries)

    print(merged_cases_and_deaths.head(10))


# -----------------------------------------------------------------------------
