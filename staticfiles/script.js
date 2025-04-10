const hamburger = document.querySelector('.hamburger');
const navMobile = document.querySelector('.nav-mobile');
const openMenu = document.querySelector('.open-menu');
const closeMenu = document.querySelector('.close-menu');
const dropdown = document.querySelector('.dropdown');
const dropdownMobile = document.querySelector('.dropdown-mobile');

hamburger.addEventListener('click', () => {
    navMobile.classList.toggle('active');
    openMenu.style.display = navMobile.classList.contains('active') ? 'none' : 'block';
    closeMenu.style.display = navMobile.classList.contains('active') ? 'block' : 'none';
    document.body.classList.toggle('mobile-menu-open', navMobile.classList.contains('active'));
});

function checkDestopMode() {
    if (window.innerWidth > 808) {
        document.body.classList.remove('mobile-menu-open');
        navMobile.classList.remove('active');
        openMenu.style.display = 'block';
        closeMenu.style.display = 'none';
    }
}

window.addEventListener('resize', checkDestopMode);
checkDestopMode();

if (dropdown) {
    dropdown.addEventListener('çlick', (event) => {
        if (event.target.classList.contains('dropdown-icon') || event.target.parentNode.classList.contains('dropdown-icon')) {
            dropdown.classList.toggle('active');
        }
    });
}

//Dropdown toggle for mobile 
if (dropdownMobile) {
    dropdownMobile.addEventListener('çlick', (event) => {
        if (event.target.classList.contains('dropdown-icon-mobile') || event.target.parentNode.classList.contains('dropdown-icon-mobile')) {
            event.preventDefault();
            dropdown.classList.toggle('active');
        }
    });
}

const openFormBtn = document.getElementById('openFormBtn');
const PartnerForm = document.getElementById('partnerForm');
const closeBtn = document.querySelector('.close-btn');

openFormBtn.addEventListener('click', () => {
    PartnerForm.style.display = 'flex';
    setTimeout(() => {
        PartnerForm.classList.add('active');
    }, 10)
})

closeBtn.addEventListener('click', () => {
    PartnerForm.classList.remove('active');
    setTimeout(() => {
        PartnerForm.style.display = 'none';;
    }, 300)
})

window.addEventListener('click', (event) => {
    if (event.target === PartnerForm) {
        PartnerForm.classList.remove('active');
        setTimeout(() => {
            PartnerForm.style.display = 'none';;
        }, 300)
    }
})

const volunteerForm = document.getElementById('volunteerForm')

function openForm() {
    document.getElementById('volunteerForm').style.display = 'flex';
}

function closeForm() {
    document.getElementById('volunteerForm').style.display = 'none';
}

window.addEventListener('click', (event) => {
    if (event.target === volunteerForm) {
        document.getElementById('volunteerForm').style.display = 'none';
    }
})

const joinForm = document.getElementById('joinForm')

function openJoinForm() {
    document.getElementById('joinForm').style.display = 'flex';
}

function closeJoinForm() {
    document.getElementById('joinForm').style.display = 'none';
}

window.addEventListener('click', (event) => {
    if (event.target === joinForm) {
        document.getElementById('joinForm').style.display = 'none';
    }
})