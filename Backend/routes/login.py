from flask import Blueprint, request, render_template, session

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
  
    if username == "admin" and password == "test":
        session['username'] = username
        return render_template('admin_dashboard.html')
        
    elif username == "driver" and password == "test":
        session['username'] = username
        return render_template('driver_dashboard.html')
        
    elif username == "sponsor" and password == "test":
        session['username'] = username
        return render_template('sponsor_dashboard.html')
        
    else:
        return "Invalid credentials. Please press back and try again."

@auth_bp.route('/profile')
def profile():
    if 'username' not in session:
        return render_template('FrontPage.html') 
    
    current_user = session['username']
    
    mock_user_data = {
        "username": current_user,
        "email": f"{current_user}@example.com",
        "user_type": current_user.capitalize()
    }
    
    return render_template('profile.html', user=mock_user_data)

@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('FrontPage.html')