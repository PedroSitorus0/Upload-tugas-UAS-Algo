// script.js

document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const body = document.body;

    // Cek preferensi tema dari local storage atau sistem operasi
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        body.className = savedTheme;
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        body.className = 'dark-mode';
    } else {
        body.className = 'light-mode';
    }

    themeToggleBtn.addEventListener('click', () => {
        if (body.classList.contains('light-mode')) {
            body.classList.remove('light-mode');
            body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark-mode');
        } else {
            body.classList.remove('dark-mode');
            body.classList.add('light-mode');
            localStorage.setItem('theme', 'light-mode');
        }
    });

    // Anda bisa menambahkan array kutipan untuk mengubahnya secara dinamis
    const quotes = [
        {
            quote: "Satu-satunya cara untuk melakukan pekerjaan hebat adalah mencintai apa yang Anda lakukan.",
            author: "Steve Jobs"
        },
        {
            quote: "Masa depan adalah milik mereka yang percaya pada keindahan mimpi-mimpi mereka.",
            author: "Eleanor Roosevelt"
        },
        {
            quote: "Hidup ini sangat sederhana, tapi kita bersikeras membuatnya rumit.",
            author: "Confucius"
        },
        {
            quote: "Jika Anda ingin hidup bahagia, ikatlah pada tujuan, bukan pada orang atau benda.",
            author: "Albert Einstein"
        }
    ];

    const quoteText = document.getElementById('quote-text');
    const authorName = document.getElementById('author-name');

    // Fungsi untuk menampilkan kutipan acak
    function displayRandomQuote() {
        const randomIndex = Math.floor(Math.random() * quotes.length);
        const randomQuote = quotes[randomIndex];
        quoteText.textContent = `"${randomQuote.quote}"`;
        authorName.textContent = `— ${randomQuote.author}`;
    }

    // Tampilkan kutipan acak saat pertama kali dimuat
    displayRandomQuote();

    // Anda juga bisa menambahkan tombol untuk mengganti kutipan secara manual jika diinginkan
    // Misalnya, event listener pada card itu sendiri:
    const quoteCard = document.querySelector('.quote-card');
    quoteCard.addEventListener('click', (event) => {
        // Hanya ganti kutipan jika tidak mengklik tombol toggle
        if (event.target !== themeToggleBtn && !themeToggleBtn.contains(event.target)) {
            displayRandomQuote();
        }
    });
});