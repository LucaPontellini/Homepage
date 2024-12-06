from Pontellini_006 import Credit_Card, PayPal, make_payment

def test_credit_card_process_payment(capfd):
    credit_card_payment = Credit_Card(
        "Mario Rossi", "1234 5678 9012 3456", "12/23", "123"
    )
    credit_card_payment.process_payment()
    captured = capfd.readouterr()
    assert "Credit Card payment processing for Mario Rossi" in captured.out

def test_paypal_process_payment(capfd):
    paypal_payment = PayPal("mario.rossi@example.com", "password123")
    paypal_payment.process_payment()
    captured = capfd.readouterr()
    assert (
        "Payment processing with PayPal for mario.rossi@example.com" in captured.out
    )

def test_make_payment_credit_card(capfd):
    credit_card_payment = Credit_Card(
        "Mario Rossi", "1234 5678 9012 3456", "12/23", "123"
    )
    make_payment(credit_card_payment)
    captured = capfd.readouterr()
    assert "Credit Card payment processing for Mario Rossi" in captured.out

def test_make_payment_paypal(capfd):
    paypal_payment = PayPal("mario.rossi@example.com", "password123")
    make_payment(paypal_payment)
    captured = capfd.readouterr()
    assert (
        "Payment processing with PayPal for mario.rossi@example.com" in captured.out
    )