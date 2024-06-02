import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials
#from flask import escape, jsonify
import functions_framework

# Initialize Firebase Admin SDK
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

@functions_framework.http
def sendEarthQuakeEvent(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'magnitude' in request_json and 'depth' in request_json:
        magnitude = request_json['magnitude']
        depth = request_json['depth']
    elif request_args and 'magnitude' in request_args and 'depth' in request_args:
        magnitude = request_args['magnitude']
        depth = request_args['depth']
    else:
        return 'Invalid data', 400

    # Construct the message for FCM
    message = messaging.Message(
        notification=messaging.Notification(
            title='Earthquake Detected!',
            body=f'Magnitude: {magnitude} at Depth: {depth} km'
        ),
        data={
            'magnitude': magnitude,
            'depth': depth
        },
        topic='earthquake-alerts',
    )

    # Send a message to devices subscribed to the "earthquake-alerts" topic
    try:
        response = messaging.send(message)
        print('Successfully sent message:', response)
        return {'success': True, 'message_id': response}, 200  # Returns JSON with status 200
    except Exception as e:
        print('Error sending message:', str(e))
        return {'success': False, 'error': str(e)}, 500  # Returns JSON with status 500


