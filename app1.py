import pickle
import streamlit as st

# Load the pre-trained model and data
music = pickle.load(open("C:/Users/sipis/Downloads/df", 'rb'))
similarity = pickle.load(open("C:/Users/sipis/Downloads/model", 'rb'))

def recommend(song, num_recommendations):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    for i in distances[1:num_recommendations + 1]:
        recommended_music_names.append(music.iloc[i[0]].song)

    return recommended_music_names

st.header('Music Recommender System')

music_list = music['song'].values
selected_song = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

# Add a slider for the number of recommendations
num_recommendations = st.slider("Select the number of recommendations", 1, 10, 5)

if st.button('Show Recommendations'):
    recommended_music_names = recommend(selected_song, num_recommendations)
    
    # Define rainbow text colors using HTML and CSS
    rainbow_colors = [
        "red", "orange", "yellow", "green", "blue", "indigo", "violet"
    ]
    
    # Display recommended songs with rainbow text
    for i, recommended_music_name in enumerate(recommended_music_names):
        rainbow_color = rainbow_colors[i % len(rainbow_colors)]  # Cycle through rainbow colors
        styled_text = f'<span style="color: {rainbow_color}; font-weight: bold;">{recommended_music_name}</span>'
        st.markdown(styled_text, unsafe_allow_html=True)
