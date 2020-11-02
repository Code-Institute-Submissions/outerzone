/* 
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
*/

let stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
let client_secret = $('#id_client_secret').text().slice(1,-1);
let stripe = Stripe(stripe_public_key);
let elements = stripe.elements();

let style = {
    base: {
        color: '#000',
        fontFamily: '"Oswald", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    }
}

let card = elements.create('card', {style:style});

card.mount('#card-element');