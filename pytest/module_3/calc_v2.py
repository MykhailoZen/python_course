"""
Calculator ver. 2
"""
import logging


def add(a, b):
    logging.debug("Operation: addition")
    logging.info(f"Input Values: {a} and {b}")
    result = a + b
    logging.info(f"Result: {result}")
    return result


def subtract(a, b):
    logging.debug("Operation: subtraction")
    logging.info(f"Input Values: {a} and {b}")
    result = a - b
    logging.info(f"Result: {result}")
    return result


def multiply(a, b):
    logging.debug("Operation: multiplication")
    logging.info(f"Input Values: {a} and {b}")
    result = a * b
    logging.info(f"Result: {result}")
    return result


def divide(a, b):
    logging.debug("Operation: division")
    logging.info(f"Input Values: {a} and {b}")
    if b != 0:
        result = a / b
        logging.info(f"Result: {result}")
        return result
    else:
        logging.error(f"Cannot divide by zero")
        raise ZeroDivisionError