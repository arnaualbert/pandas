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
# - You can also use the solution file of question 3.
# -
# - Now, write a function that obtains the ranking of all disease that have
# - registered cases and deaths, by death_ratio.
# - The death ratio is the result of divide number of deaths by all the 
# - number of cases, multiplied by 100.
# - Finally, plot this results.
# 
# - Return parameters, in each function:
#   - Return a dataframe
#   - The dataframe must have 4 columns in this order: disease,deaths,cases,ratio_deaths
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
def get_death_ratios(entries: pd.DataFrame) -> pd.DataFrame:
    df_merged_cases_and_deaths: pd.DataFrame = (entries)

    df_total_deaths: pd.DataFrame = (entries)
    # i serch the deaths
    df_total_deaths = df_total_deaths.loc[df_total_deaths["event"] == 'DEATHS']
    #i group by disease
    df_total_deaths = df_total_deaths.groupby(by="disease").sum()
    df_total_deaths = df_total_deaths.sort_values(by=["disease"],ascending=False)
    df_total_deaths.reset_index(inplace=True)

    df_total_deaths = df_total_deaths.reindex(columns=["disease","number"])


    df_total_cases: pd.DataFrame = (entries)
    # i serch the cases
    df_total_cases = df_total_cases.loc[df_total_cases["event"] == 'CASES']
    #i group by disease
    df_total_cases = df_total_cases.groupby(by="disease").sum()
    df_total_cases = df_total_cases.sort_values(by=["disease"],ascending=False)
    df_total_cases = df_total_cases.rename(columns={'number':'cases'})
    df_total_cases.reset_index(inplace=True)
    df_total_cases = df_total_cases.reindex(columns=["disease","cases"])


    df_merged_cases_and_deaths = pd.merge(df_total_deaths,df_total_cases)
    df_merged_cases_and_deaths = df_merged_cases_and_deaths.rename(columns={'number':'deaths'})
    #here i do the id
    contar = df_merged_cases_and_deaths["disease"]
    indices = []
    cont = 1
    for _ in contar:
        indices.append(cont)
        cont += 1
    id = indices
    df_merged_cases_and_deaths["id"] = id
    #here i put the ratio
    df_merged_cases_and_deaths["ratio_deaths"] = df_merged_cases_and_deaths["deaths"] / df_merged_cases_and_deaths["cases"]  * 100
    df_merged_cases_and_deaths = df_merged_cases_and_deaths.sort_values(by=["ratio_deaths",'cases','deaths'],ascending=False)
    df_merged_cases_and_deaths = df_merged_cases_and_deaths.reset_index(drop=True).assign(id=lambda df: df.index)
    df_merged_cases_and_deaths = df_merged_cases_and_deaths.reindex(columns=["id","disease","deaths","cases","ratio_deaths"])


    return df_merged_cases_and_deaths



# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    entries: pd.DataFrame = pd.read_csv("data/tycho-fixed.csv", sep=",")

    death_ratios:  pd.DataFrame = get_death_ratios(entries)

    print(death_ratios.head(10))

    # Plot the death_ratios
    death_ratios = death_ratios.loc[:,['disease','ratio_deaths']].set_index('disease')
    death_ratios.plot(kind="barh", title="Diseases death ratio in USA (1931-1936)").get_figure().savefig("output/q4-ratio-deaths.pdf")


# -----------------------------------------------------------------------------
