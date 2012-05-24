
import json

from flask import Flask
from flask import render_template, request, url_for, redirect, make_response, abort

from instagram.client import InstagramAPI
import readability

import local_settings

app = Flask(__name__)
app.debug = local_settings.DEBUG_SET

@app.route('/')
def home():


    insta_api = InstagramAPI(access_token=local_settings.INSTAGRAM_TOKEN)
    feed = insta_api.user_recent_media(count=15)
    medias = feed[0]

    rdd_api = readability.oauth(local_settings.READABILITY_CLIENT_KEY, local_settings.READABILITY_CLIENT_SECRET, token=local_settings.READABILITY_USER_TOKEN)
    bookmarks = rdd_api.get_bookmarks(limit=10)

#    ['author', 'content', 'content_size', 'date_published', 'domain', 'excerpt', 'id', 'next_page_href', 'processed', 'short_url', 'title', 'url', 'word_count']
    return render_template("index.html", medias=medias, bookmarks=bookmarks)



# used these in development to get the API token, nothing to see here
if app.debug:
    @app.route('/authorize-instagram')
    def authorize_instagram():
        from instagram import client

        redirect_uri = 'http://127.0.0.1:5000/handle-instagram-authorization'
        instagram_client = client.InstagramAPI(client_id=INSTAGRAM_CLIENT, client_secret=INSTAGRAM_SECRET, redirect_uri=redirect_uri)
        return redirect(instagram_client.get_authorize_url(scope=['basic']))


    @app.route('/handle-instagram-authorization')
    def handle_instagram_authorization():
        from instagram import client

        code = request.values.get('code')
        if not code:
            raise ValueError('Missing code')
        try:
            redirect_uri = 'http://127.0.0.1:5000/handle-instagram-authorization'
            instagram_client = client.InstagramAPI(client_id=INSTAGRAM_CLIENT, client_secret=INSTAGRAM_SECRET, redirect_uri=redirect_uri)
            access_token, instagram_user = instagram_client.exchange_code_for_access_token(code)
            if not access_token:
                raise ValueError('Could not get access token')

            print "user id:"
            print instagram_user['id']
            print 'access_token'
            print access_token

            # deferred.defer(fetch_instagram_for_user, g.user.get_id(), count=20, _queue='instagram')
        except Exception, e:
            raise ValueError('Error')
        return redirect('http://www.google.com')




if __name__ == '__main__':
    app.run()
