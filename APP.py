from flask import Flask, render_template, request
import anime_infos

app = Flask(__name__)
data = {}

@app.route('/')
def get_username():
    return render_template('get_user.html')

@app.route('/user/anime/<id>')
def anime_info(id):
    global data
    data[id]['synopsis'] = anime_infos.API_USAGE().get_anime_sinopse(id)
    return render_template('anime_details.html', anime_info=data[id])

@app.route('/get_animes', methods=['POST'])
def get_animes():
    global data
    user_name = request.form['user']
    data = anime_infos.API_USAGE(user=user_name).start()
    return render_template('user_animes.html', data=data)

@app.route('/user/<user_name>')
def show_animes(user_name):
    return "<p>hello_world</p>"

if __name__ == '__main__':
    app.run(debug=True)
