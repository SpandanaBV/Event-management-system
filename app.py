from flask import Flask, flash, session,redirect,url_for, send_file, render_template, request
from PIL import Image, ImageDraw, ImageFont
import random
import io
import base64
from datetime import datetime, date
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'spandana'


#dummy to run all
@app.route('/login', methods=['GET', 'POST'])
def admin_login():
    return render_template('admin/index.html')



#Mock data to simulate the database
admin_users = {
    'spandana': generate_password_hash('nikola369')
}

@app.route('/admin_login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in admin_users and check_password_hash(admin_users[username], password):
            session['adminsession'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('admin/index.html')


# Define routes
@app.route('/dashboard')
def dashboard():
       # Retrieve data from your database or wherever you're storing it
    # Replace these placeholders with actual data retrieval code
    listedcategories = 10
    listedsponsers = 20
    totalevents = 30
    regusers = 40
    totalbookings = 50
    newbooking = 15
    confirmedbooking = 25
    cancelledbooking = 5
    regsubscribers = 100

    # Pass the data to the template
    return render_template('admin/dashboard_new.html',
                           listedcategories=listedcategories,
                           listedsponsers=listedsponsers,
                           totalevents=totalevents,
                           regusers=regusers,
                           totalbookings=totalbookings,
                           newbooking=newbooking,
                           confirmedbooking=confirmedbooking,
                           cancelledbooking=cancelledbooking,
                           regsubscribers=regsubscribers)

@app.route('/profile')
def profile():
    return render_template('admin/admin_profile.html')

# Mock Category Data
mock_category = {
    'id': 1,
    'CategoryName': 'Mock Category',
    'CategoryDescription': 'This is a mock description.',
    'IsActive': True,
    'UpdationDate': datetime.now().date()


}


# Mock data for categories and sponsors
mock_categories = [
    {'id': 1, 'CategoryName': 'Music'},
    {'id': 2, 'CategoryName': 'Art'},
    {'id': 3, 'CategoryName': 'Technology'},
]

mock_sponsor = [
    {'id': 1, 'sponserName': 'Sponsor1'},
    {'id': 2, 'sponserName': 'Sponsor2'},
    {'id': 3, 'sponserName': 'Sponsor3'},
]

# Mock Sponser Data
mock_sponser = {
    'id': 1,
    'sponserName': 'Mock Sponser',
    'sponserLogo': 'mock_logo.jpg',
    'postingDate': datetime.now()
}



@app.route('/edit_sponser/<int:sponserid>', methods=['GET', 'POST'])
def edit_sponser(sponserid):
    sponser = mock_sponser
    msg = None
    if request.method == 'POST':
        sponser['sponserName'] = request.form['sponser']
        msg = "Sponser info updated."
        return render_template('admin/edit_sponser.html', sponser=sponser, msg=msg)
    return render_template('admin/edit_sponser.html', sponser=sponser)


mock_event = {
    'id': 1,
    'EventName': 'Mock Event',
    'EventStartDate': datetime(2023, 6, 15).date(),
    'EventEndDate': datetime(2023, 6, 16).date(),
    'CategoryId': 1,
    'SponserId': 1,
    'EventDescription': 'This is a mock event description.',
    'EventLocation': 'Mock Location',
    'EventImage': 'mock_image.jpg'
}

@app.route('/edit_category/<int:catid>', methods=['GET', 'POST'])
def edit_category(catid):
    category = mock_category
    if request.method == 'POST':
        category['CategoryName'] = request.form['category']
        category['CategoryDescription'] = request.form['description']
        category['IsActive'] = bool(int(request.form['status']))
        category['UpdationDate'] = datetime.now().date()
        msg = "Category updated."
        return render_template('admin/edit_category.html', category=category, msg=msg)
    return render_template('admin/edit_category.html', category=category)

@app.route('/edit_event/<int:eventid>', methods=['GET', 'POST'])
def edit_event(eventid):
    event = mock_event
    if request.method == 'POST':
        event['EventName'] = request.form['eventname']
        event['EventDescription'] = request.form['eventdescription']
        event['EventStartDate'] = datetime.strptime(request.form['eventstartdate'], '%Y-%m-%d').date()
        event['EventEndDate'] = datetime.strptime(request.form['eventenddate'], '%Y-%m-%d').date()
        event['EventLocation'] = request.form['eventlocation']
        msg = "Event updated."

        mock_event['CategoryId'] = int(catid)
        mock_event['SponserId'] = int(spnserid)
        mock_event['EventName'] = ename
        mock_event['EventDescription'] = edescription
        mock_event['EventStartDate'] = datetime.datetime.strptime(esdate, '%Y-%m-%d').date()
        mock_event['EventEndDate'] = datetime.datetime.strptime(eedate, '%Y-%m-%d').date()
        mock_event['EventLocation'] = elocation

        flash('Success: Event details updated successfully', 'success')
        return redirect(url_for('admin/edit_event'))

    return render_template('admin/edit_event.html', event=mock_event, categories=mock_categories, sponsors=mock_sponsors)


    #     return render_template('admin/edit_event.html', event=event, msg=msg)
    # return render_template('admin/edit_event.html', event=event)

# @app.route('/edit_event', methods=['GET', 'POST'])
# def edit_event():
#     if request.method == 'POST':
#         # Get form data
#         eventid = request.args.get('sid')
#         catid = request.form['category']
#         spnserid = request.form['sponser']
#         ename = request.form['eventname']
#         edescription = request.form['evetndescription']
#         esdate = request.form['eventstartdate']
#         eedate = request.form['eventenddate']
#         elocation = request.form['eventlocation']

        # Update mock_event data (in a real application, update the database)


# Mock data to simulate the database
users = {
    1: {
        'Userid': 1,
        'FullName': 'Spandana B V',
        'UserName': 'spandana',
        'Emailid': 'spandanabv1018@example.com',
        'PhoneNumber': '1234567890',
        'UserGender': 'female',
        'IsActive': 1,
        'RegDate': datetime(2023, 10, 1),
        'LastUpdationDate': datetime(2024, 10, 1)
    }
}

@app.route('/edit_user/<int:uid>', methods=['GET', 'POST'])
def edit_user(uid):
    # if 'adminsession' not in session:
    #     return redirect(url_for('logout'))

    user = users.get(uid)
    if not user:
        flash("User not found.", "danger")
        return redirect(url_for('manage_users'))

    if request.method == 'POST':
        user['FullName'] = request.form['name']
        user['Emailid'] = request.form['email']
        user['PhoneNumber'] = request.form['phonenumber']
        user['UserGender'] = request.form['gender']
        user['IsActive'] = int(request.form['status'])
        user['LastUpdationDate'] = datetime.now()

        flash("Success: Profile updated successfully.", "success")
        return redirect(url_for('manage_users'))

    return render_template('admin/edit_user.html', user=user)


@app.route('/change_password')
def change_password():
    return render_template('admin/change_password.html')

@app.route('/logout')
def logout():
    return "You have been logged out."

@app.route('/new-bookings')
def new_bookings():
    return render_template('admin/new_bookings.html')

@app.route('/booking_details/<int:bkid>')
def booking_details(bkid):
    return render_template('admin/booking_details.html', bkid=bkid)

@app.route('/add-category')
def add_category():
    return render_template('admin/add_category.html')

@app.route('/manage-category')
def manage_category():
    return render_template('admin/manage_category.html')

@app.route('/add_sponsor', methods=['GET', 'POST'])
def add_sponsor():
    return render_template('admin/add_sponsor.html')


@app.route('/manage-sponsors')
def manage_sponsors():
    return render_template('admin/manage_sponsors.html')

@app.route('/add_event')
def add_event():
    return render_template('admin/add_event.html')

@app.route('/manage-events')
def manage_events():
    return render_template('admin/manage_events.html')

@app.route('/manage-users')
def manage_users():
    return render_template('admin/manage_users.html')

@app.route('/manage-subscribers')
def manage_subscribers():
    return render_template('admin/manage_subscribers.html')

@app.route('/all_bookings')
def all_bookings():
    return render_template('admin/all_bookings.html')

@app.route('/cancelled_bookings')
def cancelled_bookings():
    return render_template('admin/cancelled_bookings.html')

@app.route('/confirmed_bookings')
def confirmed_bookings():
    return render_template('admin/confirmed_bookings.html')


@app.route('/generate_captcha')
def generate_captcha():
    text = str(random.randint(10000, 99999))
    session["vercode"] = text
    width, height = 65, 25

    # Create an image with a white background
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)

    # Choose a font and size
    font = ImageFont.truetype("arial.ttf", 14)

    # Draw the text on the image
    draw.text((5, 5), text, fill='black', font=font)

    # Save the image to a BytesIO object
    image_io = io.BytesIO()
    image.save(image_io, format='JPEG', quality=80)
    image_io.seek(0)

    # Encode the image data as base64
    image_data_base64 = base64.b64encode(image_io.getvalue()).decode('utf-8')

    # Pass the base64-encoded image data to the template
    return render_template('admin/captcha.html', captcha_image=image_data_base64)

       # return send_file(image_io, mimetype='image/jpeg')


    # Pass the image data to the template
    #return render_template('admin/captcha.html', captcha_image=image_io.read().encode('base64'))


# Verify captcha
@app.route('/verify_captcha', methods=['POST'])
def verify_captcha():
    user_input = request.form.get('captcha_input')
    vercode = session.get('vercode')
    if vercode and user_input == vercode:
        return "Captcha is correct!"
    else:
        return "Captcha is incorrect!"



@app.route('/add_news')
def add_news():
    return render_template('admin/add_news.html')

@app.route('/manage-news')
def manage_news():
    return render_template('admin/manage_news.html')

@app.route('/about_us')
def about_us():
    return render_template('admin/about_us.html')

@app.route('/update_about_us', methods=['POST'])
def update_about_us():
    return redirect(url_for('about_us'))  # Redirect to about us page after successful update

# Function to handle editing event image
@app.route('/edit_event_image', methods=['GET', 'POST'])
def edit_event_image():
    if request.method == 'POST':
        # Handle form submission
        evtid = request.form['evntid']
        event_image = request.files['eventimage']
        if event_image:
            # Get file extension
            _, extension = os.path.splitext(event_image.filename)
            extension = extension.lower()

            # Check if file extension is allowed
            allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
            if extension not in allowed_extensions:
                return "Invalid file format. Only jpg, jpeg, png, and gif formats are allowed."

            # Generate new file name
            img_new_file = str(random.getrandbits(32)) + extension

            # Save image to server
            event_image.save(os.path.join('eventimages', img_new_file))

            # Update event image in database
            # Code to update database goes here

            return "Event image updated successfully!"
        else:
            return "No image selected!"

    else:
        # Handle GET request
        evtid = request.args.get('evntid')
        # Fetch event details from database
        # Code to fetch event details goes here
        event_details = {'id': evtid, 'EventName': 'Sample Event', 'EventImage': 'sample.jpg'}  # Sample data
        return render_template('admin/change_event_image.html', event=event_details)

@app.route('/website-setting')
def website_setting():
    return render_template('admin/website_setting.html')

if __name__ == '__main__':
    app.run(debug=True)
