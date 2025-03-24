import requests
import smtplib
from email.message import EmailMessage
TRAIN_API_URL = "http://demo3278802.mockable.io/Train"
BOOK_TICKET_API_URL = "http://demo3278802.mockable.io/Booking_Details"
def search_trains(source, destination):
    params = {"source": source, "destination": destination, "date": date}
    response = requests.get(TRAIN_API_URL, params=params)
    
    if response.status_code == 200:
        trains = response.json() 
        return trains
    else:
        print("Error fetching train details.")
        return None
        
def book_ticket(train_id, passenger_name, email):
    data = {
        "train_id": train_id,
        "passenger_name": passenger_name,
        "email": email
    }
    
    response = requests.post(BOOK_TICKET_API_URL, json=data)
    
    if response.status_code == 200:
        ticket_details = response.json()
        send_email_confirmation(email, ticket_details)
        return ticket_details
    else:
        print("Error booking ticket.")
        return None
def send_email_confirmation(to_email, ticket_details):
    sender_email = "nithyanandanithin5@gmail.com" 
    sender_password = "hfom cyli atpt tpji"  
    msg = EmailMessage()
    msg["Subject"] = "Train Ticket Booking Confirmation"
    msg["From"] = sender_email
    msg["To"] = to_email
    
    message_body = f"""
    Hello,
    
    Your ticket has been successfully booked.
    
    Train Name: {ticket_details['train_name']}
    Train Number: {ticket_details['train_number']}
    Passenger Name: {ticket_details['passenger_name']}
    Seat Number: {ticket_details['seat_number']}
    Date: {ticket_details['date']}
    
    Thank you for using our service!
    """
    
    msg.set_content(message_body)
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Email confirmation sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)
if __name__ == "__main__":
    source = "holenarsipura"
    destination = "hassan"
    available_trains = search_trains(source, destination, date)
    if available_trains:
        print("Available Trains:")
        for train in available_trains:
            print(f"{train['train_id']} - {train['train_name']} ({train['departure_time']})")
   
        selected_train_id = available_trains[0]["train_id"]
        passenger_name = "abhi"
        email = "rabhi0929@gmail.com"
        
        ticket = book_ticket(selected_train_id, passenger_name, email)
        if ticket:
            print("Ticket booked successfully!")
    else:
        print("No trains available.")