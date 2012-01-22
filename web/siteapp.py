
from flask import Flask
app = Flask(__name__)

from flask import render_template, request, url_for, redirect, make_response, abort

@app.route('/')
def home():
    return render_template("index.html")



#@app.route("/instagram", methods=["GET","POST"])
#def instagram():    
#    #from quantifi.lib.instagram.client import InstagramAPI

#    client_id = 'XXX'
#    client_secret = 'XX'
#    
##  redirect_uri needs match what is registered online with the instagram API
#    #redirect_uri = 'http://%s' % app.config['SITE_DOMAIN'] + url_for('instagram')   # for production environment
#    redirect_uri = 'http://localhost:5000/instagram'  # for dev environment

#    if 'code' in request.args:

#        CODE = request.args['code']

#        url = "https://api.instagram.com/oauth/access_token"

#        data = {
#            "client_id": client_id,
#            "client_secret": client_secret,
#            "redirect_uri": redirect_uri,
#            "grant_type": "authorization_code",
#            "code": CODE
#        }        
#        urlencoded_data = urllib.urlencode(data)

#        http_object = Http(disable_ssl_certificate_validation=True)
#        response, content = http_object.request(url, method="POST", body=urlencoded_data)
#        parsed_content = json.loads(content)

#        if int(response['status']) != 200:
#            print "RESPONSE: %s" % response
#            print "\n"
#            print "CONTENT: %s" % content
#            raise ValueError(parsed_content.get("message", ""))

#        user_identifier = parsed_content["user"]["id"]
#        access_token = parsed_content['access_token']
#        

#        oauth_click="https://api.instagram.com/oauth/authorize/?client_id={{client_id}}&redirect_uri={{redirect_uri}}&response_type=code"

#        

#        from pymongo.connection import Connection

#        connection = Connection()
#        db = connection.psite_db
#        auths = db.auths

#        new_auth = { api: "instagram",
#            user_identifier : user_identifier,  # external api
#            access_token: access_token }
#        
#        
#        old_auth = auths.find_one({api: "instagram", username: fullname})
#        
#        if not old_auth:
#            db.auths.save(new_auth)
#        
#        else:
#            db.auths.update({"api":"instagram", "user_identifier": "user_identifier"}, {"$set": {"access_token": "access_token"}})
#        
#        





#        api = db.session.query(API).filter_by(name='instagram').first()

#        api_connection = db.session.query(APIUserConnection).filter_by(api=api, user=current_user).first()
#        if not api_connection:
#            api_connection = APIUserConnection(user_identifier=user_identifier, user=current_user, api=api)
#            db.session.add(api_connection)        
#        api_connection.access_token = access_token

#        db.session.commit()

#        quantifi_app.sync_user(current_user, apis=[api.name])

#        return redirect(url_for('settings'))            

#    return render_template("api_connectors/instagram.html", client_id=client_id, redirect_uri=redirect_uri)

if __name__ == '__main__':
    app.run()
