<script src="https://cdn.jsdelivr.net/npm/@cuberto/mouse-follower@1/dist/mouse-follower.min.js"></script>

document.addEventListener("DOMContentLoaded", function () {
    const cursor = new MouseFollower({
        container: document.body,  
        speed: 0.5,  
        ease: 0.1,   
        skewing: 2,  
        skewingText: 2,
        stateDetection: {
            '-pointer': 'a, button' 
        }
    });
});
