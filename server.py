from flask import Flask, render_template, redirect, url_for, request
import views


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    return app

app = create_app()

@app.route('/admin_home_page', methods=['GET', 'POST'])
def admin_home_page():
    return views.admin_home_page()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return views.login_page(request)

@app.route('/hotels/<int:id>', methods=['GET', 'POST'])
def home(id):
    return views.hotel_page(id)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return views.home_page()

@app.route('/firms/<int:id>', methods=['GET', 'POST'])
def firms_page(id):
    return views.firms_page(id)

@app.route('/driver_list/<int:id>', methods=['GET', 'POST'])
def driver_list_page(id):
    return views.driver_list_page(id)

@app.route('/driver_profile/<int:id>', methods=['GET', 'POST'])
def driver_profile_page(id):
    return views.driver_profile_page(id)

@app.route('/driver_edit/<int:id>', methods=['GET', 'POST'])
def driver_edit_page(id):
    return views.driver_edit_page(id)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return views.signup_page()

if __name__ == "__main__":
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)
