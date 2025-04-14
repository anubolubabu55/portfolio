// static/js/animation.js

// Animate elements when they come into view
$(document).ready(function() {
    // Function to check if element is in viewport
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }
    
    // Elements to animate
    const animateElements = document.querySelectorAll('.animate-on-scroll');
    
    // Function to handle animation
    function handleAnimation() {
        animateElements.forEach(element => {
            if (isElementInViewport(element)) {
                element.classList.add('animated');
            }
        });
    }
    
    // Run once on page load
    handleAnimation();
    
    // Run on scroll
    window.addEventListener('scroll', handleAnimation);
    
    // Skill progress bars animation
    $('.skill-progress').each(function() {
        const progressBar = $(this).find('.progress-bar');
        const progressValue = progressBar.data('progress');
        
        progressBar.css('width', '0%');
        
        $(window).scroll(function() {
            const position = progressBar.offset().top;
            const windowHeight = $(window).height();