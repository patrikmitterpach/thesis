from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

import json

from source.authentication import login_required
from source.database import get_db

bp = Blueprint('input', __name__)

VALID_CONTENT_TYPES = ["text/json", "text/xml"]

def validateRequest(request):
    print(request)
    print(request.data)

    if not request.data:
        return 400, "Empty request"
    
    if not request.content_type:
        return 400, "No content type given"
    if request.content_type.lower() not in VALID_CONTENT_TYPES:
        return 400, "Content type not accepted"
    
    if "json" in request.content_type.lower():
        try: json.loads(request.data)
        except ValueError:
            return 400, "Invalid JSON"
    import xml.etree.ElementTree as ET

    if "xml" in request.content_type:
        try:    
            tree = ET.XML(request.data)
        except ET.ParseError:
            return 400, "Invalid XML"
        
    return 200, "Success"

@bp.route('/', methods=['POST'])
def index():
    returnCode, returnMessage = validateRequest(request)
    if returnCode != 200:
        return json.dumps(
            {'Result': returnMessage}
        ), returnCode, {'ContentType':'application/json'}


    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


    # choices = request.form.get('choices')
    # created_by = request.form.get('created_by')
    # difficulty_level = request.form.get('difficulty_level')
    # question = request.form.get('question')
    # topics = request.form.get('topics')