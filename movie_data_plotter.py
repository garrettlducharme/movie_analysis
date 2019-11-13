"""
This module contains two functions for making some horizontal bar graphs.
They are not included in the technical notebook because of their length.
"""

import matplotlib.pyplot as plt

def plot_genre_counts(df, top_n = 10):
    """Accepts the cleaned and joined dataframe as an argument. If no top_x
       is given, the top 10 most frequent genres will be plotted.
    """
    
    genre_count_dict = {}
    
    for i, genres in enumerate(df.genres):
        for genre in genres:
            if genre not in genre_count_dict:
                genre_count_dict[genre] = 1
            else:
                genre_count_dict[genre] += 1
                
    sorted_genre_counts = sorted(genre_count_dict.items(), key = lambda kv: kv[1])
    genres, counts = zip(*sorted_genre_counts)
    
    lbound = len(genre_count_dict) - top_n
    ubound = len(genre_count_dict)
    
    print(sorted_genre_counts)
    
    plt.figure(figsize = (12,4))
    plt.barh(range(len(genre_count_dict))[lbound:ubound], counts[lbound:ubound], align = 'center')
    plt.yticks(range(len(genre_count_dict))[lbound:ubound], genres[lbound:ubound]);
    plt.title('Number of Genre Appearances in the Top 101 Most Popular Movies')
    plt.ylabel('Genre')
    plt.xlabel('Counts')
    
def plot_avg_genre_stats(df, col_name, top_n = 10):
    """Accepts the the cleaned and joined dataframe and a column name as an argument.
       If top_n is not supplied, the top 10 genres for the given average over the column
       name will be plotted.
    """
    
    col_name_dict = {}
    genre_count_dict = {}
    
    for i, genres in enumerate(df.genres):
        for genre in genres:
            if genre not in col_name_dict.keys():
                col_name_dict[genre] = df[col_name].iloc[i]
                genre_count_dict[genre] = 1
            else:
                col_name_dict[genre] += df[col_name].iloc[i]
                genre_count_dict[genre] += 1
                
    avg_stats = {k: col_name_dict[k] / genre_count_dict[k] for k \
               in col_name_dict if k in genre_count_dict}
    
    sorted_stats = sorted(avg_stats.items(), key = lambda kv: kv[1])
    genres, stats = zip(*sorted_stats)
    
    lbound = len(genre_count_dict) - top_n
    ubound = len(genre_count_dict)
    
    plt.figure(figsize = (12,4))
    plt.barh(range(len(avg_stats))[lbound:ubound], stats[lbound:ubound], align = 'center')
    plt.yticks(range(len(avg_stats))[lbound:ubound], genres[lbound:ubound]);
    plt.title(f'Average {col_name.capitalize()} for top 101 Movies by Genre')
    plt.ylabel('Genre')
    plt.xlabel(f'Average {col_name.capitalize()}')