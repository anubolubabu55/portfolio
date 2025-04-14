// static/js/main.js

$(document).ready(function() {
    // Add active class to current nav item
    const currentLocation = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentLocation) {
            link.classList.add('active');
        }
    });
    
    // Smooth scrolling for anchor links
    $('a[href^="#"]').on('click', function(event) {
        var target = $(this.getAttribute('href'));
        if (target.length) {
            event.preventDefault();
            $('html, body').stop().animate({
                scrollTop: target.offset().top - 70
            }, 1000);
        }
    });
    
    // Project filter functionality
    $('.filter-btn').on('click', function() {
        const value = $(this).attr('data-filter');
        
        if (value == 'all') {
            $('.project-item').show('1000');
        } else {
            $('.project-item').not('.' + value).hide('1000');
            $('.project-item').filter('.' + value).show('1000');
        }
        
        // Add active class to current filter button
        $('.filter-btn').removeClass('active');
        $(this).addClass('active');
    });
    
    // Contact form submission handling
    $('#contactForm').submit(function(e) {
        e.preventDefault();
        
        // Add form submission logic here
        // For now, we'll just show a success message
        $('#formSubmissionStatus').html('<div class="alert alert-success">Message sent successfully!</div>');
        $(this)[0].reset();
    });
    
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

