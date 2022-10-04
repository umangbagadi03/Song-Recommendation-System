import os
from flask import Flask ,  render_template , request 

app = Flask(__name__)
@app.route("/")
def home():
   return render_template('home.html')

@app.route("/about")
def about():
   return render_template('about.html')

@app.route('/recommend', methods=['POST'])
def recommend():
   URL = request.form['URL']
   df = extract(URL)
   edm_top40 = recommend_from_playlist(songDF, complete_feature_set,       df)
   number_of_recs = int(request.form['number-of-recs'])
   my_songs = []
    
   for i in range(number_of_recs):
       my_songs.append([str(edm_top40.iloc[i,1]) + ' - '+ '"'+str(edm_top40.iloc[i,4])+'"', "https://open.spotify.com/track/"+ str(edm_top40.iloc[i,-6]).split("/")[-1]])
    

   return render_template('results.html',songs= my_songs)

if __name__ == "__main__":
    app.run(debug=True)


    
