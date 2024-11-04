import pytest
from Pontellini_006 import CreditCard, PayPal, process_payment

def test_credit_card_process_payment(capfd):
    credit_card_payment = CreditCard(
        "Mario Rossi", "1234 5678 9012 3456", "12/23", "123"
    )
    credit_card_payment.process_payment()
    captured = capfd.readouterr()
    assert "Processing payment with Credit Card for Mario Rossi" in captured.out

def test_paypal_process_payment(capfd):
    paypal_payment = PayPal("mario.rossi@example.com", "password123")
    paypal_payment.process_payment()
    captured = capfd.readouterr()
    assert (
        "Processing payment with PayPal for mario.rossi@example.com" in captured.out
    )

def test_process_payment_credit_card(capfd):
    credit_card_payment = CreditCard(
        "Mario Rossi", "1234 5678 9012 3456", "12/23", "123"
    )
    process_payment(credit_card_payment)
    captured = capfd.readouterr()
    assert "Processing payment with Credit Card for Mario Rossi" in captured.out

def test_process_payment_paypal(capfd):
    paypal_payment = PayPal("mario.rossi@example.com", "password123")
    process_payment(paypal_payment)
    captured = capfd.readouterr()
    assert (
        "Processing payment with PayPal for mario.rossi@example.com" in captured.out
    )