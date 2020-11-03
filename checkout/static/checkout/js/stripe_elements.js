/* 
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
*/

let stripePublicKey = $('#id_stripe_public_key').text().slice(1,-1);
let clientSecret = $('#id_client_secret').text().slice(1,-1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();

let style = {
    base: {
        color: '#000',
        fontFamily: '"Oswald", sans-serif',
        fontSize: '16px',
        '::placeholder': {
            color: '#8a8a8a'
        }
    },
    invalid: {
        color:'#dc3545',
        iconColor: '#dc3545'
    }
};

let card = elements.create('card', {style:style});

card.mount('#card-element');

// Handles validation errors
card.addEventListener('change', function(event) {
    let errorDiv = document.querySelector('#card-errors');
    if (event.error) {
        let html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>`
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
let form = document.querySelector('#payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if(result.error) {
            let errorDiv = document.querySelector('#card-errors');
            let html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>`
            $(errorDiv).html(html);
            card.update({'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});