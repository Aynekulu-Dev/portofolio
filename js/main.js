// 1️⃣ Smooth scroll for navbar links
const navLinks = document.querySelectorAll(".nav-link");
navLinks.forEach(link => {
    link.addEventListener("click", function(e){
        e.preventDefault();
        const id = this.getAttribute("href").substring(1);
        document.getElementById(id).scrollIntoView({behavior:"smooth"});
    });
});

// 2️⃣ Active navbar highlight on scroll
const sections = document.querySelectorAll("section");
window.addEventListener("scroll", () => {
    let current = "";
    sections.forEach(sec => {
        const top = sec.offsetTop - 70;
        if(scrollY >= top) current = sec.getAttribute("id");
    });
    navLinks.forEach(link => {
        link.classList.remove("text-purple-700");
        if(link.getAttribute("href") === "#" + current){
            link.classList.add("text-purple-700");
        }
    });

    // Back-to-top button show/hide
    const backToTop = document.getElementById("backToTop");
    if(scrollY > 300) backToTop.classList.remove("hidden");
    else backToTop.classList.add("hidden");
});

// 3️⃣ Back-to-top button
document.getElementById("backToTop").addEventListener("click", () => {
    window.scrollTo({top:0, behavior:"smooth"});
});

// 4️⃣ Typed text effect for Hero
const typedText = document.getElementById("typed-text");
const words = ["Aynekulu", "Developer", "Data Scientist"];
let i=0, j=0;
function type() {
    if(i < words.length){
        typedText.innerText = words[i].substring(0,j+1);
        j++;
        if(j === words[i].length){ i++; j=0; setTimeout(type,500); return;}
        setTimeout(type,150);
    } else { i=0; type(); }
}
type();

// 5️⃣ Skills animation on scroll
const skills = document.querySelectorAll(".skill-card");
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if(entry.isIntersecting){
            entry.target.classList.add("scale-105", "transition-transform", "duration-500");
        }
    });
}, {threshold:0.3});
skills.forEach(skill => observer.observe(skill));

// 6️⃣ Contact form validation
document.getElementById("contactForm").addEventListener("submit", e => {
    e.preventDefault();
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();
    if(name === "" || email === "" || message === ""){
        alert("Please fill in all fields!");
        return;
    }
    if(!email.includes("@")){
        alert("Please enter a valid email!");
        return;
    }
    alert("Message sent successfully!");
    e.target.reset();
});
