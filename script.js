// Function to toggle the visibility of the booking form
function toggleBookingForm() {
    const bookingForm = document.querySelector('.booking-form');
    bookingForm.style.display = bookingForm.style.display === 'block' ? 'none' : 'block';
}

// Function to handle form submission (you can modify this as needed)
function handleFormSubmit(event) {
    event.preventDefault(); // Prevent the default form submission behavior
    const doctorSelect = document.getElementById('doctor');
    const selectedDoctor = doctorSelect.options[doctorSelect.selectedIndex].text;
    const selectedDate = document.getElementById('date').value;
    
    // You can customize the logic to handle the form data (e.g., send it to a server)
    
    // For this example, we'll just display an alert
    alert(`Appointment booked with ${selectedDoctor} on ${selectedDate}`);
}

// Add event listeners
document.addEventListener('DOMContentLoaded', () => {
    // Toggle booking form visibility when the "Book Appointment" button is clicked
    const bookButtons = document.querySelectorAll('.book-button');
    bookButtons.forEach((button) => {
        button.addEventListener('click', toggleBookingForm);
    });
    
    // Handle form submission when the form is submitted
    const bookingForm = document.querySelector('.booking-form form');
    bookingForm.addEventListener('submit', handleFormSubmit);
});