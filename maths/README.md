https://hng.tech/hire/python-developers

#===Project Description===#
This is a basic DRF api, built to accept a "number", and return the following information in JSON format, if a valid number:
1. "number": 371,
2. "is_prime": false,
3. "is_perfect": false,
4. "properties": ["armstrong", "odd"],
5. "digit_sum": 11,  // sum of its digits
6. "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" //gotten from the numbers API
if not a valid number, it returns:
1. "number": "alphabet",
2. "error": true

Features
Simple GET request to <your-domain.com>/api/classify-number?number=
Returns JSON-formatted response
Uses Django REST Framework

#===clone and open the git repo==#
gitclone https://github.com/Donchess1/Myproject.git
cd maths

#===Install Dependencies==#
pip install -r requirements.txt

#===Apply Migrations==#
python manage.py migrate

#=== Run the Development Server==#
python manage.py runserver
and access api at http://127.0.0.1:8000/

==>Endpoint URL:
 GET /api/

==> Request Format:
Method: GET
Headers:
Content-Type: application/json
Body: No body required for this request.

==> Response Format:
Content-Type: application/json
==> Response Body
{
    "slack_email": "stepabod@yahoo.com",
    "current_datetime": "2025-01-29T12:34:56.789Z",
    "github_url": "https://github.com/Donchess1/Myproject.git"
}
==> Request Example
curl -X GET http://127.0.0.1:8000/api/classify-number?number=number
