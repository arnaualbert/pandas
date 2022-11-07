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
# -
# - Now, write a function that save all the data of the rows that have an
# - epi_week equal to 53.
# 
# - Return parameters, in each function:
#   - Return a dataframe, with all the rows that have an epi_week equal to 53.
#   - 
# - Hints:
#   - epi_week field 2 last characters indicate the week. 
#   - One of the years which has 53 weeks is 1936.
#   - 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
# -----------------------------------------------------------------------------
def get_rows_53_epi_week(entries: pd.DataFrame) -> pd.DataFrame:
    rows_53_epi_week: pd.DataFrame = (entries)


    epi = rows_53_epi_week["epi_week"]
    lista = []
    for e in epi:
        es = str(e)
        ano = es[4:]
        year = int(ano)
        lista.append(year)
    year = lista
    rows_53_epi_week["semana"] = year

    rows_53_epi_week.query("semana == 53",inplace=True)
    rows_53_epi_week = rows_53_epi_week.reindex(columns=["id", "epi_week", "year", "from_date", "to_date", "state", "city", "event", "disease", "number", "semana"])
    return rows_53_epi_week



# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    entries: pd.DataFrame = pd.read_csv("data/tycho-fixed.csv", sep=",")

    rows_53_epi_week:  pd.DataFrame = get_rows_53_epi_week(entries)


    print(rows_53_epi_week.head(10))





# -----------------------------------------------------------------------------
