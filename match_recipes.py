import pandas as pd
df = pd.read_csv("restaurant_food_data_100.csv")

def get_recommendations(user_ings):
    def score(row):
        dish_ings = [i.strip().lower() for i in row['ingredients'].split(',')]
        return len(set(dish_ings) & set(user_ings))
    
    df['match_score'] = df.apply(score, axis=1)
    top = df[df['match_score'] > 0].sort_values(by=['match_score', 'rating'], ascending=False).head(3)
    
    if top.empty:
        return ["Sorry, I couldn't find any matching dishes."]
    
    recommendations = []
    for _, row in top.iterrows():
        recommendations.append(f"{row['food_name']} at {row['restaurant_name']} (₹{row['price']}, ⭐{row['rating']})")
    return recommendations


