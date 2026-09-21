from flask import Blueprint, request, render_template

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
  
  #Hard coded login information for testing  
    if username == "admin" and password == "test":
        return render_template('admin_dashboard.html')
        
    elif username == "driver" and password == "test":
        return render_template('driver_dashboard.html')
        
    elif username == "sponsor" and password == "test":
        return render_template('sponsor_dashboard.html')
        
    else:
        return "Invalid credentials. Please press back and try again."
