# Imports
import pandas  as pd

# -----------------------------------------------------------------------------
# Student name: Arnau Albert Sanchez
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question: fix_broken_tycho()
# -----------------------------------------------------------------------------
# 
# - You are given a broken Tycho dataset. Write a function to fix it.
# - The function fix_broken_tycho() must do the following:
#   1. Drop 'country' and 'url' columns
#   2. Cleanup the diseases removing the descriptions in square brackets, we don't need it. (See hint below)
#   3. Sort the dataframe by epi_week and state in alphabetical order (oldest weeks first, state order A-Z)
#   4. Add a new column called 'year' of type 'int' with the year from the epi_week.
#   5. Select rows where the years are between 1932 and 1936.
#   6. Select the rows with value 'CITY' in the column named loc_city. 
#   7. Add a new column called 'id' with a numerical unique identifier starting from 0
# 
# - Return parameters:
#   - Return the fixed entries as a dataframe.
#   - This dataframe must have this columns, in this order:
#   - ['id','epi_week', 'year', 'from_date', 'to_date', 'state', 'city', 'event', 'disease', 'number']
# 
# - Hints:
#   Step2.
#   <dataframe>.str.replace(pat=r' \[.*\]', repl='', regex=True)
#   Step5. You can use masks or this function:
#   <dataframe>.query( min_year <= year <= max_year )
# 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
#   - Run pytest to be sure you succeeded.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
def get_year(epi_week: int) -> int:

    epi_week_str: str = str(epi_week)
    year_str:     str = epi_week_str[0:4]
    year_int:     int = int(year_str)

    return year_int


# -----------------------------------------------------------------------------
def fix_broken_tycho(entries: pd.DataFrame) -> pd.DataFrame:

    fixed_entries: pd.DataFrame = (entries)

    #here i delete the columns country andurl
    fixed_entries.drop(["country"],axis=1,inplace=True)
    fixed_entries.drop(["url"],axis=1,inplace=True)

    #here i do a for loop to get the years of the epi week
    epi = fixed_entries["epi_week"]
    lista = []
    for e in epi:
        es = str(e)
        ano = es[0:4]
        year = int(ano)
        lista.append(year)
    year = lista
    fixed_entries["year"] = year
   
    #here i make a query to search the years between 1930 and 1937
    fixed_entries.query("year > 1930 & year < 1937",inplace=True)
    #here i make a query to search only the city
    fixed_entries.query("loc_type == 'CITY'",inplace=True)
    #here i sort the values
    fixed_entries.sort_values(by=["epi_week","state"],ascending=True,inplace=True)
    # her i replace the wrong thins in disease
    fixed_entries["disease"] = fixed_entries["disease"].str.replace(pat=r' \[.*\]', repl='', regex=True)
    #i reset the index
    fixed_entries = fixed_entries.reset_index(drop=True).assign(id=lambda df: df.index)
    #i put in order the index
    fixed_entries = fixed_entries.reindex(columns=['id','epi_week', 'year', 'from_date', 'to_date', 'state', 'city', 'event', 'disease', 'number'])

    return fixed_entries


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    broken_entries: pd.DataFrame = pd.read_csv("data/tycho-broken.csv", sep=",")
    fixed_entries:  pd.DataFrame = fix_broken_tycho(broken_entries)
    
    print(fixed_entries.head(20))



# -----------------------------------------------------------------------------
