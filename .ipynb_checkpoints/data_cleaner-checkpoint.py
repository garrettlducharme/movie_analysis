"""
TO DO:
- A function that drops movies that don't make money
- Functions to remove duplicates from each data set
- Functions to remove columns we don't need. This will probably be vote_count and language
- A function to filter out all movies before 2010
- Convert budgets and profits to millions
- A function to drop everything but English movies
  
- Non-technical and technical markdowns need to be put together
     - 
     
- Outline the assumptions in the presentation

- Popularity vs ratings 
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
       there is no genre id, the name is set as 'none'.
    
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


def remove_non_en(tmdb_movies_df):
    
    """Removes any non english movies from the DataFrame
    
    Parameters:
    tmdb_movies_df: A DataFrame of the data from tmdb.movies.csv
    
    Returns:
    DataFrame: tmdb_movies_df with only english movies
    """

    tmdb_movies_df = tmdb_movies_df[tmdb_movies_df['original_language'] == 'en']
    
    return tmdb_movies_df


def drop_tmdb_cols(tmdb_movies_df):
    
    """Drops unnecessary columns from tmdb_movies_df. Also filters out all
       movies created before 2010.
    
    Parameters:
    tmdb_movies_df: A DataFrame of the data from tmdb.movies.csv
    
    Returns:
    DataFrame: tmdb_movies_df with the id, original_title, and original_language, and 
               release_date columns dropped from the DataFrame
    """
    tmdb_movies_df = tmdb_movies_df[tmdb_movies_df['release_date'].str[:4].map(lambda x: int(x)) >= 2010]
    tmdb_movies_df.drop('release_date', axis = 1, inplace = True)
    tmdb_movies_df.drop(columns = ['id', 'original_title', 'original_language'], inplace = True)
    
    return tmdb_movies_df

    
def convert_amount(amount):
    
    """Converts a dollar amount in the form '$123,456,789' to a float
    
    Parameters:
    amount: A string containing a dollar amount
    
    Returns:
    float: A float of the dollar amount
    """
    
    return float(amount[1:].replace(',','')) #remove $ and ,


def drop_zero_amounts(mb_df):
    
    """Removes zeros from the profit and production cost columns of mb_df
    
    Paramaters:
    mb_df: DataFrame from tn.movie_budgets.csv
    
    Returns:
    DataFrame: mb_df minus without the zero profit movies
    """
    
    mb_df = mb_df[mb_df['production_budget ($M)'] > 0]
    mb_df = mb_df[mb_df['domestic_gross ($M)'] > 0]
    mb_df = mb_df[mb_df['worldwide_gross ($M)'] > 0]
    
    return mb_df


def filter_mb_df_dates(mb_df):
    
    """Removes movies from before 2010 from mb_df, then removes the
       release date column.
       
    Parameters:
    mb_df: DataFrame from tn.movie_budgets.csv
    
    Returns:
    DataFrame: mb_df with no movies before 2010, minus thye release date
               column
    """
    
    mb_df = mb_df[mb_df['release_date'].str[-4:].map(lambda x: int(x)) >= 2010]
    mb_df.drop('release_date', axis = 1, inplace = True)
    
    return mb_df


def convert_money_column(mb_df):
    
    """Replaces all strings of dollar amounts in mb_df to floats using
       the convert_amount function. Amounts are then represented in
       millions of dollars
    
    Parameters:
    mb_df: The DataFrame from tn.movie_budgets.csv
    
    Returns:
    Dataframe: mb_df with columns containing dollar
    amounts cast as floats
    """
    
    mb_df['production_budget'] = round(mb_df['production_budget'] \
                                       .map(convert_amount)/10**6, 1)
    mb_df['domestic_gross'] = round(mb_df['domestic_gross'] \
                                    .map(convert_amount)/10**6, 1)
    mb_df['worldwide_gross'] = round(mb_df['worldwide_gross'] \
                                     .map(convert_amount)/10**6, 1)
    
    mb_df.rename(columns = {'production_budget': 'production_budget ($M)',
                            'domestic_gross': 'domestic_gross ($M)', 
                            'worldwide_gross': 'worldwide_gross ($M)'},
                 inplace = True)
    
    return mb_df

    
def create_profit_ratios(mb_df):

    """Creates new columns in mb_df with the ratios
       domestic_gross/production_cost, worldwide_gross/production_cost,
       and worldwide_gross/domestic_gross. All profit ratios less than 1
       are dropped.
    
    Parameters:
    mb_df: The DataFrame from tn.movie_budgets.csv
    
    Returns:
    DataFrame: mb_df with three additional columns for the
    ratios listed above.
    """
    
    mb_df['domestic_production_ratio'] = \
    round(mb_df['domestic_gross ($M)']/mb_df['production_budget ($M)'], 2)
    
    mb_df['worldwide_production_ratio'] = \
    round(mb_df['worldwide_gross ($M)']/mb_df['production_budget ($M)'], 2)
    
    mb_df['worldwide_domestic_ratio'] = \
    round(mb_df['worldwide_gross ($M)']/mb_df['domestic_gross ($M)'], 2)
    
    mb_df = mb_df[mb_df['domestic_production_ratio'] >= 1]
    mb_df = mb_df[mb_df['worldwide_production_ratio'] >= 1]
    
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
    tmdb_movies_df = remove_non_en(tmdb_movies_df)
    tmdb_movies_df = drop_tmdb_cols(tmdb_movies_df)
    #Will write an external function for this
    tmdb_movies_df = tmdb_movies_df[tmdb_movies_df['vote_count'] > 100]
    
    return tmdb_movies_df

    
def clean_movie_budgets(mb_df):
    
    """Cleans the DataFrame from tn.movie_budgets.csv
    
    Parameters:
    mb_df: The DataFrame from tn.movie_budgets.csv
    
    Returns:
    DataFrame: A cleaned version of mb_df
    """
    mb_df = convert_money_column(mb_df)
    mb_df = drop_zero_amounts(mb_df)
    mb_df = create_profit_ratios(mb_df)
    mb_df = filter_mb_df_dates(mb_df)

    return mb_df


def join_dataframes(clean_tmdb_movies_df, clean_mb_df):
    
    """Joins the cleaned movie budgets and movie information DataFrames.
       The movie info DataFrame must be passed first
    
    Parameters:
    clean_mb_df: The cleaned DataFrame from tn.movie_budgets.csv
    clean_tmdb_movies_df: The cleaned DataFrame from tmdb.movies.csv
    
    Returns:
    DataFrame: A joined DataFrame from the two cleaned DataFrames
    """
    clean_mb_df.rename(columns = {'movie': 'title'}, inplace = True) #rename 'movie'
    clean_mb_df.set_index('title',inplace = True) #Set index to title
    clean_tmdb_movies_df.set_index('title',inplace = True) #set index to title
    joined_movie_df = clean_tmdb_movies_df.join(clean_mb_df, how = 'inner', rsuffix = '_budget') #join on title
    joined_movie_df.drop(columns = ['Unnamed: 0', 'id'], inplace = True)   
    joined_movie_df = joined_movie_df[~joined_movie_df.index.duplicated(keep='first')] #drop duplicates
    joined_movie_df.dropna(inplace = True) #drop nulls
    
    return joined_movie_df
    