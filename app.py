import kihara.link
import kihara.index
import kihara._cachedir

import requests, json

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
        url = kihara.link.get_url(link)
    except ValueError:
        return render_template('invalid_link.html')

    try:
        index = kihara.index.load_remote_index(url, link)
    except requests.HTTPError:
        return render_template('invalid_url.html', URL=url)

    index = kihara.index.parse_index(index)
    print(json.dumps(index, indent=4))
    return render_template('download_page.html', data=index['resource'][0], humanize=kihara.index.humanize_file_size)

if __name__ == '__main__':
    app.run()
