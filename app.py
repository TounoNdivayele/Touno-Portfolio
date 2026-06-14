from flask import Flask, render_template, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder='assets', static_url_path='/assets')

# Color scheme
PRIMARY = "#0b3d91"
ACCENT = "#87CEEB"
SECONDARY = "#6b7280"
CARD = "#111827"
PANEL = ACCENT
TEXT = "#ffffff"
SUBTEXT = "#d1d5db"

@app.route('/')
def home():
    return render_template('index.html', 
        primary=PRIMARY, accent=ACCENT, secondary=SECONDARY,
        card=CARD, panel=PANEL, text=TEXT, subtext=SUBTEXT)

@app.route('/about')
def about():
    return render_template('about.html',
        primary=PRIMARY, accent=ACCENT, secondary=SECONDARY,
        card=CARD, panel=PANEL, text=TEXT, subtext=SUBTEXT)

@app.route('/timeline')
def timeline():
    return render_template('timeline.html',
        primary=PRIMARY, accent=ACCENT, secondary=SECONDARY,
        card=CARD, panel=PANEL, text=TEXT, subtext=SUBTEXT)

@app.route('/matlab')
def matlab():
    return render_template('matlab.html',
        primary=PRIMARY, accent=ACCENT, secondary=SECONDARY,
        card=CARD, panel=PANEL, text=TEXT, subtext=SUBTEXT)

@app.route('/blog')
def blog():
    return render_template('blog.html',
        primary=PRIMARY, accent=ACCENT, secondary=SECONDARY,
        card=CARD, panel=PANEL, text=TEXT, subtext=SUBTEXT)

@app.route('/github')
def github():
    return render_template('github.html',
        primary=PRIMARY, accent=ACCENT, secondary=SECONDARY,
        card=CARD, panel=PANEL, text=TEXT, subtext=SUBTEXT)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html',
        primary=PRIMARY, accent=ACCENT, secondary=SECONDARY,
        card=CARD, panel=PANEL, text=TEXT, subtext=SUBTEXT)

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('assets', filename)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
