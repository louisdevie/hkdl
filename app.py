import kihara.link

from flask import Flask, render_template
app = Flask(__name__)

@app.errorhandler(403)
def not_found(e):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def not_found(e):
    return render_template('500.html'), 500

@app.route('/dl/<link>')
def downloader(link):
    try:
        return kihara.link.get_url(link)
    except ValueError:
        return render_template('invalid_link.html', test="test")

if __name__ == '__main__':
    app.run()
