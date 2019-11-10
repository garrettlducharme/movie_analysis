"""
TO DO:
- A function that drops movies without any revenue data
- A function that drops movies that don't make money
- Functions to remove duplicates from each data set
- Functions to remove columns we don't need. This will probably be vote_count and language
- A function to filter out all movies before 2010
- A function to join the two datasets on the titles or title_id
- If joining on title_id, another function which will create a column in
  the budgets data frame with the corresponding ids for each title
"""


def genre_ids_to_list(genre_ids):
    
    """Converts a string of genre ids from tmdb.movies.csv to a list
    
    Parameters:
    genre_ids: A string containing the genre ids
    
    Returns:
    list: A list of genre ids
    """
    
    genre_ids = genre_ids.replace('[', '') #remove left bracket
    genre_ids = genre_ids.replace(']', '') #remove right bracket
    genre_ids = genre_ids.replace(' ', '') #remove white space
    genre_ids = genre_ids.split(',') #convert to a list
    
    return genre_ids

def recast_genre(genre_id_list):
    
    """Recasts a list of genre ids to the corresponding genre names. If
       there is no genre id, the name is set as 'none'
    
    Parameters:
    genre_id_list: A list of genre ids from tmdb.movies.csv
    
    Returns:
    list: A list of genre names
    """
    
    #dictionary containing genre ids and their associated names
    genre_id_dict = {'28':'action','16':'animated','99':'documentary',
          '18':'drama','10751':'family','14':'fantasy','36':'history',
          '35':'comedy','10752':'war','80':'crime','10402':'music',
          '9648':'mystery','10749':'mystery','878':'sci-fi','27':'horror',
          '10770':'TV-movie','53':'thriller','37':'western','12':'adventure',
          '':'none'}
    
    return [genre_id_dict[x] for x in genre_id_list]

def convert_amount(amount):
    
    """Converts a dollar amount in the form '$123,456,789' to a float
    
    Parameters:
    amount: A string containing a dollar amount
    
    Returns:
    float: A float of the dollar amount
    """
    
    return float(amount[1:].replace(',','')) #remove $ and ,

def convert_money_column(mb_df):
    
    """Replaces all strings of dollar amounts in mb_df to
       floats using the convert_amount function
    
    Parameters:
    mb_df: The DataFrame from tn.movie_budgets.csv
    
    Returns:
    Dataframe: mb_df with columns containing dollar
    amounts cast as floats.
    """
    
    mb_df['production_budget'] = mb_df['production_budget'].map(convert_amount)
    mb_df['domestic_gross'] = mb_df['domestic_gross'].map(convert_amount)
    mb_df['worldwide_gross'] = mb_df['worldwide_gross'].map(convert_amount)
    
    return mb_df 
    
def create_profit_ratios(mb_df):

    """Creates new columns in mb_df with the ratios
       domestic_gross/production_cost, worldwide_gross/production_cost,
       and worldwide_gross/domestic_gross.
    
    Parameters:
    mb_df: The DataFrame from tn.movie_budgets.csv
    
    Returns:
    DataFrame: mb_df with three additional columns for the
    ratios listed above.
    """
    
    mb_df['domestic_production_ratio'] = \
    mb_df['domestic_gross']/mb_df['production_budget']
    
    mb_df['worldwide_production_ratio'] = \
    mb_df['worldwide_gross']/mb_df['production_budget']
    
    mb_df['worldwide_domestic_ratio'] = \
    mb_df['worldwide_gross']/mb_df['domestic_gross']
    
    return mb_df
    
def clean_tmdb_movies(tmdb_movies_df):
    
    """Cleans the DataFrame from tmdb.movies.csv
    
    Parameters:
    tmdb_movies_df: The DataFrame from tmdb.movies.csv
    
    Returns:
    DataFrame: A cleaned version of tmdb_movies_df
    """
    
    tmdb_movies_df['genre_ids'] = tmdb_movies_df['genre_ids'].map(genre_ids_to_list)
    tmdb_movies_df['genre_ids'] = tmdb_movies_df['genre_ids'].map(recast_genre)
    
    return tmdb_movies_df
    
def clean_movie_budgets(mb_df):
    
    """Cleans the DataFrame from tn.movie_budgets.csv
    
    Parameters:
    mb_df: The DataFrame from tn.movie_budgets.csv
    
    Returns:
    DataFrame: A cleaned version of mb_df
    """
    mb_df = convert_money_column(mb_df)
    mb_df = create_profit_ratios(mb_df)
    
    return mb_df
    